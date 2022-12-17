from . import PeeweeBaseModel
import peewee as p
from enum import Enum
from utils.db import EnumField
from playhouse.postgres_ext import BinaryJSONField


class ProductStatusEnum(EnumField):
    class EnumClass(str, Enum):
        NEW = "new"
        SECOND = "2nd"
        SECOND_NO_BOX = "2nd (no box)"

    field_type = "e_status"


class ProductShippingStatusEnum(EnumField):
    class EnumClass(str, Enum):
        WISHED = "wished"
        PRE_ORDERED = "pre-ordered"
        ORDERED = "ordered"
        SHIPPING = "shipping"
        SHIPPED = "shipped"
        SOLD = "sold"

    field_type = "e_shipping_status"


class Products(PeeweeBaseModel):
    id = p.BigAutoField()
    name = p.TextField()
    code = p.TextField()
    brand_id = p.BigIntegerField()
    series_id = p.BigIntegerField()
    bought_price = p.DoubleField()
    sold_price = p.DoubleField()
    status = ProductStatusEnum()
    shipping_status = ProductShippingStatusEnum()
    bought_from = p.TextField()
    metadata = BinaryJSONField()
