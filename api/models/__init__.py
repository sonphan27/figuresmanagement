from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import Model
from contextvars import ContextVar

db_context_var: ContextVar[PostgresqlExtDatabase] = ContextVar("db")


def create_db():
  """Create db connection"""
  return PostgresqlExtDatabase(
      'fastapi_project',
      user='postgres',
      password='postgres',
      host='db',
      port=5432,
      autorollback=True,
  )


def _get_db():
    if db_context_var.get(None) is None:
        db_context_var.set(create_db())
    return db_context_var.get()


class _DBProxy:
    def __getattr__(self, item):
        return getattr(_get_db(), item)

    def __setattr__(self, key, value):
        return setattr(_get_db(), key, value)


db = _DBProxy()


class PeeweeBaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
        schema = 'public'
        legacy_table_names = False 
