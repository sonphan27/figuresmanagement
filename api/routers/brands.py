from fastapi import APIRouter
from models.brands import Brands
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict


router = APIRouter()


class PostBrand(BaseModel):
    name: str
    company_id: int = None
    country_id: str = None
    prefix_code: str = None


class GetBrand(PostBrand):
    id: int
    metadata: dict = None


@router.get("/brands/{brand_id}", response_model=GetBrand, tags=["Brands"])
def get_brand(brand_id: int):
    brand = Brands.get_by_id(brand_id)
    return model_to_dict(brand)


@router.post("/brands", tags=["Brands"])
def post_brand(payload_: PostBrand):
    payload = payload_.dict()
    return Brands.create(**payload)
