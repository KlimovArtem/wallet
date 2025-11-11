from fastapi import APIRouter


v1_wallets_router = APIRouter(
    prefix="/api/v1/wallets",
    tags=["wallets"]
)
