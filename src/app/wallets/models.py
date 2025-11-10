import os
import uuid

from dotenv import load_dotenv
from databases import Database
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        MetaData,
                        Table)

from sqlalchemy.dialects.postgresql import UUID


load_dotenv()

engine = create_engine(os.getenv("DB_URL"))
database = Database(os.getenv("DB_URL", ""))
metadata = MetaData()

wallets = Table(
    "wallets",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True),
    Column("balance", Integer, default=0)
)
