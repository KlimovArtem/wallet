from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api import routers
from app.wallets import models


models.metadata.create_all(models.engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await models.database.connect()
    yield
    await models.database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(routers.v1_router)