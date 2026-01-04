from typing import List

from sqlalchemy import select, delete, exists, update

from src.adapters.outbound.config import AsyncSessionDep
from src.adapters.outbound.mappers import UserOrmMapperDep
from src.adapters.outbound.orms import UserOrm
from src.domain import User


class UserSqlAlchemyRepository:

    def __init__(self,
                 db: AsyncSessionDep,
                 mapper: UserOrmMapperDep):
        self.db = db
        self.mapper = mapper

    async def find_all(self) -> List[User]:
        result = await self.db.execute(select(UserOrm))
        return [await self.mapper.to_domain(r) for r in result.scalars().all()]

    async def find_by_id(self, user_id: int) -> User | None:
        stmt = select(UserOrm).where(UserOrm.id == user_id)
        query = await self.db.execute(stmt)
        result = query.scalar()
        return await self.mapper.to_domain(result) if result is not None else None

    async def save(self, new_user: User) -> User:
        result = await self.mapper.to_orm(new_user)
        self.db.add(result)
        await self.db.commit()
        await self.db.refresh(result)
        return await self.mapper.to_domain(result)

    async def update(self, updated_user: User) -> None:
        stmt = (update(UserOrm)
                .where(UserOrm.id == updated_user.id)
                .values(name=updated_user.name, email=updated_user.email))
        await self.db.execute(stmt)
        await self.db.commit()

    async def delete_by_id(self, user_id: int) -> None:
        stmt = (delete(UserOrm).where(UserOrm.id == user_id))
        await self.db.execute(stmt)
        await self.db.commit()

    async def exists_by_id(self, user_id: int) -> bool:
        stmt = select(exists(UserOrm).where(UserOrm.id == user_id))
        query = await self.db.execute(stmt)
        return query.scalar()

    async def exists_by_email(self, email: str) -> bool:
        stmt = select(exists(UserOrm).where(UserOrm.email == email))
        query = await self.db.execute(stmt)
        return query.scalar()

    async def exists_by_id_not_and_email(self, user_id: int, email: str) -> bool:
        stmt = select(exists(UserOrm).where(UserOrm.id != user_id, UserOrm.email == email))
        query = await self.db.execute(stmt)
        return query.scalar()
