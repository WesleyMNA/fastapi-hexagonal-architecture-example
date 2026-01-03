import pytest

import src.adapters.inbound.mappers.user_dtos_mapper as mapper
from src.adapters.inbound.dtos import UserRequest, UserPatchRequest
from src.domain import User


@pytest.mark.anyio
@pytest.mark.parametrize(
    'dto, mapper_func',
    [
        (UserRequest(name='User', email='user@email.com'), mapper._get_user_request),
        (UserPatchRequest(name='Patched'), mapper._get_user_patch_request),
        (UserPatchRequest(email='patched@email.com'), mapper._get_user_patch_request),
    ],
)
async def test_mapper_functions(dto, mapper_func):
    user = await mapper_func(dto)

    assert isinstance(user, User)

    for key, value in dto.model_dump().items():
        assert getattr(user, key) == value
