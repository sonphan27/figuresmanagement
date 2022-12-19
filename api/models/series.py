from utils.db import f, e
from . import PeeweeBaseModel
import peewee as p
from playhouse.postgres_ext import BinaryJSONField

from .countries import Countries


class Series(PeeweeBaseModel):
    id = p.BigAutoField()
    name = p.TextField()
    type = p.TextField()
    country_id = p.TextField()
    metadata = BinaryJSONField()

    @classmethod
    def get_details(cls, series_id: int = None, single=False):
        query = Series.select()
        # get country
        query = query.select_extend(Countries.name.alias("country"))
        query = query.join(
            Countries,
            p.JOIN.INNER,
            on=Countries.id == Series.country_id
        )
        if series_id:
            query = query.where(Series.id == series_id)
        if single:
            return f(query)
        return e(query)
