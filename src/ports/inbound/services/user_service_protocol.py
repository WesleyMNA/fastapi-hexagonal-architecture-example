from typing import List, Protocol

from src.domain import User


class UserServiceProtocol(Protocol):

    async def find_all(self) -> List[User]:
        pass

    async def find_by_id(self, user_id: int) -> User:
        pass

    async def create(self, user: User) -> User:
        pass

    async def update(self, user_id: int, updated_user: User) -> None:
        pass

    async def patch(self, user_id: int, updated_user: User) -> None:
        pass

    async def delete(self, user_id: int) -> None:
        pass
