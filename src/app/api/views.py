import uuid

from app.api import schemes
from app.api import routers
from app.wallets import models


async def post():
    query = models.wallets.insert()
    return await models.database.execute(query=query)


@routers.wallets_router.post("/", status_code=201)
async def create_wallet():
    new_wallet_id = await post()
    return { "id": new_wallet_id, "balance":  0}

@routers.wallets_router.get("/{wallet_id}")
async def wallet_balance(wallet_id: int):
    # wallet = Wallet.objects.filter(id=wallet_id)[0]
    return {"id": wallet_id, "balance":  0}

@routers.wallets_router.post("/{wallet_id}/operation")
async def change_wallet_balance(wallet_id: int, payload: schemes.OperationWithWalletSchema):
    match payload.operation_type:
        # пополнение
        case "DEPOSIT":
            #wallet = get_wallet_by_id(id=operation.wallet_id)
            #wallet.balacne = wallet.balace + operation.amount
            pass
        # снятие
        case "WITHDRAW":
             pass

    return { "id": wallet_id, "balance":  0}
