# Lapin site

Public pages for Lapin ("Lapin: Ski Pass & Resort Log"), the Burrow Works ski pass app (earlier names Lift Days and
Corduroy), served by GitHub Pages from `main`.

- `privacy-policy.md`: the app's privacy policy, at `/privacy-policy`. It's a copy of `docs/privacy-policy.md` in
  the (private) app repo `burrow-works/Lapin`, which is the source; change it there first, then copy it here.
- `resorts.json`: the resort list and pass rules the app downloads (at most once a day) from
  `https://raw.githubusercontent.com/burrow-works/lapin-site/main/resorts.json` (0.70 and later; earlier builds use
  the old `Rampagingpuffin/lift-days-site` address, which GitHub redirects here), so roster fixes reach phones
  without an app update. It's a copy of `app/src/main/assets/resorts.json` built by `tools/build_roster.py` in the app
  repo. Apps install it only when its `version` is higher than theirs, its `format` is one they read, and it passes
  their checks (`RosterFile.replaces`); otherwise they keep what they have. Bump `VERSION` in `build_roster.py` for
  every change.
