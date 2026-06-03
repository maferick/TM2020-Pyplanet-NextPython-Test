"""
PyPlanet apps. The stock contrib apps plus the ported third-party plugin
skybaks.cup_manager (vendored in this image under /app/server/skybaks).
"""
APPS = {
	'default': [
		'pyplanet.apps.contrib.admin',
		'pyplanet.apps.contrib.jukebox',
		'pyplanet.apps.contrib.karma',
		'pyplanet.apps.contrib.local_records',
		'pyplanet.apps.contrib.dedimania',
		'pyplanet.apps.contrib.players',
		'pyplanet.apps.contrib.info',
		'pyplanet.apps.contrib.mx',
		'pyplanet.apps.contrib.transactions',
		'pyplanet.apps.contrib.sector_times',
		'pyplanet.apps.contrib.clock',
		'pyplanet.apps.contrib.funcmd',
		'pyplanet.apps.contrib.live_rankings',
		'pyplanet.apps.contrib.best_cps',
		'pyplanet.apps.contrib.voting',
		'pyplanet.apps.contrib.rankings',

		# Third-party plugins:
		'skybaks.cup_manager',
	]
}
