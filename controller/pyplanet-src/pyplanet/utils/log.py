import logging
import logging.config
import os
import sys
import traceback

from logging.handlers import QueueHandler as BaseQueueHandler

from pyplanet.conf import settings
from pyplanet.core.exceptions import ImproperlyConfigured


IGNORED_PATHS = [
	'aiomysql',
]
IGNORED_TEXT = [
	'InternalError: Packet sequence number wrong',
	'Lost connection to',
	'MemoryError',
]


def initiate_logger():  # pragma: no cover
	if settings.LOGGING_CONFIG == 'logging.config.dictConfig':
		logging.config.dictConfig(settings.LOGGING)

	# If we have writing logs enabled.
	if settings.LOGGING_WRITE_LOGS:
		# Parse directory
		if settings.LOGGING_DIRECTORY:
			if os.path.isabs(settings.LOGGING_DIRECTORY):
				path = settings.LOGGING_DIRECTORY
			else:
				path = os.path.join(settings.ROOT_PATH, settings.LOGGING_DIRECTORY)

			# Create if not exists!
			if not os.path.exists(path):
				os.mkdir(path)

			path = os.path.join(path, 'pyplanet.log')
		else:
			path = os.path.join(settings.ROOT_PATH, 'pyplanet.log')

		# Determinate handler and initiate it.
		if settings.LOGGING_ROTATE_LOGS:
			handler = logging.handlers.TimedRotatingFileHandler(
				path, when='D', interval=1, backupCount=14, encoding='utf-8', delay=True
			)
		else:
			handler = logging.FileHandler(
				path, encoding='utf-8'
			)

		# Change the formatter.
		handler.setFormatter(
			logging.Formatter('[%(asctime)s][%(levelname)s][%(threadName)s] %(name)s: %(message)s (%(filename)s:%(lineno)d)')
		)

		# Add to the root handler.
		logging.root.addHandler(handler)


def handle_exception(exception=None, module_name=None, func_name=None, extra_data=None, force=False):  # pragma: no cover
	# Test for ignored exceptions
	if exception and isinstance(exception, (ImproperlyConfigured,)):
		return

	if settings.DEBUG or settings.LOGGING_REPORTING == 0:
		if exception:
			logging.exception(exception)
		return

	# Filter out exceptions.
	ignore = False
	try:
		stack = traceback.extract_stack()
		for frame in stack:
			if any(ig in frame.filename for ig in IGNORED_PATHS):
				ignore = True
				break
	except:
		pass
	try:
		if not force:
			if any(ig.lower() in str(exception).lower() for ig in IGNORED_TEXT):
				ignore = True
	except:
		pass

	if ignore:
		return

	# The remote reporting backend (raven/Sentry) has been removed. Log the
	# exception locally so it is still surfaced instead of being silently dropped.
	location = '{}.{}'.format(module_name or '?', func_name or '?')
	if exception:
		logging.error('Unhandled exception in %s', location, exc_info=exception)
	else:
		logging.error('Unhandled exception in %s', location, exc_info=sys.exc_info())


class RequireDebugFalse(logging.Filter):
	def filter(self, record):
		return not settings.DEBUG


class RequireDebugTrue(logging.Filter):
	def filter(self, record):
		return settings.DEBUG


class RequireException(logging.Filter):
	def filter(self, record):
		return bool(record.exc_info)


class QueueHandler(BaseQueueHandler):  # pragma: no cover
	def prepare(self, record):
		# Override due to bug
		self.format(record)
		record.msg = record.msg or record.message
		record.args = None
		record.exc_info = None
		return record
