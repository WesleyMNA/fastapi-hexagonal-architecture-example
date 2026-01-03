from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.inbound import main_router
from src.adapters.outbound import init_db, db_dispose
from src.application import ApplicationException
from src.config import handle_application_exception


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await db_dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)
app.add_exception_handler(ApplicationException, handle_application_exception)
