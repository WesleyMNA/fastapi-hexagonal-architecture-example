from typing import Annotated

from fastapi.params import Depends

from src.domain.user import (
    UserRepositoryProtocol,
    UserService,
    UserServiceProtocol,
    UserValidator,
    UserValidatorProtocol,
)
from src.infrastructure.persistence import UserSqlAlchemyRepository
from src.infrastructure.web.routers.config.email_dependency_config import EmailCryptoDep

UserRepositoryDep = Annotated[UserRepositoryProtocol, Depends(UserSqlAlchemyRepository)]


async def get_user_validator(r: UserRepositoryDep) -> UserValidatorProtocol:
    return UserValidator(r)


UserValidatorDep = Annotated[UserValidatorProtocol, Depends(get_user_validator)]


async def get_user_service(
        r: UserRepositoryDep,
        v: UserValidatorDep,
        c: EmailCryptoDep,
) -> UserServiceProtocol:
    return UserService(r, v, c)


UserServiceDep = Annotated[UserServiceProtocol, Depends(get_user_service)]
