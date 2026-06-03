"""
Helpers for running coroutines in the background ("fire and forget") without
losing exceptions or risking the task being garbage collected while pending.
"""
import asyncio
import logging

logger = logging.getLogger(__name__)

#: Strong references to in-flight background tasks. asyncio only keeps a weak
#: reference to a running task, so without this set the garbage collector can
#: drop a task while it is still pending. See the asyncio.ensure_future docs.
_background_tasks = set()


def run_detached(coro, *, name=None):
	"""
	Schedule ``coro`` to run in the background without awaiting it.

	Unlike a bare ``asyncio.ensure_future(coro)`` this keeps a strong reference
	to the task until it completes and logs any exception it raises instead of
	silently swallowing it.

	:param coro: Coroutine or future to schedule.
	:param name: Optional label used in the log message if the task fails.
	:return: The scheduled task/future.
	"""
	task = asyncio.ensure_future(coro)
	_background_tasks.add(task)
	task.add_done_callback(lambda t: _on_done(t, name))
	return task


def _on_done(task, name):
	_background_tasks.discard(task)
	if task.cancelled():
		return
	exception = task.exception()
	if exception is not None:
		logger.error(
			'Unhandled exception in background task %s', name or task,
			exc_info=exception
		)
