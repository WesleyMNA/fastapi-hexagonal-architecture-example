from typing import Protocol


class UserValidatorProtocol(Protocol):

    async def exists_by_id(self, user_id: int) -> bool:
        ...

    async def exists_by_email(self, email: str) -> bool:
        ...

    async def exists_by_id_not_and_email(self, user_id: int, email: str) -> bool:
        ...
