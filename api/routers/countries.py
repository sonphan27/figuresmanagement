from typing import List

from fastapi import APIRouter
from models.countries import Countries, ContinentTypeEnum
from pydantic import BaseModel

router = APIRouter()


class GetCountry(BaseModel):
    id: str
    name: str
    continent: ContinentTypeEnum.EnumClass


@router.get("/countries", response_model=List[GetCountry], tags=["Countries"])
def get_coutries():
    countries = Countries.select().dicts()
    return [country for country in countries]
