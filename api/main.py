from fastapi import FastAPI
from routers import users, products, countries, brands

router = FastAPI()


for module in (products, brands, countries, users):
    router.include_router(
        module.router,
        prefix="/api",
    )
