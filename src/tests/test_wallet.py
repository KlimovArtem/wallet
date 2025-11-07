from starlette.testclient import TestClient

from app.main import app


client = TestClient(app)

def tests_wallet_balance():
    WALLET_ID = 1
    response = client.get(f"api/v1/wallets/{WALLET_ID}")
    assert response.status_code == 200
    assert response.json() == {"id": WALLET_ID, "balance": 0}
