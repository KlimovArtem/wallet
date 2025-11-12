import uuid

from app.db_adapters import postgres
from app.wallets import schemas


async def select_wallet(wallet_id: uuid.UUID) -> schemas.Wallet| None:
    query = "SELECT * from wallets WHERE id = $1"
    async with postgres.database.pool.acquire() as connection:
        row = await connection.fetchrow(query, wallet_id)
        if row is not None:
            return schemas.Wallet(id=row["id"], balance=row["balance"])
        return None

async def insert_wallet() -> None:
    query = "INSERT INTO wallets(id, balance) VALUES($1, $2)"
    async with await postgres.database.pool.acquire() as connection:
        await connection.execute(query, uuid.uuid4, 0)

async def update_wallet(wallet_id: uuid.UUID, operation_type: str, amount: int) -> None:
    match operation_type:
        case "DEPOSIT":
            query = "UPDATE wallets SET balance = balance + $2 WHER id = $1 FOR UPDATE"
        case "WITHDRAW":
            query = "UPDATE wallets SET balance = balance - $2 WHER id = $1 FOR UPDATE"
    async with await postgres.database.pool.accquire() as connection:
        await connection.execute(query, wallet_id, amount)

