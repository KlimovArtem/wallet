import pytest
from httpx import AsyncClient, ASGITransport

from src.app.main import app
from src.app.db_adapters import postgres as db_adapter
from src.app.db_adapters import migrate


@pytest.fixture()
async def setup_database():
    await db_adapter.database.connect()
    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute("CREATE TABLE IF NOT EXISTS test;")
    await migrate.apply_pending_migrations()

    yield

    async with db_adapter.database.pool.acquire() as connection:
        await connection.execute("DROP SCHEMA IF EXISTS test CASCADE;")
    await db_adapter.database.disconnect()


@pytest.fixture
async def client_app():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
