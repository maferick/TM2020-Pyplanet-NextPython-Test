# Notices and attribution

This repository bundles and builds on the following GPLv3 projects. All are
used under the GNU General Public License v3 (see `LICENSE`).

## PyPlanet (vendored under `controller/pyplanet-src/`)
- Upstream: https://github.com/PyPlanet/PyPlanet
- Author: Tom Valk and PyPlanet contributors
- License: GPLv3
- Modifications in this copy: migrated to run on Python 3.12 (peewee 4 /
  peewee-async 2, aiohttp 3.10+, Jinja2 3, dropped EOL deps), plus assorted
  bugfixes and UI tweaks. See the project's CHANGELOG and commit history.

## cup_manager (vendored under `controller/project/skybaks/cup_manager/`)
- Upstream: https://github.com/skybaks/pyplanet-cup_manager
- Author: skybaks
- License: GPLv3
- Modifications in this copy: ported to the peewee 4 / Python 3.12 PyPlanet
  fork above (migration table-name fix, null-safe player fields, raw-string
  regex).

## Trackmania dedicated server image
- Image: `evoesports/trackmania` (https://github.com/EvoEsports/docker-trackmania)
- This pulls the **official, proprietary Nadeo/Ubisoft** `TrackmaniaServer`
  binary, which is NOT covered by this repository's license. It is the
  unmodified vendor binary, used under Nadeo/Ubisoft's own terms.

## MariaDB
- Image: `mariadb` (GPLv2). Used unmodified.
