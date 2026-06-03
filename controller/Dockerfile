# PyPlanet controller, running our modernized Python 3.12 fork with the
# ported skybaks.cup_manager plugin baked in. Fully self-contained: the
# controller source is vendored under pyplanet-src/ (no external pip index
# or private registry needed).
FROM python:3.12-slim

LABEL org.opencontainers.image.title="pyplanet-controller (Python 3.12 fork)" \
      org.opencontainers.image.licenses="GPL-3.0-or-later"

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app/server \
    PYPLANET_SETTINGS_METHOD=python \
    PYPLANET_SETTINGS_MODULE=settings

# Build deps for PyPlanet's native wheels (cryptography / bcrypt / etc.).
RUN apt-get -q update \
 && apt-get install -y --no-install-recommends \
        build-essential libssl-dev libffi-dev zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

RUN addgroup --gid 1000 maniaplanet \
 && adduser --uid 1000 --gid 1000 --system maniaplanet

# Install the vendored, modernized PyPlanet.
COPY pyplanet-src/ /build/pyplanet-src/
RUN pip install /build/pyplanet-src && rm -rf /build

# Project: manage.py, settings, and the vendored cup_manager plugin
# (importable as skybaks.cup_manager via PYTHONPATH=/app/server).
COPY project/ /app/server/
RUN chown -R maniaplanet:maniaplanet /app

WORKDIR /app/server/
USER maniaplanet

ENTRYPOINT [ "python3", "manage.py" ]
CMD [ "start", "--pool=default", "--settings=settings" ]
