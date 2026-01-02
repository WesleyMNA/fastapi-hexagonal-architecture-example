from typing import List

from src.application.exceptions import NotFound
from src.domain import User
from src.ports.outbound import UserRepository


class UserServiceImpl:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def find_all(self) -> List[User]:
        return await self.repository.find_all()

    async def find_by_id(self, user_id: int) -> User:
        result = await self.repository.find_by_id(user_id)
        if not result:
            raise NotFound('User not found')
        return result

    async def create(self, user: User) -> User:
        return await self.repository.save(user)

    async def update(self, user_id: int, updated_user: User) -> None:
        user = await self.find_by_id(user_id)
        user.name = updated_user.name
        user.email = updated_user.email
        await self.repository.update(user)

    async def patch(self, user_id: int, updated_user: User) -> None:
        user = await self.find_by_id(user_id)
        if updated_user.name is not None:
            user.name = updated_user.name
        if updated_user.email is not None:
            user.email = updated_user.email
        await self.repository.update(user)

    async def delete(self, user_id: int) -> None:
        pass
