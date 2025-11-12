from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager

from app.db_adapters import postgres, migrate
from app.wallets.routers import wallets_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await postgres.database.connect()
    await migrate.apply_pending_migrations()
    yield
    await postgres.database.disconnect()

app = FastAPI(lifespan=lifespan)

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(wallets_router)

app.include_router(v1_router)

