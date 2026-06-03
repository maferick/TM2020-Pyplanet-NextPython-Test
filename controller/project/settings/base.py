"""
PyPlanet base settings. Env-driven: every secret comes from the container
environment (set via the .env file / compose), nothing sensitive lives here.
"""
import os

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
TMP_PATH = os.path.join(ROOT_PATH, "tmp")
if not os.path.exists(TMP_PATH):
	os.mkdir(TMP_PATH)

DEBUG = bool(os.environ.get("PYPLANET_DEBUG", False))

POOLS = ["default"]

OWNERS = {
	"default": [o for o in os.environ.get("PYPLANET_OWNERS", "").split(",") if o],
}

SELF_UPGRADE = False

DATABASES = {
	"default": {
		"ENGINE": "peewee_async.MySQLDatabase",
		"NAME": os.environ.get("DB_NAME", "pyplanet"),
		"OPTIONS": {
			"host": os.environ.get("DB_HOST", "db"),
			"port": int(os.environ.get("DB_PORT", "3306")),
			"user": os.environ.get("DB_USER", "pyplanet"),
			"password": os.environ.get("DB_PASSWORD", "pyplanet"),
			"charset": "utf8mb4",
		},
	}
}

DEDICATED = {
	"default": {
		"HOST": os.environ.get("DEDICATED_HOST", "dedicated"),
		"PORT": os.environ.get("DEDICATED_PORT", "5000"),
		"USER": "SuperAdmin",
		"PASSWORD": os.environ.get("DEDICATED_PASSWORD", "SuperAdmin"),
	}
}

MAP_MATCHSETTINGS = {
	"default": os.environ.get("MAP_MATCHSETTINGS", "maplist.txt"),
}

BLACKLIST_FILE = {
	"default": "blacklist.txt",
}

STORAGE = {
	"default": {
		"DRIVER": "pyplanet.core.storage.drivers.local.LocalDriver",
		"OPTIONS": {},
	}
}

SONGS = {
	"default": [],
}
