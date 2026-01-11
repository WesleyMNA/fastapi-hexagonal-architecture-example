from typing import List, Protocol

from src.domain import User


class UserRepositoryProtocol(Protocol):

    async def find_all(self) -> List[User]:
        ...

    async def find_by_id(self, user_id: int) -> User | None:
        ...

    async def save(self, new_user: User) -> User:
        ...

    async def update(self, updated_user: User) -> None:
        ...

    async def delete_by_id(self, user_id: int) -> None:
        ...

    async def delete_all(self):
        ...

    async def exists_by_id(self, user_id: int) -> bool:
        ...

    async def exists_by_email(self, email: str) -> bool:
        ...

    async def exists_by_id_not_and_email(self, user_id: int, email: str) -> bool:
        ...
