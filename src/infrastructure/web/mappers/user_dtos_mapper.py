from typing import Annotated

from fastapi import Depends

from src.domain.user.user_model import User
from src.infrastructure.web.dtos import UserRequest, UserPatchRequest


async def _get_user_request(r: UserRequest) -> User:
    return User(**r.model_dump())


UserRequestDep = Annotated[User, Depends(_get_user_request)]


async def _get_user_patch_request(r: UserPatchRequest) -> User:
    return User(**r.model_dump())


UserPatchDep = Annotated[User, Depends(_get_user_patch_request)]
