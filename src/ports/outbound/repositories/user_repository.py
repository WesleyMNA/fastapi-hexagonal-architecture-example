from typing import List, Protocol

from src.domain import User


class UserRepository(Protocol):

    def find_all(self) -> List[User]:
        pass

    def find_by_id(self, user_id: int) -> User | None:
        pass

    def create(self, user: User) -> User:
        pass
