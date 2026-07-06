import pytest

import src.infrastructure.web.mappers.user_dtos_mapper as mapper
from src.domain.user import User
from src.infrastructure.web.dtos import UserRequest, UserPatchRequest


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
