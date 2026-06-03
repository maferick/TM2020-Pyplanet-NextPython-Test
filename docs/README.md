# Documentation

Everything you need to run and use this server, without leaving the repo.

- **[commands.md](commands.md)** — in-game chat commands (player and admin).
- **[configuration.md](configuration.md)** — environment variables, owners and
  admin levels, maps, and updating.
- **[features.md](features.md)** — what each bundled app/plugin does, and which
  apps auto-unload on Trackmania 2020.

## First steps after the server is up

1. **Join it.** Find it in the in-game server browser under your
   `TM_SERVER_NAME`, or use the join link the dedicated prints in its logs.
2. **Become admin.** Put your login in `PYPLANET_OWNERS` (see
   [configuration](configuration.md)), or paste the one-time `/claim <code>`
   token from the controller logs into chat.
3. **Open the toolbar.** Type `//toolbar` for the admin button bar, or
   `//settings` for the settings window.
4. **Add maps.** `//add mx <id>` pulls a map from ManiaExchange by its id.
5. **Queue maps.** Players open `/list` and click a map to jukebox it.

## Quick reference

| I want to... | Do this |
|---|---|
| See player commands in game | `/help` |
| See admin commands in game | `//help` |
| Skip the current map | `//skip` (admin) or `/skip` (start a vote) |
| Add a map from ManiaExchange | `//add mx <id>` |
| Change a setting | `//settings` |
| Change game mode settings | `//modesettings` |
| Run a cup | `//cup on` |
| Rate the current map | type `++` or `--` in chat |

## Further reading

These docs cover this server. For deep dives into PyPlanet internals, writing
your own plugin, or the full ManiaScript/GBX background, the upstream project
documents it at <http://pypla.net/>. This is an independent Python 3.12 fork and
is not affiliated with the upstream project.
