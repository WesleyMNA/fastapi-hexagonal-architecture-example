from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.adapters.outbound.config.db import create_db
from src.adapters.outbound.repository.user import UserRepositoryImpl
from src.ports.outbound.repositories.user import UserRepository


def create_user_repository(db: Session = Depends(create_db)) -> UserRepository:
    return UserRepositoryImpl(db)
