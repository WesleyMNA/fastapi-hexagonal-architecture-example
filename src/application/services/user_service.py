from typing import List

from src.application.exceptions import NotFound
from src.domain import User
from src.ports.outbound import UserRepository


class UserServiceImpl:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def find_all(self) -> List[User]:
        return self.repository.find_all()

    def find_by_id(self, user_id: int) -> User:
        result = self.repository.find_by_id(user_id)
        if not result:
            raise NotFound('User not found')
        return result

    def create(self, user: User) -> User:
        return self.repository.create(user)
