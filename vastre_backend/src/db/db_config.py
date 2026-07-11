from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
engine = create_async_engine(DB_URL,echo=True)

sessionLocal = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with sessionLocal.begin() as session:
        yield session