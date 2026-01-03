from src.ports.outbound import UserRepositoryProtocol


class UserValidator:

    def __init__(self, repository: UserRepositoryProtocol):
        self.repository = repository

    async def exists_by_id(self, user_id: int) -> bool:
        return await self.repository.exists_by_id(user_id)

    async def exists_by_email(self, email: str) -> bool:
        return await self.repository.exists_by_email(email)

    async def exists_by_id_not_and_email(self, user_id: int, email: str) -> bool:
        return await self.repository.exists_by_id_not_and_email(user_id, email)
