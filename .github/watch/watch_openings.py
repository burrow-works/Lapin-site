"""Daily opening-date watcher for Lapin (runs in GitHub Actions; no AI, no keys).

For every North American resort on a pass that hasn't confirmed it opened this season (resorts.json + events.json in
this repo), fetch the resort's own home page, pull out the sentences that talk about opening ("Opening day is Saturday,
December 5", "We're open!", "targeting Dec 12"), and compare them with the last run (state.json next to this file).
Resorts whose sentences changed are listed on one GitHub issue labelled `openings`, for a person (or Claude) to
check and add to Lapin's tools/data/season_dates.csv. Nothing here writes a date: a misread page must never publish
an opening.

Polite: robots.txt is honoured, one request per site per day, a plain identifying User-Agent, 20 s timeouts.
"""
import concurrent.futures as cf
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import urllib.robotparser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
STATE = os.path.join(HERE, "state.json")
UA = "LapinOpeningWatch/1.0 (+https://github.com/burrow-works/lapin-site)"
MONTHS = r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?"
DAYS = r"(?:mon|tues|wednes|thurs|fri|satur|sun)day"
WHEN = re.compile(rf"\b(?:{MONTHS}\s+\d{{1,2}}\b|\d{{1,2}}(?:st|nd|rd|th)?\s+(?:of\s+)?{MONTHS}|{DAYS}|today|tomorrow|this weekend)", re.I)
OPENING = re.compile(
    r"\b(?:opening\s+(?:day|date|weekend)|(?:we\s*(?:'|’)?re|we are|now|is)\s+open\b|open(?:s|ing)?\s+(?:for\s+the\s+season|on|this|next)"
    r"|target(?:s|ing|ed)?\b|(?:plan|hope|aim)(?:s|ing|ed)?\s+to\s+open|first\s+(?:chair|day)"
    r"|delay(?:s|ed|ing)?\s+(?:our\s+|the\s+)?opening|postpone(?:s|d)?)",
    re.I,
)
TAGS = re.compile(r"<(script|style|noscript|svg|template)\b.*?</\1>|<!--.*?-->", re.I | re.S)


def text_of(page: str) -> str:
    page = TAGS.sub(" ", page)
    page = re.sub(r"<(br|p|div|li|h\d|section|article|header|footer|span|a)\b[^>]*>", " \n ", page, flags=re.I)
    page = re.sub(r"<[^>]+>", " ", page)
    return re.sub(r"\s+", " ", html.unescape(page)).strip()


def snippets(text: str, limit: int = 4) -> list[str]:
    """Passages about opening that also say when; the same wording each day gives the same passage."""
    spans = []
    for m in OPENING.finditer(text):
        # A window around the phrase, cut at word edges ("Dec. 12" would break a cut at sentence ends).
        start, end = max(0, m.start() - 120), min(len(text), m.end() + 140)
        if start > 0:
            start = text.find(" ", start) + 1
        if end < len(text):
            end = max(text.rfind(" ", m.end(), end), m.end())
        if spans and start <= spans[-1][1]:
            spans[-1][1] = max(spans[-1][1], end)    # overlapping windows are one passage
        else:
            spans.append([start, end])
    out = []
    for start, end in spans:
        s = text[start:end].strip(" .|-–—")
        if WHEN.search(s) and len(s) >= 12 and s not in out:
            out.append(s[:400])
        if len(out) >= limit:
            break
    return out


def season_start(today: dt.date) -> dt.date:
    return dt.date(today.year if today.month >= 8 else today.year - 1, 8, 1)


def watch_list(today: dt.date) -> list[dict]:
    roster = json.load(open(os.path.join(ROOT, "resorts.json"), encoding="utf-8"))["resorts"]
    seasons = json.load(open(os.path.join(ROOT, "events.json"), encoding="utf-8")).get("seasons", {})
    start = season_start(today)
    out = []
    for r in roster:
        if r.get("country") not in ("US", "CA") or not r.get("access") or not r.get("website"):
            continue
        tags = r.get("tags") or []
        tags = set(tags.split() if isinstance(tags, str) else tags)
        if ("xc" in tags or "sightseeing" in tags) and "alpine" not in tags:
            continue
        s = seasons.get(r["id"], {})
        opens = s.get("opens")
        # Confirmed open this season already: nothing left to watch for until spring.
        if opens and not s.get("target") and start <= dt.date.fromisoformat(opens) <= today:
            continue
        out.append({"id": r["id"], "name": r["name"], "url": r["website"], "known": opens, "target": bool(s.get("target"))})
    return out


def allowed(url: str) -> bool:
    p = urllib.parse.urlsplit(url)
    rp = urllib.robotparser.RobotFileParser()
    try:
        req = urllib.request.Request(f"{p.scheme}://{p.netloc}/robots.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=10) as r:
            rp.parse(r.read().decode("utf-8", "replace").splitlines())
    except Exception:
        return True  # no robots.txt (or unreachable): the page fetch decides
    return rp.can_fetch(UA, url)


def fetch(item: dict) -> tuple[str, list[str] | None]:
    url = item["url"]
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        if not allowed(url):
            return item["id"], None
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(3_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
        return item["id"], snippets(text_of(body))
    except Exception:
        return item["id"], None


def report(changed: list[tuple[dict, list[str]]], today: dt.date, first: bool) -> str:
    lines = [
        f"**{today.isoformat()}**: {len(changed)} resort page(s) changed what they say about opening"
        + (" (first sweep: everything the pages say today)" if first else "") + ".",
        "",
        "Check each, then add confirmed or announced dates to Lapin's `tools/data/season_dates.csv` "
        "(`target=yes` for a day a resort is only aiming for), rebuild `events.json` and push it here.",
        "",
    ]
    for item, snips in changed:
        known = f" · in the app: {item['known']}{' (target)' if item['target'] else ''}" if item["known"] else ""
        lines.append(f"- **{item['name']}** (`{item['id']}`) · {item['url']}{known}")
        lines += [f"  > {s}" for s in snips]
    text = "\n".join(lines)
    return text if len(text) < 60000 else text[:60000] + "\n\n…cut here (GitHub's limit); the rest waits for the next run."


def main() -> int:
    today = dt.date.fromisoformat(os.environ.get("TODAY") or dt.date.today().isoformat())
    items = watch_list(today)
    old = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else None
    seen = dict(old or {})
    changed = []
    with cf.ThreadPoolExecutor(16) as pool:
        for rid, snips in pool.map(fetch, items):
            if snips is None:          # unreachable today: keep what we had, report nothing
                continue
            before = set((old or {}).get(rid, []))
            if set(snips) - before and snips:
                changed.append((next(i for i in items if i["id"] == rid), [s for s in snips if s not in before]))
            seen[rid] = snips
    json.dump(dict(sorted(seen.items())), open(STATE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    reached = sum(1 for i in items if i["id"] in seen)
    print(f"watched {len(items)} resorts, {len(changed)} changed")
    changed.sort(key=lambda c: c[0]["name"])
    if changed:
        open(os.path.join(HERE, "report.md"), "w", encoding="utf-8").write(report(changed, today, old is None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
