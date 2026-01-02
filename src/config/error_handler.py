from urllib.request import Request

from starlette.responses import JSONResponse

from src.application import RestException


async def handle_rest_exception(request: Request, exc: RestException):
    c = exc.content
    c['path'] = request.url.path
    return JSONResponse(status_code=exc.status_code, content=c)
