import uuid

import pytest

from src.app.db_adapters import postgres


@pytest.mark.asyncio
async def test_create_wallet(setup_database, client_app):
    query = "SELECT COUNT(*) FROM wallets;"
    before, after = None, None
    async with postgres.database.pool.acquire() as connection:
        before = await connection.execute(query)
    response = await client_app.post("/api/v1/wallets")
    async with postgres.database.pool.aquries() as connection:
        after = await connection.execute(query)
    assert response.status_code == 201
    assert after > before, "Ошибка создания нового объекта. Новых объектов не создано."

@pytest.mark.asyncio
async def test_show_wallet_balance(setup_database, client_app):
    query = "INSERT INTO wallets(id, balance) VALUES($1, 0);"
    wallet_id = uuid.uuid4()
    async with postgres.database.pool.acquire() as connection:
        await connection.execute(query, wallet_id)
    response = await client_app.post("/api/v1/wallets/test-id")
    assert response.status_code == 200
    assert response.json()["id"] == wallet_id, "Ошибка при запросе объекта."

