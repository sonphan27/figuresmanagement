from fastapi import FastAPI
from routers import users, products


router = FastAPI()


for module in (users, products):
    router.include_router(
        module.router,
        prefix="/api",
    )
