"""
This folder contains the configuration in different files. This init file imports
all files in the current directory to combine them into one settings module.
Documentation: http://pypla.net/
"""

from .base import *
from .apps import *

try:
	from .local import *
except ImportError:
	pass
