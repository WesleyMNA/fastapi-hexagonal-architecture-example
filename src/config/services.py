from fastapi.params import Depends

from src.adapters.outbound.repository import UserSqlAlchemyRepository
from src.application.services.user import UserServiceImpl
from src.ports.inbound.services.user import UserService
from src.ports.outbound.repositories.user import UserRepository


def create_user_service(r: UserRepository = Depends(UserSqlAlchemyRepository)) -> UserService:
    return UserServiceImpl(r)
