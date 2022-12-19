from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from models.companies import Companies


router = APIRouter()


class CompanyCommon(BaseModel):
    name: str
    code: str = None
    country_id: str = None


class GetCompany(CompanyCommon):
    id: int
    metadata: dict = None
    country: str


class PatchCompany(BaseModel):
    name: str = None
    code: str = None
    country_id: str = None


@router.get("/companies/{company_id}", response_model=GetCompany, tags=["Companies"])
def get_company(company_id: int):
    company = Companies.get_details(company_id, single=True)
    return company


@router.get("/companies", response_model=List[GetCompany], tags=["Companies"])
def get_companies():
    return Companies.get_details()


@router.post("/companies", tags=["Companies"])
def post_company(payload_: CompanyCommon):
    payload = payload_.dict()
    return Companies.create(**payload)


@router.patch("/companies/{company_id}", tags=["Companies"])
def patch_company(company_id: int, payload_: PatchCompany):
    payload = payload_.dict(exclude_unset=True)
    return Companies.update(**payload).where(Companies.id == company_id).execute()
