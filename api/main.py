from fastapi import FastAPI
from routers import users, products, countries, brands, companies, series

router = FastAPI()


for module in (products, series, brands, companies, countries, users):
    router.include_router(
        module.router,
        prefix="/api",
    )
