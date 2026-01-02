from dataclasses import asdict
from typing import List

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.outbound.config import create_db
from src.adapters.outbound.mappers import UserOrmMapper
from src.adapters.outbound.orms import UserOrm
from src.domain import User


class UserSqlAlchemyRepository:

    def __init__(self,
                 db: AsyncSession = Depends(create_db),
                 mapper: UserOrmMapper = Depends()):
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
        user_as_dict = asdict(updated_user)
        stmt = (insert(UserOrm)
                .values(**user_as_dict)
                .on_conflict_do_update(index_elements=[UserOrm.id], set_=user_as_dict))
        await self.db.execute(stmt)
        await self.db.commit()

    async def delete(self, user_id: int) -> None:
        stmt = (delete(UserOrm).where(UserOrm.id == user_id))
        await self.db.execute(stmt)
        await self.db.commit()
