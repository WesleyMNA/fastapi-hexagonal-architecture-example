from fastapi.params import Depends

from src.adapters.outbound import UserSqlAlchemyRepository
from src.application import UserServiceImpl, UserValidatorImpl
from src.ports.inbound import UserService, UserValidator
from src.ports.outbound import UserRepository


async def create_user_validator(r: UserRepository = Depends(UserSqlAlchemyRepository)) -> UserValidator:
    return UserValidatorImpl(r)


async def create_user_service(
        r: UserRepository = Depends(UserSqlAlchemyRepository),
        v: UserValidator = Depends(create_user_validator),
) -> UserService:
    return UserServiceImpl(r, v)
