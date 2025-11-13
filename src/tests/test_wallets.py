import uuid

import pytest

from app.db_adapters import postgres as db_adapter


@pytest.mark.asyncio
async def test_create_wallet(setup_database, client_app):
    query = "SELECT COUNT(*) FROM wallets;"
    before, after = None, None
    async with db_adapter.database.pool.acquire() as connection:
        before = await connection.execute(query)
    response = await client_app.post("/api/v1/wallets")
    async with db_adapter.database.pool.acquire() as connection:
        after = await connection.execute(query)
    assert response.status_code == 201, f"Неверный статус ответа ожидается 201, вернулся {response.status_code}"
    assert after > before, "Ошибка создания нового объекта. Новых объектов не создано."

@pytest.mark.asyncio
async def test_show_wallet_balance(setup_database, client_app):
    query = "INSERT INTO wallets(id, balance) VALUES($1, 0);"
    wallet_id = uuid.uuid4()
    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute(query, wallet_id)
    response = await client_app.post("/api/v1/wallets/test-id")
    assert response.status_code == 200, f"Неверный статус ответа ожидается 200, вернулся {response.status_code}"
    assert response.json()["id"] == wallet_id, "Ошибка при запросе объекта."

@pytest.mark.asyncio
async def test_update_wallet_balance(setup_database, client_app):
    wallet_id = uuid.uuid4()
    create_query = "INSERT INTO wallets(id, balance) VALUES($1, 0);"
    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute(create_query, wallet_id)

    before, after = None, None
    payload = {"operation_type": "DEPOSIT", "amount": 2000}
    select_query = f"SELECT * FROM wallets WHERE id={wallet_id};"
    async with db_adapter.database.pool.acquire() as connection:
         row = await connection.fetch(select_query)
         before = row["balance"]
    response = await client_app.post(f"/api/v1/wallets/{wallet_id}/operation", data=payload)
    async with db_adapter.database.pool.acquire() as connection:
         row = await connection.fetch(select_query)
         after = row["balance"]
    assert response.status_code == 200, f"Неверный статус ответа ожидается 200, вернулся {response.status_code}"
    assert after == before + payload["amount"], "Ошибка обновления объекта."

@pytest.mark.asyncio
async def test_cros_update_wallet_balance(setup_database, client_app):
    wallet_id = uuid.uuid4()
    create_query = "INSERT INTO wallets(id, balance) VALUES($1, 0);"
    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute(create_query, wallet_id)

    before, after = None, None
    deposit_payload = {"operation_type": "DEPOSIT", "amount": 2000}
    withdraw_payload = {"operation_type": "WITHDRAW", "amount": 2000}
    select_query = f"SELECT * FROM wallets WHERE id={wallet_id};"
    async with db_adapter.database.pool.acquire() as connection:
         row = await connection.fetch(select_query)
         before = row["balance"]
    deposit_response = await client_app.post(f"/api/v1/wallets/{wallet_id}/operation", data=deposit_payload)
    withdraw_response = await client_app.post(f"/api/v1/wallets/{wallet_id}/operation", data=withdraw_payload)
    deposit_response = await client_app.post(f"/api/v1/wallets/{wallet_id}/operation", data=deposit_payload)
    async with db_adapter.database.pool.acquire() as connection:
        row = await connection.fetch(select_query)
        after = row["balance"]
    assert (deposit_response, withdraw_response) == (200, 200), f"Неверный статус ответа."
    assert after == 2000, "Ошибкаа перекрестного обновления, транзакция не блокируетсяю"
