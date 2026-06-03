# What's included

The controller ships with PyPlanet's bundled apps plus the `cup_manager`
plugin. Here's what each one gives you in game.

| App | What it does |
|---|---|
| **admin** | All `//` admin commands and the on-screen admin toolbar (`//toolbar`). |
| **jukebox** | Players queue maps from `/list`; the queue advances each map end. |
| **karma** | Map rating. Players vote with `++` / `--`; see `/karma`, `/whokarma`. |
| **local_records** | Per-server records on each map (`/records`, `/cp`). |
| **players** | Online player list and `/laston`. |
| **info** | Server/map info widgets and `/info`. |
| **mx** | Import maps from ManiaExchange (`//add mx <id>`, `//add search`). |
| **sector_times** | On-screen sector/checkpoint time comparison widget. |
| **best_cps** | Best-checkpoints widget during a run. |
| **live_rankings** | Live standings widget during the map. |
| **rankings** | Server-wide ranking across maps (`/rank`, `/nextrank`, `/topranks`). |
| **clock** | Optional on-screen clock (toggle in `//settings`). |
| **funcmd** | Fun chat commands (`/gg`, `/n1`, `/muffin`, ...). |
| **voting** | Chat-based votes to skip/replay/extend a map. |
| **cup_manager** | Run cups/competitions: `//cup on`, brackets, scoring, results. |

## Apps that auto-unload on Trackmania 2020

PyPlanet also bundles a few apps that only work on the older ManiaPlanet /
ShootMania titles. On a TM2020 server they detect the game and unload
themselves on startup, which is why you'll see lines like this in the logs:

```
Unloading app core.shootmania. Doesn't support the current game 'trackmania_next'!
Unloading app dedimania. Doesn't support the current game 'trackmania_next'!
Unloading app transactions. Doesn't support the current game 'trackmania_next'!
```

That is expected, not an error:

- **dedimania** — global record database, ManiaPlanet only.
- **transactions** — Planets donations/payments, ManiaPlanet only.
- **shootmania** core — ShootMania-specific, not Trackmania.

## The Python 3.12 fork bits

This controller is a modernized fork of PyPlanet brought up to Python 3.12.
A few behaviours differ from stock:

- The map **jukebox** advances on map end, so queued maps are no longer skipped
  in podium modes or left unloaded in modes without a podium.
- The PyPlanet **logo**, the **report-issue** overlay and the **clock** are
  toggle settings (default off) in `//settings`, instead of always-on.
- Dark "glass" menus and HUD widgets with a teal accent.

See [`controller/pyplanet-src/CHANGELOG.rst`](../controller/pyplanet-src/CHANGELOG.rst)
for the full list.
