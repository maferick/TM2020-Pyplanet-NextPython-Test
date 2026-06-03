<div align="center">

# TM2020 PyPlanet (Next Python) Stack

**A complete Trackmania 2020 server in one `docker compose up`:**
the official Nadeo dedicated server + a **modernized, Python 3.12** build of
[PyPlanet](https://github.com/PyPlanet/PyPlanet) + the
[cup_manager](https://github.com/skybaks/pyplanet-cup_manager) plugin, wired
together with MariaDB.

![Python](https://img.shields.io/badge/python-3.12-blue)
![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-GPLv3-green)
![PyPlanet](https://img.shields.io/badge/PyPlanet-0.12%20(3.12%20fork)-orange)

</div>

---

## What is this?

PyPlanet is a server controller for Trackmania: it adds the in-game admin menu,
local records, karma, map jukebox, live rankings, map search, cup management and
much more on top of the bare dedicated server.

Upstream PyPlanet is pinned to the **end-of-life Python 3.8** stack. This repo
ships a copy that has been **migrated to run on Python 3.12** (peewee 4 /
peewee-async 2, aiohttp 3.10+, Jinja2 3, EOL dependencies dropped), with a few
bugfixes and UI tweaks on top, and the popular `cup_manager` plugin ported to
match and baked in.

Everything needed to run it is **vendored in this repository**. There is no
dependency on PyPI for the controller, no private registry, and no manual
plugin install. Clone, fill in a `.env`, and bring it up.

## What's inside

```
.
├── docker-compose.yml          # db + dedicated + controller, wired together
├── .env.example                # all settings & secrets (copy to .env)
└── controller/                 # the PyPlanet controller image build context
    ├── Dockerfile              # builds the Python 3.12 fork + bakes in cup_manager
    ├── pyplanet-src/           # vendored modernized PyPlanet (GPLv3)
    └── project/
        ├── manage.py
        ├── settings/           # env-driven base.py + app list
        └── skybaks/cup_manager # vendored ported plugin (GPLv3)
```

Three containers:

| Service      | Image                          | Role                                   |
|--------------|--------------------------------|----------------------------------------|
| `dedicated`  | `evoesports/trackmania`        | Official Nadeo TM2020 server (port 2350) |
| `controller` | built from `./controller`      | PyPlanet 3.12 fork + cup_manager        |
| `db`         | `mariadb:11`                   | Controller database                     |

## Quick start

1. **Get a dedicated-server account.** Create one (free) at
   <https://www.trackmania.com/player/dedicated-servers>. You get a login and
   password used as `TM_MASTERSERVER_LOGIN` / `TM_MASTERSERVER_PASSWORD`.

2. **Configure.**
   ```bash
   cp .env.example .env
   # edit .env: dedicated account, XML-RPC passwords, your owner login
   ```

3. **Bring it up.**
   ```bash
   docker compose up -d --build
   ```
   First build compiles the controller image (a few minutes). The controller
   waits for the database and the dedicated server, then runs its migrations and
   connects.

4. **Find it in game.** Trackmania > Play > Local / LAN or the server browser,
   under the `TM_SERVER_NAME` you set.

5. **Become admin.** Put your Ubisoft/Trackmania login in `PYPLANET_OWNERS`
   (comma-separated for multiple). Owners get the full `//` admin command set
   and the in-game admin menu.

### Handy commands

```bash
docker compose logs -f controller     # watch the controller
docker compose restart controller     # safe: reconnects, does NOT kick players
docker compose pull dedicated && docker compose up -d   # update the server image
```

> Restarting **controller** is safe and does not disconnect anyone. Restarting
> **dedicated** kicks everyone, so avoid it during events.

## Configuration

All configuration is environment driven via `.env` (see `.env.example` for the
full list). The controller settings live in `controller/project/settings/` and
read those variables, so you normally never edit Python to configure the server.

Maps and MatchSettings live in the shared `userdata` volume under
`UserData/Maps/`. Point `MAP_MATCHSETTINGS` at your MatchSettings file.

## Notes on the Python 3.12 fork

The migration keeps PyPlanet's public APIs intact, so stock contrib apps and
third-party plugins work unchanged after a small peewee-4 pass. Highlights:

- ORM rebuilt on `peewee_async.AioModel` + the `aio_*` methods, same call sites.
- Jukebox advances on `map_end` instead of `podium_start` (fixes skipped/again-
  loaded maps in modes with or without a podium).
- Map search result cap raised, plus assorted resilience fixes.

See `controller/pyplanet-src/CHANGELOG.rst` and the commit history for details.

## License & credits

This repository is **GPLv3** (see `LICENSE`). It builds on:

- **PyPlanet** by Tom Valk and contributors (GPLv3)
- **cup_manager** by skybaks (GPLv3)
- **evoesports/trackmania** Docker image, which wraps the **official,
  proprietary Nadeo/Ubisoft** server binary (used under Nadeo/Ubisoft's terms,
  not covered by this repo's license)

See `NOTICE.md` for full attribution and the list of local modifications.
