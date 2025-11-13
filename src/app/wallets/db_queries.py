import uuid

from app.db_adapters import postgres as db_adapter
from app.wallets import schemas
from app.app_logger import logger

async def select_wallet(wallet_id: uuid.UUID) -> schemas.Wallet| None:
    query = "SELECT * from wallets WHERE id = $1"
    async with db_adapter.database.pool.acquire() as connection:
        row = await connection.fetchrow(query, wallet_id)
        if row is not None:
            wallet = schemas.Wallet(id=row["id"], balance=row["balance"])
            return wallet
        return None

async def select_all_wallets() -> list[schemas.Wallet] | None:
    query = "SELECT * from wallets"
    async with db_adapter.database.pool.acquire() as connection:
        rows = await connection.fetch(query)
        if rows is not None:
            wallets = [schemas.Wallet(id=row["id"], balance=row["balance"]) for row in rows]
            return wallets
        return None

async def insert_wallet() -> None:
    query = "INSERT INTO wallets(id, balance) VALUES($1, $2)"
    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute(query, uuid.uuid4(), 0)

async def update_wallet(wallet_id: uuid.UUID, operation_type: str, amount: int) -> None:
    match operation_type:
        case "DEPOSIT":
            update_query = "UPDATE wallets SET balance = balance + $2 WHERE id = $1;"
        case "WITHDRAW":
            update_query = "UPDATE wallets SET balance = balance - $2 WHERE id = $1;"
        case _:
            update_query = ""
    blocking_query = "SELECT * FROM wallets WHERE id=$1 FOR UPDATE;"
    async with db_adapter.database.pool.acquire() as connection:
        async with connection.transaction():
            await connection.execute(blocking_query, wallet_id)
            await connection.execute(update_query, wallet_id, amount)
