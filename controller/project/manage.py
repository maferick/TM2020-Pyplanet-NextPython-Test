#!/usr/bin/env python3
import os
import sys

if __name__ == '__main__':

	# Use Python for the configuration.
	os.environ.setdefault('PYPLANET_SETTINGS_METHOD', 'python')
	os.environ.setdefault('PYPLANET_SETTINGS_MODULE', 'settings')

	try:
		from pyplanet.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			'Couldn\'t import PyPlanet. Are you sure it\'s installed and '
			'available on your PYTHONPATH environment variable?'
		) from exc
	execute_from_command_line(sys.argv)
