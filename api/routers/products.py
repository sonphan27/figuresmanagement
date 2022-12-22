from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from models.images import Images
from models.products import Products


router = APIRouter()


class ProductCommon(BaseModel):
    name: str
    code: str = None
    bought_price: float = None
    sold_price: float = None
    status: str = "new"
    shipping_status: str = "shipped"
    bought_from: str = None
    images: List[str] = []


class PostProduct(ProductCommon):
    brand_id: int = None
    series_id: int = None


class GetProduct(ProductCommon):
    id: int
    metadata: dict = None
    brand_name: str
    series: str
    category: str
    company: str
    country_code: str
    country: str


class PatchProduct(BaseModel):
    name: str = None
    code: str = None
    brand_id: int = None
    series_id: int = None
    bought_price: float = None
    sold_price: float = None
    status: str = None
    shipping_status: str = None
    bought_from: str = None
    images: List[str] = []


@router.get("/products/{product_id}", response_model=GetProduct, tags=["Products"])
def get_product(product_id: int):
    product = Products.get_details(product_id, single=True)
    return product


@router.get("/products", response_model=List[GetProduct], tags=["Products"])
def get_products():
    return Products.get_details()


@router.post("/products", tags=["Products"])
def post_product(payload_: PostProduct):
    payload = payload_.dict()
    images = payload.pop("images", None)
    result = Products.create(**payload)
    if images:
        image_payload = {
            "parent_id": result,
            "parent_table": "products",
        }
        for url in images:
            Images.create(url=url, **image_payload)
    return


@router.patch("/products/{product_id}", tags=["Products"])
def patch_product(product_id: int, payload_: PatchProduct):
    payload = payload_.dict(exclude_unset=True)
    if images := payload.pop("images", None):
        image_payload = {
            "parent_id": product_id,
            "parent_table": "products",
        }
        for url in images:
            Images.create(url=url, **image_payload)
    if not payload:
        return
    return Products.update(**payload).where(Products.id == product_id).execute()
