import pytest

from src.adapters.outbound import UserSqlAlchemyRepository
from src.adapters.outbound.mappers.user_orm_mapper import UserOrmMapper
from src.domain import User
from src.ports.outbound import UserRepositoryProtocol


@pytest.mark.anyio
class TestUserSqlAlchemyRepository:

    @pytest.fixture(autouse=True)
    async def _setup(self, get_db_session, get_faker):
        self.db = get_db_session
        self.repository: UserRepositoryProtocol = UserSqlAlchemyRepository(self.db, UserOrmMapper())
        self.faker = get_faker
        yield
        await self.repository.delete_all()

    async def test_find_all(self):
        expected_users = [
            self._create_faker_user()
            for _ in range(self.faker.random_int(1, 100))
        ]
        for u in expected_users:
            await self.repository.save(u)

        users = await self.repository.find_all()
        assert len(users) == len(expected_users)

    def _create_faker_user(self) -> User:
        return User(name=self.faker.name(), email=self.faker.email())

    async def test_find_by_id_should_return_user_when_id_exists(self):
        saved_user = await self.repository.save(self._create_faker_user())

        result_user = await self.repository.find_by_id(saved_user.id)

        assert result_user is not None
        assert result_user.id == saved_user.id
        assert result_user.name == saved_user.name
        assert result_user.email == saved_user.email

    async def test_find_by_id_should_return_none_when_id_does_not_exist(self):
        user = await self.repository.find_by_id(1)

        assert user is None
