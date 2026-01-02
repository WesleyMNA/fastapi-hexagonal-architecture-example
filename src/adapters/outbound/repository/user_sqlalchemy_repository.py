from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.adapters.outbound.config import create_db
from src.adapters.outbound.mappers import UserOrmMapper
from src.adapters.outbound.orms import UserOrm
from src.domain import User


class UserSqlAlchemyRepository:

    def __init__(self,
                 db: Session = Depends(create_db),
                 mapper: UserOrmMapper = Depends()):
        self.db = db
        self.mapper = mapper

    def find_all(self) -> List[User]:
        result = self.db.query(UserOrm).all()
        return [self.mapper.to_domain(r) for r in result]

    def find_by_id(self, user_id: int) -> User | None:
        result = self.db.query(UserOrm).where(UserOrm.id == user_id).first()
        return self.mapper.to_domain(result) if result is not None else None

    def create(self, new_user: User) -> User:
        result = self.mapper.to_orm(new_user)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return self.mapper.to_domain(result)
