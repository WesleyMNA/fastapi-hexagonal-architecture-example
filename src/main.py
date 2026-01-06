from contextlib import asynccontextmanager

import uvicorn
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


def _create_app() -> FastAPI:
    result = FastAPI(
        title='FastAPI Hexagonal Architecture Example',
        version='1.0.0',
        lifespan=lifespan,
    )
    result.include_router(main_router)
    result.add_exception_handler(
        ApplicationException,
        handle_application_exception,
    )

    return result


app = _create_app()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=False,
    )
