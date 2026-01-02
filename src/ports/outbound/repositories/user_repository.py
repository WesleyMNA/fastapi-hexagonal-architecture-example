from typing import List, Protocol

from src.domain import User


class UserRepository(Protocol):

    async def find_all(self) -> List[User]:
        pass

    async def find_by_id(self, user_id: int) -> User | None:
        pass

    async def save(self, new_user: User) -> User:
        pass

    async def update(self, updated_user: User) -> None:
        pass

    async def delete_by_id(self, user_id: int) -> None:
        pass