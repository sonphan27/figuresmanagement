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
    status: str
    shipping_status: str
    bought_from: str = None
    metadata: dict = None


class GetProduct(PostProduct):
    id: int


@router.get("/products/{product_id}", response_model=GetProduct, tags=["Products"])
def get_product(product_id: int):
    product = Products.get_by_id(product_id)
    return model_to_dict(product)


@router.post("/products", tags=["Products"])
def post_product(payload_: PostProduct):
    payload = payload_.dict()
    print(payload)
    return
