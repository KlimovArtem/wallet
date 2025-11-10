from fastapi import APIRouter


v1_router = APIRouter(
    prefix="/api/v1"
)


@v1_router.post("/wallets/{wallet_id}/operation")
async def wallet_balance(wallet_id: int):
   # match operation.operation_type:
   #     case "DEPOSIT":
   #         #wallet = get_wallet_by_id(id=operation.wallet_id)
   #         #wallet.balacne = wallet.balace + operation.amount
   #         pass
   #     case "WITHDRAW":
   #          pass
   #
    return { "id": wallet_id, "balance":  0}


@v1_router.get("/wallets/{wallet_id}")
async def wallet_balance(wallet_id: int):
    # wallet = Wallet.objects.filter(id=wallet_id)[0]
    return {"id": wallet_id, "balance":  0}

