import datetime

import peewee
from peewee import DateTimeField
from peewee_async import AioModel

from .database import Proxy


class ObjectManager:
	"""
	Backwards compatible async query helper.

	Historically this was a ``peewee_async.Manager`` subclass. peewee-async >= 2.0
	dropped the Manager concept in favour of ``AioModel`` and the ``aio_*`` query
	methods, so this class now simply delegates to those while keeping the call
	signatures the PyPlanet apps already rely on (``Model.objects.execute(query)``,
	``Model.objects.count(query)``, ...).
	"""

	async def execute(self, query):
		return await query.aio_execute()

	async def count(self, query):
		return await query.aio_count()

	async def scalar(self, query, as_tuple=False):
		return await query.aio_scalar(as_tuple=as_tuple)

	async def get(self, model, *query, **filters):
		return await model.aio_get(*query, **filters)

	async def get_or_create(self, model, **kwargs):
		return await model.aio_get_or_create(**kwargs)

	async def create(self, model, **data):
		return await model.aio_create(**data)

	async def update(self, instance, only=None):
		return await instance.aio_save(only=only)

	async def delete(self, instance, recursive=False, delete_nullable=False):
		return await instance.aio_delete_instance(recursive=recursive, delete_nullable=delete_nullable)

	async def get_related(self, instance, related_name, single_backref=False):
		"""
		Return the related instance(s) for a relationship.

		For a forward foreign key this returns the single target instance. For a
		reverse relation (backref) it returns the result query, or the first
		instance when ``single_backref`` is True.
		"""
		model_cls = type(instance)
		related_field = getattr(model_cls, related_name)

		if isinstance(related_field, peewee.BackrefAccessor):
			query = getattr(instance, related_name)
			instances = await query.aio_execute()
			if single_backref:
				for related in instances:
					return related
				raise model_cls.DoesNotExist
			return instances

		# Forward foreign key relationship.
		foreign_key_value = getattr(instance, related_name + '_id')
		target_cls = related_field.rel_model
		target_field = related_field.rel_field
		return await target_cls.aio_get(target_field == foreign_key_value)


class Model(AioModel):
	objects = ObjectManager()

	@classmethod
	async def get(cls, *args, **kwargs):
		return await cls.aio_get(*args, **kwargs)

	@classmethod
	async def get_or_none(cls, *args, **kwargs):
		return await cls.aio_get_or_none(*args, **kwargs)

	@classmethod
	async def execute(cls, query):
		return await query.aio_execute()

	@classmethod
	async def get_or_create(cls, *args, **kwargs):
		return await cls.aio_get_or_create(*args, **kwargs)

	@classmethod
	async def create(cls, **insert):
		return await cls.aio_create(**insert)

	async def save(self, *args, **kwargs):
		return await self.aio_save(*args, **kwargs)

	async def destroy(self, recursive=False, delete_nullable=False):
		return await self.aio_delete_instance(recursive=recursive, delete_nullable=delete_nullable)

	async def get_related(self, related_name, single_backref=False):
		return await self.objects.get_related(self, related_name, single_backref)

	class Meta:
		database = Proxy


class TimedModel(Model):
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

	async def save(self, *args, **kwargs):
		self.updated_at = datetime.datetime.now()
		return await super().save(*args, **kwargs)

	@classmethod
	async def create(cls, **insert):
		insert['updated_at'] = datetime.datetime.now()
		return await super().create(**insert)
