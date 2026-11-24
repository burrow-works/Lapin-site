# Lapin privacy policy

Last updated 24 November 2026.

Lapin: Ski Pass & Resort Log ("Lapin") is made by Burrow Works LLC. Lapin keeps your ski days on your phone.
No account is needed and there are no ads. Burrow Works does not sell your data and does not share it for anyone else's
purposes. What the app collects and sends is described below; if that changes, this policy is updated first.

## What stays on your phone

- The passes you hold, what you paid for them and a walk-up ticket price if you enter them, your Ski Free voucher
  count and your units.
- Your home town and its map position, if you set one. It's used for distances to resorts.
- The days you log: date, resort, pass, how the day counted and your notes.
- Ski days you import from Slopes, GPX or KMZ files: the GPS track, its stats and the runs it matched.
- Ski days you record in the app: the GPS track (time, position and height every few seconds while recording), its
  stats and the runs and lifts it matched.
- Stored forecasts, and the resorts you told check-ins to skip.
- Trail maps of the resorts whose maps, pages or days you've opened, or saved over Wi-Fi.
- 3D views of the resorts whose 3D view or replay you've opened (a picture and the grid that places a track on it).
- Map backgrounds of the resorts whose maps you've opened, or saved over Wi-Fi (terrain, woods, roads, place names).
- Whether you have Lapin+: the last answer from Google Play (see Lapin+ below).

All of this is deleted when you uninstall the app or clear its storage.

## Location

Location is used for two things, each off until you choose it: Day check-ins and recording a day.

**Day check-ins** are off until you turn them on in Settings.

- When the app is open, it asks the phone where it is, to see whether you're at a resort on your passes.
- If you also allow location all the time, Android watches the area around nearby resorts on your passes. After about
  90 minutes at one, the app shows a notification asking whether to log the day. Nothing is logged unless you tap Log it.

Check-ins don't store your location.

**Recording a day** starts only when you tap Start recording or Record a day. From then until it stops, the app notes
the phone's position every 2 seconds while you're moving and every 15 seconds while you're standing still, and shows a
notification the whole time with Pause and Stop. It stops when you tap Stop, or by itself once you've been well away from
the resort for 15 minutes. The track is kept on your phone. If you log the day, it's saved with the day; if you discard
it, it's deleted.

The app never sends your location anywhere. Your phone works out its position using Google Play services, under
Google's own privacy policy. You can turn check-ins off in Settings, stop a recording, or remove the permission in
Android's settings, at any time.

## What the app sends over the internet

The app downloads forecasts, alerts and map backgrounds. Each request goes straight to the service named below and
carries only what's listed. As with any internet request, the service also sees your IP address.

- **US National Weather Service** (api.weather.gov): the map position of a US resort, to get its forecast and to
  check for storm alerts. The list of resorts asked about can show which passes you hold. Your own location is never
  sent. With powder alerts on, the forecast request also happens once a day in the background, for resorts on your
  passes within your alert distance.
- **MET Norway** (api.met.no): the map position and mid-mountain height of a resort outside the United States, to
  get its forecast. The same applies: the list can show which passes you hold, your own location is never sent, and
  with powder alerts on it also happens once a day in the background.
- **Google** (www.google.com), in test builds only: a resort's website address, to fetch its logo. The version on
  Google Play shows the resort's initials instead and never makes this request.
- **Your phone's address lookup**: the town or ZIP code you type for your home location. Android's built-in geocoder
  sends it to Google to find it on the map.
- **Google Play** (through the Play Store app on your phone): with the version from Google Play, the app asks Play
  whether your Google account has Lapin+ and what it costs where you are. See Lapin+ below.
- **Burrow Works** (api.burrowworks.app), only if you sign in to a Burrow Works account: see the account section
  below. Nothing is sent to it while you're signed out.
- **GitHub** (raw.githubusercontent.com): the list of resorts and pass rules, at most once a day, so changes reach
  you without an app update. Nothing about you is sent with it. Also a resort's trail map (its runs and lifts), the
  first time you open its map, its page or a day there, then kept on the phone; and, over Wi-Fi, the trail maps of the
  resorts on your passes within 200 miles of home, so they work with no signal. Also a resort's 3D view, the first
  time you open it or play a day back on it, then kept on the phone. The requests carry only which resort; the
  resorts chosen can show which passes you hold and roughly where you ski. Also the map background of a resort
  (its woods, roads, car parks and place names): see Amazon below.
- **Amazon Web Services** (elevation-tiles-prod.s3.amazonaws.com): terrain tiles for the area around a resort, for
  the shaded relief under its trail map. They're requested the first time you open a map of that resort, then kept on
  the phone. With map backgrounds on (Settings → Map backgrounds), the app also saves them, together with the GitHub
  file above, for the resorts on your passes within 200 miles of home, over Wi-Fi only. The requests carry only which
  map tiles or which resort; the resorts chosen can show which passes you hold and roughly where you ski. Your own
  location is never sent. Turning map backgrounds off stops these requests and deletes what was saved.

Buttons such as Website, Snow report, Niehues painting and Directions open your browser or maps app. Those apps and sites have their own
privacy policies.

## Lapin+ and Google Play

Lapin is free. Lapin+ is an optional subscription that adds features. It is sold and billed by Google Play:

- You subscribe, pay, change plan and cancel in Google Play. Your payment details go to Google, never to Burrow Works.
- Google Play tells the app on your phone whether your Google account has Lapin+, and the app keeps that answer on
  your phone. It isn't part of an export or of Android's backup, so a new phone asks Google Play again.
- Burrow Works can see the sales reports Google Play gives every developer: for example, how many people subscribed,
  in which countries, and the order details Google shares with developers. It doesn't receive your ski days, tracks,
  location or anything else in the app.
- Google handles the purchase under its own privacy policy and the Google Play terms.

Lapin+ never deletes anything. If it ends, what you made with it (planned days, prices you typed) stays on your phone
and comes back if you subscribe again.

## The Burrow Works account (optional)

Burrow Works makes Lapin and Puffly. If you sign in with Google to a Burrow Works account (Settings → Burrow Works
account), one subscription unlocks both apps: Lapin+ in Lapin and Puffly+ in Puffly. Nothing else in Lapin needs an
account, and without one everything works as described above.

- **What is sent when you sign in:** the sign-in token Google gives the app, so our server (api.burrowworks.app) can
  check it with Google. The server keeps Google's number for your account (a user ID), not your email address or
  name. The app shows your email address from your phone's own Google sign-in; it isn't sent.
- **What is sent while you're signed in:** the Google Play purchase token of your Lapin+ subscription, if you have
  one, and which app is asking. The server asks Google Play about that token and keeps what Google says: which
  product, whether it is active or renewing, when it runs out, and whether it was refunded. Google Play also tells the
  server when a subscription renews, is cancelled or is refunded. The server answers the app with a record it signs,
  which the app keeps on your phone. A purchase made while you're signed in carries your account's number, so it
  lands on the right account.
- **What is never sent:** your ski days, tracks, recordings, location, passes, plans or anything else in the app.
- **Who sees it:** Burrow Works, on servers run by Cloudflare for us. It is not sold or shared for anyone else's
  purposes. Together with Puffly's subscription it lets the apps tell you if you're paying for both, so you can cancel
  one.
- **Deleting it:** Settings → Burrow Works account → Delete account, in Lapin or Puffly, or at
  https://api.burrowworks.app/delete-account. This deletes the account, its sign-ins and the record of its
  subscriptions from the server at once. Subscriptions are Google Play's and keep running until you cancel them in
  Google Play. Signing out removes the account from your phone but keeps it on the server until you delete it.

## Backups

- **Export visits** saves your logged days to a file in the place you choose. What happens to that file is up to you.
- If Android backup to your Google account is turned on, Android may include the app's data in that backup. You
  control this in Android's settings.

## Imported files

Files you share to Lapin or pick in Settings are read on your phone. Their tracks are kept on your phone and are
not uploaded. The same goes for the days you record.

## Children

Lapin isn't directed at children under 13 and doesn't knowingly collect anything from them.

## Changes

If this policy changes, the new version will be posted here with a new date.

## Contact

Questions about this policy: hello@burrowworks.app

© Burrow Works LLC
