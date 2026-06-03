# In-game commands

PyPlanet has two kinds of chat commands:

- **`/command`** — player commands, anyone on the server can use them.
- **`//command`** — admin commands, only owners/admins can use them.

> In game you can always type **`/help`** for the live list of player commands and **`//help`** for admin commands. That list is generated from exactly what your server has loaded, so it is the authoritative reference. The tables below cover the common ones.

Owners (set via `PYPLANET_OWNERS`, see [configuration](configuration.md)) automatically have every admin command. New admins can also be added in-game with `//level`.

## Player commands

| Command | Aliases | What it does |
|---|---|---|
| `/list` | | Open the map list. Search maps and click one to **jukebox** (queue) it. |
| `/jukebox list` | | Show the current jukebox queue. |
| `/records` | | Local records on the current map. |
| `/cpcomparison` | `/cp` | Compare your checkpoint times with the local record and the ideal line. |
| `/scoreprogression` | `/progression` | Your time/score progression on the current map. |
| `/karma` | | Show the current map's rating. |
| `/whokarma` | | Show who voted what on the current map. |
| `/resetkarma` | | Reset your own karma vote on this map. |
| `++` / `--` | `+++`/`---` | Type in chat to vote the map up/down (triple for a strong vote). |
| `/rank` | | Your current server rank. |
| `/nextrank` | | The player just ahead of you in the ranking. |
| `/topranks` | | Top ranked players on this server. |
| `/topsums` | | Players with the most top records. |
| `/topactive` | | Most active players (time spent on the server). |
| `/stats` | | Your personal statistics. |
| `/players` | | Players currently online. |
| `/laston <login>` | `/lastseen` | When a player was last seen here. |
| `/info` | | Info about the current map. |
| `/help` | | List all available player commands. |

### Fun commands

`/gg` (good game), `/n1` (nice one), `/nt` (nice try/time), `/ns` (nice shot), `/muffin <login>` (give a muffin), `/afk` (mark yourself away), `/bootme` (leave the server), `/rq` / `/ragequit`.

### Chat votes (player-started)

`/skip`, `/replay`, `/restart` (`/res`), `/extend`, `/previous` (`/prev`) start a chat vote. Others vote with `/y` (`/yes`) or `/n` (`/no`).

## Admin commands

### Match flow
| Command | Aliases | What it does |
|---|---|---|
| `//skip` | `//next` | Skip to the next map immediately. |
| `//restart` | `//res`, `//rs` | Restart the current map. |
| `//replay` | | Replay the current map (re-queues it). |
| `//previous` | `//prev` | Switch to the previously played map. |
| `//extend` | | Extend the time limit on the current map. |
| `//endround` | | End the current round. |
| `//pause` / `//unpause` | `//resume`, `//endpause` | Pause / resume the match. |
| `//endwu` / `//endwuround` | | End the warm-up / the current warm-up round. |
| `//pointsrepartition` | `//pointsrep` | Change how round points are distributed. |

### Maps
| Command | Aliases | What it does |
|---|---|---|
| `//add mx <id>` | `//add tmx <id>` | Download and add a map from ManiaExchange / TMX by id. |
| `//add local` | | Add a map already on the server's disk (file browser). |
| `//add random` | | Add random maps from ManiaExchange. |
| `//add search <query>` | | Search ManiaExchange and add results. |
| `//remove` | | Remove the current/selected map from the playlist. |
| `//erase` | | Remove and delete the map from disk. |
| `//shuffle` | | Shuffle the playlist. |
| `//clearjukebox` | `//cjb` | Clear the jukebox queue. |
| `//writemaplist` / `//readmaplist` | `//wml` / `//rml` | Save / load the playlist to/from disk. |
| `//localmaps` | | Browse local map files. |

### Players
| Command | Aliases | What it does |
|---|---|---|
| `//kick <login>` | | Kick a player. |
| `//ban` / `//unban` | | Ban / unban (until server restart). |
| `//blacklist` / `//unblacklist` | `//black` / `//unblack` | Permanent ban / remove. |
| `//addguest` / `//removeguest` | | Add / remove a guest (always-allowed player). |
| `//mute` / `//unmute` | `//ignore` / `//unignore` | Hide / show a player's chat. |
| `//forcespec` / `//forceplay` | | Force a player into spectator / player slot. |
| `//forceteam` / `//switchteam` | | Assign / switch a player's team. |
| `//warn` | `//warning` | Send a warning popup to a player. |
| `//level <login> <level>` | | Set a player's admin level (see configuration). |

### Server & settings
| Command | Aliases | What it does |
|---|---|---|
| `//settings` | | Open the PyPlanet/plugin settings window. |
| `//modesettings` | | View/change the current game mode settings. |
| `//mode` | | Change the game mode. |
| `//servername <name>` | | Change the server name. |
| `//setpassword` / `//setspecpassword` | `//srvpass` / `//spectpass` | Set play / spectator password. |
| `//setmaxplayers` / `//setmaxspectators` | | Set player / spectator slot limits. |
| `//chat` | | Enable/disable public chat. |
| `//toolbar` | | Toggle the on-screen admin button bar. |
| `//cancel` / `//pass` | | Cancel / pass the current chat vote. |
| `//cancelcallvote` | `//cancelcall` | Cancel the current in-game (server) callvote. |
| `//reboot` | | Restart the PyPlanet controller. |

### Cups (cup_manager plugin)
| Command | Aliases | What it does |
|---|---|---|
| `//cup on` | `//cup start` | Start a cup on this server. |
| `//cup off` | `//cup stop` | Stop the running cup. |
| `//cup edit` | | Edit the active cup. |
| `//cup setup` | `//cup s` | Open the cup setup/presets window. |
| `//cup mapcount` / `//cup edition` / `//cup scoremode` | | Tune maps-per-match, edition number, scoring. |
| `//cup matches` | `//cup m` | Manage the cup's matches. |
| `/cups` | | View cups (player). |

cup_manager can use optional `presets`, `payouts` and `names` config; until those are set you will see harmless "config missing" lines in the logs. See the plugin's own readme for that config format.
