from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.inbound import main_router
from src.adapters.outbound import init_db, db_dispose


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await db_dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)
