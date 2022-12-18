from . import PeeweeBaseModel
import peewee as p
from playhouse.postgres_ext import BinaryJSONField


class Brands(PeeweeBaseModel):
    id = p.BigAutoField()
    name = p.TextField()
    company_id = p.BigIntegerField()
    country_id = p.TextField()
    prefix_code = p.TextField()
    metadata = BinaryJSONField()
