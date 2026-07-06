from typing import AsyncGenerator, Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase


class DbSettings(BaseSettings):
    db_host: str = 'localhost'
    db_port: int = 5432
    db_name: str = 'hexagonal'
    db_user: str = 'postgres'
    db_password: str = 'root'

    show_sql: bool = False


_env = DbSettings()
_db_url = f'postgresql+asyncpg://{_env.db_user}:{_env.db_password}@{_env.db_host}:{_env.db_port}/{_env.db_name}'
_engine = create_async_engine(
    _db_url,
    echo=_env.show_sql,
    future=True,
    pool_pre_ping=True,
)
_AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=_engine)


class Base(DeclarativeBase):
    pass


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    async with _AsyncSessionLocal() as db:
        yield db


AsyncSessionDep = Annotated[AsyncSession, Depends(get_db_session)]


async def init_db():
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def db_dispose():
    await _engine.dispose()
