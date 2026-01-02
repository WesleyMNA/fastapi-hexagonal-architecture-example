from typing import List, Protocol

from src.domain.models.user import User


class UserService(Protocol):

    def find_all(self) -> List[User]:
        pass

    def find_by_id(self, user_id: int) -> User:
        pass

    def create(self, user: User) -> User:
        pass
