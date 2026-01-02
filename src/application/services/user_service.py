from typing import List

from src.application.exceptions import NotFound, Conflict
from src.domain import User
from src.ports.inbound import UserValidator
from src.ports.outbound import UserRepository

_EMAIL_ALREADY_EXISTS_MESSAGE = 'Email already exists'
_NOT_FOUND_MESSAGE = 'User not found'


class UserServiceImpl:

    def __init__(self, repository: UserRepository, validator: UserValidator):
        self.repository = repository
        self.validator = validator

    async def find_all(self) -> List[User]:
        return await self.repository.find_all()

    async def find_by_id(self, user_id: int) -> User:
        result = await self.repository.find_by_id(user_id)
        if not result:
            raise NotFound(_NOT_FOUND_MESSAGE)
        return result

    async def create(self, user: User) -> User:
        email_exists = await self.validator.exists_by_email(user.email)
        if email_exists:
            raise Conflict(_EMAIL_ALREADY_EXISTS_MESSAGE)
        return await self.repository.save(user)

    async def update(self, user_id: int, updated_user: User) -> None:
        user = await self.find_by_id(user_id)
        await self.validate_email(user_id, updated_user.email)
        user.name = updated_user.name
        user.email = updated_user.email
        await self.repository.update(user)

    async def validate_email(self, user_id: int, email: str) -> None:
        exists = await self.validator.exists_by_id_not_and_email(user_id, email)
        if exists:
            raise Conflict(_EMAIL_ALREADY_EXISTS_MESSAGE)

    async def patch(self, user_id: int, updated_user: User) -> None:
        user = await self.find_by_id(user_id)
        if updated_user.name is not None:
            user.name = updated_user.name
        if updated_user.email is not None:
            await self.validate_email(user_id, updated_user.email)
            user.email = updated_user.email
        await self.repository.update(user)

    async def delete(self, user_id: int) -> None:
        user_exists = await self.validator.exists_by_id(user_id)
        if not user_exists:
            raise NotFound(_NOT_FOUND_MESSAGE)
        await self.repository.delete_by_id(user_id)
