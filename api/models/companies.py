from utils.db import f, e
from . import PeeweeBaseModel
import peewee as p
from playhouse.postgres_ext import BinaryJSONField

from .countries import Countries


class Companies(PeeweeBaseModel):
    id = p.BigAutoField()
    code = p.TextField()
    name = p.TextField()
    country_id = p.TextField()
    metadata = BinaryJSONField()

    @classmethod
    def get_details(cls, company_id: int = None, single=False):
        query = Companies.select()
        # get country
        query = query.select_extend(Countries.name.alias("country"))
        query = query.join(
            Countries,
            p.JOIN.INNER,
            on=Countries.id == Companies.country_id
        )
        if company_id:
            query = query.where(Companies.id == company_id)
        if single:
            return f(query)
        return e(query)
