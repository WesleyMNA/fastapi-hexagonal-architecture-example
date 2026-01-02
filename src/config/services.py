from fastapi.params import Depends

from src.adapters.outbound import UserSqlAlchemyRepository
from src.application import UserServiceImpl
from src.ports.inbound import UserService
from src.ports.outbound import UserRepository


async def create_user_service(r: UserRepository = Depends(UserSqlAlchemyRepository)) -> UserService:
    return UserServiceImpl(r)
