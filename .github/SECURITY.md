# Security policy

Please **do not** open a public issue for security problems.

## Reporting a vulnerability in this repository

For a vulnerability in **this packaging** (the Docker stack, compose, CI, the
settings, or the Python 3.12 fork changes), use GitHub's private reporting:

- Go to the **Security** tab of this repository, then **Report a vulnerability**.

That opens a private advisory only the maintainer can see. (If the button is not
available, the maintainer needs to enable Private Vulnerability Reporting under
the repository's security settings.)

## Reporting a vulnerability in an upstream component

Many parts of this stack are not ours. Report those to the project that owns them:

- **PyPlanet** (controller core / bundled apps): <https://github.com/PyPlanet/PyPlanet>
- **cup_manager** plugin: <https://github.com/skybaks/pyplanet-cup_manager>
- **Dedicated server image**: <https://github.com/EvoEsports/docker-trackmania>
- The **Trackmania dedicated server binary** itself is Nadeo/Ubisoft's, closed
  source, and outside the scope of this project.

## Supported versions

This is a rolling project that tracks `main`; fixes land there. There are no
long-term support branches.
