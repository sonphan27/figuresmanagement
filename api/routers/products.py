from fastapi import APIRouter
from models.users import Users
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict


router = APIRouter()


class PostProduct(BaseModel):
  name: str


class GetProduct(PostProduct):
  id: int


@router.get("/products/{product_id}", response_model=GetProduct, tags=["Products"])
def get_product(product_id: int):
  print(product_id)
  return {"name": "dummy", "id": "1"}


@router.post("/products", tags=["Products"])
def post_product(payload_: PostProduct):
  payload = payload_.dict()
  print(payload)
  return
