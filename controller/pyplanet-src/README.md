<div align="center">

# 🏁 PyPlanet · vdlaken fork

**A modernized fork of [PyPlanet](https://github.com/PyPlanet/PyPlanet), the async server controller for Trackmania (2020) and ManiaPlanet, brought up to Python 3.12.**

![Python](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-3776AB?logo=python&logoColor=white)
![peewee](https://img.shields.io/badge/peewee-4.x-2ecc71)
![peewee--async](https://img.shields.io/badge/peewee--async-2.x-2ecc71)
![aiohttp](https://img.shields.io/badge/aiohttp-3.x-2ecc71)
![version](https://img.shields.io/badge/version-0.12.0-e67e22)
![license](https://img.shields.io/badge/license-GPLv3-lightgrey)
![fork](https://img.shields.io/badge/fork%20of-PyPlanet-2ad8a0)

</div>

---

Upstream PyPlanet is pinned to the **end-of-life Python 3.8** stack (see upstream [issue #1370](https://github.com/PyPlanet/PyPlanet/issues/1370)). This fork runs the controller (core + bundled apps) on current Python with current dependencies, plus a handful of robustness and cosmetic improvements on top.

> **Scope:** the bundled controller is fully migrated. Third-party plugins that define their own database models may still need their own peewee 4 pass (the same kind of changes applied here).

## ✨ What's different from upstream

| Area | Upstream | This fork |
|------|----------|-----------|
| Python | 3.8 (EOL) | **3.12** (3.11+ supported, forward to 3.13) |
| ORM | peewee 2.10 + peewee-async 0.5 (`Manager`) | **peewee 4 + peewee-async 2** (rebuilt on `AioModel`, same façade) |
| HTTP / templates | aiohttp 3.8, Jinja2 2.11 | aiohttp 3.x, Jinja2 3.x |
| Dead dependencies | raven, cached-property, async_generator, asyncio_extras | removed (stdlib / no Sentry) |

### 🔧 Functional fixes
- **Resilient scores:** a player who disconnects right at a scores event no longer voids the entire round's results (was an unguarded `asyncio.gather` + a 4s `get_player` stall raising `PlayerNotFound`). One disconnect can no longer drop the batch.
- **Player desync self-heal:** gbx callbacks are dispatched concurrently, so a quick reconnect could leave a ghost or missing player. `map_loaded` now reconciles the online set against the authoritative player list each map.
- **Background tasks:** fire-and-forget `ensure_future` calls are routed through a `run_detached` helper that keeps a strong reference and logs exceptions instead of silently dropping them.
- **Python 3.10+ correctness:** removed the dropped `asyncio.open_connection(loop=...)`, `collections.abc` fixes, `distutils` to `sysconfig`, raw-string regex, and friends.

### 🎨 Cosmetic
- Dark "glass" menus and HUD widgets (replacing the legacy beige panels), with a teal accent line.
- Removed the bottom-right PyPlanet logo and the "report issue" overlay.
- Version bumped to **0.12.0**.

## 🎮 Running it

This fork is built automatically and deployed alongside a dedicated server:

```
Gitea Actions  ──▶  registry.vdlaken.eu/pyplanet:latest  ──▶  Portainer stack "pyplanet-tm"
                                                               ├── dedicated  (evoesports/trackmania, TM2020)
                                                               ├── db         (MariaDB)
                                                               └── pyplanet   (this image)
```

Configuration is env-driven (database, dedicated XML-RPC, owners) through a mounted `settings/base.py`, so no secrets live in the image. For general installation and configuration of vanilla PyPlanet, see the upstream docs at [pypla.net](http://pypla.net/).

## 🧩 Plugins

- [**cup_manager**](https://github.com/skybaks/pyplanet-cup_manager) (competition / cup management) is ported to this fork and running. In-game namespace: `//cup`.

## 🙏 Credits

- **PyPlanet** by Tom Valk and contributors, the original controller. http://pypla.net/
- **cup_manager** by [skybaks](https://github.com/skybaks).

This is a private fork for a self-hosted Trackmania server and is not affiliated with or endorsed by the upstream project.

## 📄 License

GPLv3, same as upstream. See [LICENSE](LICENSE).
