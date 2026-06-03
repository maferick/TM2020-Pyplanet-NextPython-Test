<!--
Reminder: this repo packages upstream projects. Fixes to PyPlanet core or the
cup_manager plugin are usually better sent to their own repositories. PRs here
should be about the packaging (compose, CI, env, docs) or the Python 3.12 fork.
-->

## What does this change?

## Why?

## How was it tested?
<!-- e.g. built the controller image, brought the stack up, checked the controller connects. -->

## Checklist
- [ ] Touches only this repo's scope (packaging / Py3.12 fork), not unrelated upstream behavior
- [ ] Controller still builds (`docker compose build` or the CI Action is green)
- [ ] Docs updated (`README.md` / `docs/`) if config or behavior changed
- [ ] No secrets committed (`.env` stays local)
