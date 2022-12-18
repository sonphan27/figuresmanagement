from fastapi import APIRouter
from models.users import Users
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict


router = APIRouter()


class PostUser(BaseModel):
    name: str
    password: str


class GetUser(PostUser):
    id: int
    active: bool


@router.get("/users/{user_id}", response_model=GetUser, tags=["Users"])
def read_user(user_id: int):
    user = Users.get_by_id(user_id)
    return model_to_dict(user)


@router.post("/users", tags=["Users"])
def post_user(payload_: PostUser):
    payload = payload_.dict()
    user = Users.create_(payload)
    return user
