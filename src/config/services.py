from fastapi.params import Depends

from src.application.services.user import UserServiceImpl
from src.config.repositories import create_user_repository
from src.ports.inbound.services.user import UserService
from src.ports.outbound.repositories.user import UserRepository


def create_user_service(r: UserRepository = Depends(create_user_repository)) -> UserService:
    return UserServiceImpl(r)
