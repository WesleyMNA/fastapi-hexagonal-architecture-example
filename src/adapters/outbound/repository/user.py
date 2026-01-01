from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.adapters.outbound.config import create_db
from src.adapters.outbound.orms.user import UserOrm
from src.domain.models.user import User
from src.ports.outbound.repositories.user import UserRepository


def to_user(u: UserOrm | type[UserOrm]) -> User:
    return User(u.name, u.email, u.id)


class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session = Depends(create_db)):
        self.db = db

    def find_all(self) -> List[User]:
        result = self.db.query(UserOrm).all()
        return [to_user(r) for r in result]

    def find_by_id(self, user_id: int) -> User | None:
        result = self.db.query(UserOrm).filter(UserOrm.id == user_id).first()
        return to_user(result) if result is not None else None

    def create(self, new_user: User) -> User:
        result = UserOrm(name=new_user.name, email=new_user.email)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return to_user(result)
