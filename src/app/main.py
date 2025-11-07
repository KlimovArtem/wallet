from fastapi import FastAPI

from app.api import wallets


app = FastAPI()

app.include_router(wallets.v1_router)
