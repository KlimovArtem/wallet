from fastapi import APIRouter


v1_router = APIRouter(
    prefix="/api/v1"
)

wallets_router = APIRouter(
    prefix="/wallets",
    tags=["wallets"]
)

v1_router.include_router(wallets_router)