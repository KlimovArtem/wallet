from uuid import UUID

from fastapi import APIRouter

from app.wallets import db_queries
from app.wallets.schemas import OperationWithWallet


wallets_router = APIRouter(prefix="/wallets", tags=["wallets"])

@wallets_router.get("/{wallet_id}")
async def get_wallet_balance(wallet_id: UUID):
    return await db_queries.select_wallet(wallet_id)

@wallets_router.get("/")
async def get_all_wallet():
    return await db_queries.select_all_wallets()


@wallets_router.post("/{wallets_id/operation}", status_code=204)
async def change_wallet_balance(wallet_id: UUID, payload: OperationWithWallet):
    await db_queries.update_wallet(wallet_id, payload.operation_type, payload.amount)


@wallets_router.post("/", status_code=201)
async def create_wallet():
    await db_queries.insert_wallet()
