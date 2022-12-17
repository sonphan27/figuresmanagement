from typing import Optional

from fastapi import FastAPI

router = FastAPI()

from models.users import Users
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict



class PostUser(BaseModel):
  name: str


class GetUser(PostUser):
  id: int
  active: bool


@router.get("/users/{user_id}", response_model=GetUser)
def read_user(user_id: int):
  user = Users.get_by_id(user_id)

  return model_to_dict(user)


@router.post("/users")
def post_user(payload_: PostUser):
  payload = payload_.dict()
  user = Users.create(**payload)
  return user
