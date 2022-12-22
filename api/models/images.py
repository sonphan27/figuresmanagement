from utils.db import EnumField
from . import PeeweeBaseModel
import peewee as p
from playhouse.postgres_ext import BinaryJSONField


class ParentTable(EnumField):
    PRODUCTS = "products"
    COMPANIES = "companies"
    SERIES = "series"
    BRANDS = "brands"


class Images(PeeweeBaseModel):
    id = p.BigAutoField()
    parent_id = p.IntegerField()
    parent_table = p.TextField()
    url = p.TextField()
    metadata = BinaryJSONField()
