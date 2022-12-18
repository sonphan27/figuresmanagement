from typing import List

from fastapi import APIRouter
from models.products import Products
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict


router = APIRouter()


class PostProduct(BaseModel):
    name: str
    code: str = None
    brand_id: int = None
    series_id: int = None
    bought_price: float = None
    sold_price: float = None
    status: str = "new"
    shipping_status: str = "shipped"
    bought_from: str = None


class GetProduct(PostProduct):
    id: int
    metadata: dict = None


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


@router.get("/products/{product_id}", response_model=GetProduct, tags=["Products"])
def get_product(product_id: int):
    product = Products.get_by_id(product_id)
    return model_to_dict(product)


@router.get("/products", response_model=List[GetProduct], tags=["Products"])
def get_products():
    products = Products.select().dicts()
    return products


@router.post("/products", tags=["Products"])
def post_product(payload_: PostProduct):
    payload = payload_.dict()
    return Products.create(**payload)


@router.patch("/products/{product_id}", tags=["Products"])
def patch_product(product_id: int, payload_: PatchProduct):
    payload = payload_.dict(exclude_unset=True)
    return Products.update(**payload).where(Products.id == product_id).execute()
