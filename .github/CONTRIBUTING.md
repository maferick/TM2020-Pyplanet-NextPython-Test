# Contributing

Thanks for your interest. Please read this first, because **this repository is a
packaging of several upstream projects**, not their original source, so a fix or
report might actually belong somewhere else.

## What this repository is

It bundles three things into one Docker Compose stack:

1. The **official Nadeo Trackmania 2020 dedicated server** via the
   `evoesports/trackmania` image (closed-source, not ours).
2. A **modernized fork of PyPlanet** (brought up to Python 3.12), vendored under
   `controller/pyplanet-src/`.
3. The **cup_manager** plugin, vendored under
   `controller/project/skybaks/cup_manager/`.

## Where to report or fix things

| The problem is in... | Goes to |
|---|---|
| The Docker stack, compose, CI, docs, or env wiring in **this** repo | **Here** |
| Something specific to running PyPlanet on **Python 3.12** (the migration) | **Here** (and ideally raised upstream too) |
| General PyPlanet behavior, a bundled app, the UI, the controller core | [PyPlanet upstream](https://github.com/PyPlanet/PyPlanet/issues) |
| The cup_manager plugin | [skybaks/pyplanet-cup_manager](https://github.com/skybaks/pyplanet-cup_manager/issues) |
| The dedicated server image or its entrypoint | [EvoEsports/docker-trackmania](https://github.com/EvoEsports/docker-trackmania/issues) |
| The Trackmania server binary or the game itself | Nadeo/Ubisoft (closed source, nothing the projects above can fix) |

Not sure? Open an issue here and we'll help route it. The issue chooser also
links the upstream trackers directly.

## Running it locally

See the [README](../README.md). In short: copy `.env.example` to `.env`, then
either `docker compose up -d --build` (build from source) or
`docker compose pull && docker compose up -d` (use the published image).

## Making a change

1. Branch off `main`.
2. If you touch the controller (`controller/**`), the GitHub Action builds the
   image on push, keep that build green.
3. Update the docs (`docs/`, `README.md`) if behavior or config changes.
4. Open a pull request describing what changed and how you tested it.

## Scope

Changes that keep the stack self-contained and faithful to upstream are
welcome: packaging fixes, the Python 3.12 migration, docs, and small quality
improvements. Large feature work on PyPlanet or cup_manager is better done in
their own repositories so the wider community benefits.
