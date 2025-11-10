import uuid

from pydantic import BaseModel

class Wallet(BaseModel):
    id: uuid.UUID
    balance: int


class OperationWithWalletSchema(BaseModel):
    operation_type: str
    amount: int
