from peewee import BooleanField
from playhouse.migrate import migrate, SchemaMigrator

from ..models.mapfolder import MapFolder


def upgrade(migrator: SchemaMigrator):
	try:
		query = MapFolder.raw("""SELECT * FROM mapfolder WHERE public = True""")
		public_folders = query.execute()

		migrate(
			migrator.add_column(MapFolder._meta.table_name, 'visibility', MapFolder.visibility),
			migrator.drop_column(MapFolder._meta.table_name, 'public')
		)

		MapFolder.update(visibility='public').where(MapFolder.id << [f.id for f in public_folders]).execute()
	except Exception as e:
		print(str(e))
		print('Migration failed but silencing error!')

def downgrade(migrator: SchemaMigrator):
	try:
		query = MapFolder.raw("""SELECT * FROM mapfolder WHERE visibility = 'public'""")
		public_folders = query.execute()

		migrate(
			migrator.add_column(MapFolder._meta.table_name, 'public', BooleanField()),
			migrator.drop_column(MapFolder._meta.table_name, 'visibility')
		)

		MapFolder.update(public=True).where(MapFolder.id << [f.id for f in public_folders]).execute()
	except Exception as e:
		print(str(e))
		print('Migration failed but silencing error!')
