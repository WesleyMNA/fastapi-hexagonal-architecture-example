from abc import ABC, abstractmethod
from typing import List

from src.domain.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass
