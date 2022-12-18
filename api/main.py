from fastapi import FastAPI
from routers import users, products, countries, brands

router = FastAPI()


for module in (users, products, countries, brands):
    router.include_router(
        module.router,
        prefix="/api",
    )
