from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from models.series import Series


router = APIRouter()


class SeriesCommon(BaseModel):
    name: str
    type: str = None
    country_id: str = None


class GetSeries(SeriesCommon):
    id: int
    metadata: dict = None
    country: str


class PatchSeries(BaseModel):
    name: str = None
    code: str = None
    type: str = None
    country_id: str = None


@router.get("/series/{series_id}", response_model=GetSeries, tags=["Series"])
def get_company(series_id: int):
    series = Series.get_details(series_id, single=True)
    return series


@router.get("/series", response_model=List[GetSeries], tags=["Series"])
def get_companies():
    return Series.get_details()


@router.post("/series", tags=["Series"])
def post_company(payload_: SeriesCommon):
    payload = payload_.dict()
    return Series.create(**payload)


@router.patch("/series/{series_id}", tags=["Series"])
def patch_company(series_id: int, payload_: PatchSeries):
    payload = payload_.dict(exclude_unset=True)
    return Series.update(**payload).where(Series.id == series_id).execute()
