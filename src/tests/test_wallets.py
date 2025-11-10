import uuid

from starlette.testclient import TestClient

from app.main import app


client = TestClient(app)

def tests_wallet_balance():
    WALLET_ID = str(uuid.uuid4)
    response = client.get(f"api/v1/wallets/{WALLET_ID}")
    assert response.status_code == 200
    assert response.json() == {"id": WALLET_ID, "balance": 0}

def test_create_wallet(test_app, monkeypatch):
    response = test_app.post("/wallets/")

    assert response.status_code == 201

    response_data = response.json()
    assert "id" in response_data
    assert "balance" in response_data
    assert isinstance(uuid.UUID, response_data.get("id"))
    assert response_data.get("balance") == 0