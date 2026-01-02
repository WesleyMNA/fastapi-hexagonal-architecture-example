from typing import List, Protocol

from src.domain import User


class UserService(Protocol):

    async def find_all(self) -> List[User]:
        pass

    async def find_by_id(self, user_id: int) -> User:
        pass

    async def create(self, user: User) -> User:
        pass
