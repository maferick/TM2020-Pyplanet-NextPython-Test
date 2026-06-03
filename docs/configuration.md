# Configuration

Everything is configured through environment variables (your `.env` file), so
you normally never edit Python. Copy `.env.example` to `.env` and fill it in.

## Environment variables

| Variable | Used by | Notes |
|---|---|---|
| `MYSQL_ROOT_PASSWORD` | db | MariaDB root password. |
| `MYSQL_PASSWORD` | db + controller | Password for the `pyplanet` database user. |
| `DB_NAME` / `DB_USER` | db + controller | Default `pyplanet` / `pyplanet`. |
| `TM_MASTERSERVER_LOGIN` | dedicated | Your dedicated-server account login (from trackmania.com). |
| `TM_MASTERSERVER_PASSWORD` | dedicated | That account's password. |
| `TM_SERVER_NAME` | dedicated | Public name in the server browser. Supports `$` color/style codes. |
| `XMLRPC_SUPERADMIN` | dedicated + controller | Password the controller logs in with. Pick a strong value. |
| `XMLRPC_ADMIN` / `XMLRPC_USER` | dedicated | Lower-privilege XML-RPC passwords. |
| `TM_SERVER_MAX_PLAYERS` | dedicated | Player slots (default 32). |
| `TM_SERVER_MAX_SPECTATORS` | dedicated | Spectator slots (default 32). Separate pool from players. |
| `TM_UPLOADRATE` / `TM_DOWNLOADRATE` | dedicated | Bandwidth in kbit/s. Raise for many players/spectators. |
| `PYPLANET_OWNERS` | controller | Comma-separated player logins that become owners (full admin). |
| `MAP_MATCHSETTINGS` | controller | MatchSettings file the controller manages. **Must match the file the dedicated loads** (the evoesports image uses `default.txt`). |

## Owners and admin levels

PyPlanet has four permission levels:

| Level | Name | Typical use |
|---|---|---|
| 0 | Player | Everyone. |
| 1 | Operator | Map/round control. |
| 2 | Admin | Player moderation + most settings. |
| 3 | Master (owner) | Everything, including managing other admins. |

- Logins listed in `PYPLANET_OWNERS` are **masters** automatically.
- If no owner is set, the controller prints a one-time `/claim <code>` token in its logs on startup. Paste that in chat to claim master rights.
- Change another player's level in-game with `//level <login> <level>`.

## Maps and MatchSettings

Maps and MatchSettings live in the shared `userdata` volume under
`UserData/Maps/`. The dedicated server seeds a default set on first start.
Add more with `//add mx <id>` (downloads from ManiaExchange) or `//add local`.
Use `//writemaplist` to persist the current list.

## Changing app behaviour

The list of enabled apps lives in `controller/project/settings/apps.py`, and the
core settings in `controller/project/settings/base.py` (both baked into the
image). Most day-to-day tuning is done live in-game via `//settings` and
`//modesettings` instead, so you rarely need to touch these files. If you do,
edit them in the repo, push, and redeploy the stack.

## Does it survive a reboot? (persistence)

Yes. You do **not** redo setup after a restart or host reboot. State lives in
two Docker volumes that outlive the containers:

- **`dbdata`** (MariaDB) holds everything PyPlanet stores: local records, karma,
  player admin levels, server rankings, cup data, and all `//settings` values.
  So any setting you change via `//settings` persists automatically.
- **`userdata`** (shared with the dedicated) holds the maps, MatchSettings,
  blacklist, and the dedicated's config files.

The dedicated's server config (name, passwords, slots, bandwidth) is re-applied
from your **environment variables** on every start, so those persist too.

The **one** thing that does not persist is a setting changed *live over XML-RPC*
that isn't backed by an env var, for example `//setmaxplayers`. Those revert to
the configured value on restart. That's exactly why server-config settings
should be set via env (e.g. `TM_SERVER_MAX_PLAYERS`) rather than a live command:
set it in the env and it's permanent.

Removing the volumes (e.g. `docker compose down -v`) is the only thing that
wipes the database and maps, so avoid `-v` unless you really mean it.

## Updating

- **Controller / plugins:** edit the repo, push; CI republishes the image; pull
  it and redeploy the stack.
- **Dedicated server:** `docker compose pull dedicated && docker compose up -d`.
- Restarting the **controller** is safe and does not disconnect players.
  Restarting the **dedicated** kicks everyone, so avoid it during events.
