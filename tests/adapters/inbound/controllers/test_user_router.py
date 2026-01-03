from unittest.mock import AsyncMock

import pytest

from src.adapters.inbound.dtos import UserRequest, UserPatchRequest
from src.config.user_dependency_config import get_user_service
from src.domain import User
from src.main import app

_REQ_EXAMPLE = {
    'name': 'John',
    'email': 'john@example.com',
}


@pytest.mark.anyio
class TestUserRouter:

    @pytest.fixture(autouse=True)
    async def _setup(self, create_client):
        self.mock_service = AsyncMock()
        app.dependency_overrides[get_user_service] = lambda: self.mock_service
        self.client = create_client

    async def test_find_all(self):
        self.mock_service.find_all.return_value = [
            User(id=1, **_REQ_EXAMPLE),
            User(id=2, name='Jane', email='jane@example.com'),
        ]

        res = await self.client.get('/users')

        assert res.status_code == 200
        assert len(res.json()) == 2

    async def test_find_by_id(self):
        self.mock_service.find_by_id.return_value = User(id=1, **_REQ_EXAMPLE)

        res = await self.client.get('/users/1')

        assert res.status_code == 200
        assert res.json().get('id') == 1

    async def test_create(self):
        self.mock_service.create.return_value = User(id=1, **_REQ_EXAMPLE)

        req = UserRequest(**_REQ_EXAMPLE)
        res = await self.client.post('/users', json=req.model_dump())

        assert res.status_code == 201
        assert res.json().get('id') == 1

    async def test_update(self):
        req = UserRequest(**_REQ_EXAMPLE)
        res = await self.client.put('/users/1', json=req.model_dump())

        assert res.status_code == 204

    async def test_patch(self):
        req = UserPatchRequest(**_REQ_EXAMPLE)
        res = await self.client.patch('/users/1', json=req.model_dump())

        assert res.status_code == 204

    async def test_delete(self):
        res = await self.client.delete('/users/1')

        assert res.status_code == 204
