from . import PeeweeBaseModel
import peewee as p
from enum import Enum
from playhouse.postgres_ext import BinaryJSONField
from .brands import Brands
from utils.db import EnumField, f, e
from .companies import Companies
from .countries import Countries
from .images import Images
from .series import Series


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

    @classmethod
    def get_details(cls, product_id: int = None, single=False):
        query = Products.select(
            Products.id,
            Products.name,
            Products.code,
            Products.bought_price,
            Products.sold_price,
            Products.bought_from,
            Products.status,
            Products.shipping_status,
            Products.metadata,
        )
        # get brand and company and country
        query = query.select_extend(
            Brands.name.alias("brand_name"),
            Companies.name.alias("company"),
            Companies.country_id.alias("country_code"),
            Countries.name.alias("country"),
        )
        query = (
            query.join(Brands, p.JOIN.LEFT_OUTER, on=Brands.id == Products.brand_id)
            .join(Companies, p.JOIN.LEFT_OUTER, on=Companies.id == Brands.company_id)
            .join(Countries, p.JOIN.LEFT_OUTER, on=Countries.id == Companies.country_id)
        )
        # get series
        query = query.select_extend(
            Series.name.alias("series"), Series.type.alias("category")
        )
        query = query.join(
            Series, p.JOIN.LEFT_OUTER, on=Series.id == Products.series_id
        )
        # get images
        query = query.select_extend(
            p.fn.array(
                Images.select(Images.url).where(
                    (Images.parent_id == Products.id)
                    & (Images.parent_table == "products")
                )
            ).alias("images")
        )
        if product_id:
            query = query.where(Products.id == product_id)
        if single:
            return f(query)
        return e(query)
