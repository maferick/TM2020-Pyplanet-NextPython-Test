import os
import re
from setuptools import setup, find_packages


def long_description():
	try:
		return open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()
	except IOError:
		return None


def read_version():
	with open(os.path.join(os.path.dirname(__file__), 'pyplanet', '__init__.py')) as handler:
		return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", handler.read(), re.M).group(1)


def read_requirements(filename):
	with open(os.path.join(os.path.dirname(__file__), filename), 'r') as handler:
		return [line for line in handler.readlines() if not line.startswith('#') and not line.startswith('-') and not len(line) <= 1]


EXCLUDE_FROM_PACKAGES = [
	'pyplanet.bin',
	'pyplanet.conf.app_template',
	'pyplanet.conf.project_template',
	'docs*',
	'env*',
	'tests*',
	'apps*',
	'settings*',
]

PKG = 'pyplanet'
######
setup(
	name=PKG,
	version=read_version(),
	description='Maniaplanet Server Controller',
	long_description=long_description(),
	long_description_content_type='text/markdown',
	keywords='maniaplanet, controller, plugins, apps',
	license='GNU General Public License v3 (GPLv3)',
	packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
	package_data={
		'pyplanet/tests': ['pyplanet/tests/**.txt', 'pyplanet/tests/**.json', 'pyplanet/tests/**.xml', 'pyplanet/tests/**.j2']
	},
	install_requires=read_requirements('requirements.txt'),
	extras_require={},
	include_package_data=True,
	python_requires='>=3.11',

	scripts=['pyplanet/bin/pyplanet'],
	entry_points={'console_scripts': [
		'pyplanet = pyplanet.core.management:execute_from_command_line',
	]},

	author='Tom Valk',
	author_email='tomvalk@lt-box.info',
	url='http://pypla.net/',

	classifiers=[
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Development Status :: 4 - Beta',

		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Programming Language :: Python :: 3.13',
		'Programming Language :: Python :: 3 :: Only',

		'Operating System :: OS Independent',

		'Topic :: Internet',
		'Topic :: Software Development',
		'Topic :: Games/Entertainment',
		'Topic :: Software Development :: Libraries :: Application Frameworks',
		'Topic :: Software Development :: Libraries :: Python Modules',

		'Intended Audience :: System Administrators',
		'Intended Audience :: Developers',

	],
	zip_safe=False,
)
