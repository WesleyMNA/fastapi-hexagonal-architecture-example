from datetime import datetime

from fastapi import Request
from starlette.responses import JSONResponse

from src.application import ApplicationException, NotFound, Conflict

EXCEPTION_STATUS_MAP: dict[type[ApplicationException], int] = {
    NotFound: 404,
    Conflict: 409,
}


async def handle_application_exception(
        request: Request,
        exc: ApplicationException,
):
    status_code = EXCEPTION_STATUS_MAP.get(type(exc), 500)
    return JSONResponse(
        status_code=status_code,
        content={
            'title': exc.__class__.__name__,
            'detail': exc.detail or 'Internal Server Error',
            'status': status_code,
            'path': request.url.path,
            'timestamp': datetime.now().isoformat(),
        },
    )
