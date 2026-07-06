from typing import Annotated

from fastapi import Depends

from src.domain.user.user_model import User
from src.infrastructure.persistence.orms import UserOrm


class UserOrmMapper:
    @staticmethod
    async def to_domain(u: UserOrm) -> User:
        return User(
            id=u.id,
            name=u.name,
            email_encrypted=u.email_encrypted,
            email_hash=u.email_hash,
        )

    @staticmethod
    async def to_orm(u: User) -> UserOrm:
        return UserOrm(
            id=u.id,
            name=u.name,
            email_encrypted=u.email_encrypted,
            email_hash=u.email_hash,
        )


UserOrmMapperDep = Annotated[UserOrmMapper, Depends(UserOrmMapper)]
