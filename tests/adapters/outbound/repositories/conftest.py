import pytest
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)
from testcontainers.postgres import PostgresContainer

from src.adapters.outbound import Base


@pytest.fixture(scope='module')
async def get_db_session():
    with PostgresContainer('postgres:16', driver=None) as postgres:
        engine = create_async_engine(postgres.get_connection_url(driver='asyncpg'))
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
        async with session() as db:
            yield db
        await engine.dispose()
