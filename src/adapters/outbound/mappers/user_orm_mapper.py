from typing import Annotated

from fastapi import Depends

from src.adapters.outbound.orms import UserOrm
from src.domain import User


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
