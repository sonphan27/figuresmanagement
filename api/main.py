from fastapi import FastAPI
from routers import users, products, countries, brands, companies

router = FastAPI()


for module in (products, brands, companies, countries, users):
    router.include_router(
        module.router,
        prefix="/api",
    )
