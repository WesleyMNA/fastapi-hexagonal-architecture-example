import json

import pytest
from fastapi import Request
from starlette.responses import JSONResponse

from src.application import NotFound, Conflict, ApplicationException
from src.config import handle_application_exception


def _make_request(path: str = '/test'):
    scope = {
        'type': 'http',
        'method': 'GET',
        'path': path,
        'headers': [],
        'query_string': b'',
        'client': ('testclient', 50000),
        'server': ('testserver', 80),
        'scheme': 'http',
    }
    return Request(scope)


@pytest.mark.anyio
async def test_handle_not_found_exception():
    request = _make_request('/users/1')
    exc = NotFound(detail='User not found')

    response: JSONResponse = await handle_application_exception(request, exc)
    content = json.loads(response.body)

    assert response.status_code == 404
    assert content['title'] == 'NotFound'
    assert content['detail'] == 'User not found'
    assert content['status'] == 404
    assert content['path'] == '/users/1'
    assert 'timestamp' in content


@pytest.mark.anyio
async def test_handle_conflict_exception():
    request = _make_request('/users')
    exc = Conflict(detail='Email already exists')

    response = await handle_application_exception(request, exc)
    content = json.loads(response.body)

    assert response.status_code == 409
    assert content['title'] == 'Conflict'
    assert content['detail'] == 'Email already exists'
    assert content['status'] == 409
    assert 'timestamp' in content


class UnknownError(ApplicationException):
    def __init__(self):
        self._detail = None


@pytest.mark.anyio
async def test_handle_unmapped_exception_returns_500():
    request = _make_request('/unknown')
    exc = UnknownError()

    response = await handle_application_exception(request, exc)
    content = json.loads(response.body)

    assert response.status_code == 500
    assert content['title'] == 'UnknownError'
    assert content['detail'] == 'Internal Server Error'
    assert content['status'] == 500
    assert 'timestamp' in content
