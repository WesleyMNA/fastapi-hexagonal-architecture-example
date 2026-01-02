from typing import Protocol


class UserValidator(Protocol):

    async def exists_by_id(self, user_id: int) -> bool:
        pass

    async def exists_by_email(self, email: str) -> bool:
        pass

    async def exists_by_id_not_and_email(self, user_id: int, email: str) -> bool:
        pass
