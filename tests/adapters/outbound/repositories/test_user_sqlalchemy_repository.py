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
        expected_users = await self._save_multiple_users()

        result_users = await self.repository.find_all()

        assert len(result_users) == len(expected_users)

    async def _save_multiple_users(self) -> list[User]:
        result = [
            self._create_faker_user()
            for _ in range(self.faker.random_int(1, 100))
        ]
        for u in result:
            await self.repository.save(u)
        return result

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

    async def test_save(self):
        user = self._create_faker_user()

        saved_user = await self.repository.save(user)

        assert saved_user is not None
        assert saved_user.name == user.name
        assert saved_user.email == user.email

    async def test_update(self):
        saved_user = await self.repository.save(self._create_faker_user())
        updated_user = self._create_faker_user()
        updated_user.id = saved_user.id
        await self.repository.update(updated_user)

        result_user = await self.repository.find_by_id(saved_user.id)

        assert result_user is not None
        assert result_user.name == updated_user.name
        assert result_user.email == updated_user.email

    async def test_delete_by_id(self):
        saved_user = await self.repository.save(self._create_faker_user())

        await self.repository.delete_by_id(saved_user.id)
        result_user = await self.repository.find_by_id(saved_user.id)

        assert result_user is None

    async def test_delete_all(self):
        await self._save_multiple_users()

        await self.repository.delete_all()
        users = await self.repository.find_all()

        assert len(users) == 0

    async def test_exists_by_id_should_return_true_when_id_exists(self):
        saved_user = await self.repository.save(self._create_faker_user())

        user_exists = await self.repository.exists_by_id(saved_user.id)

        assert user_exists

    async def test_exists_by_id_should_return_false_when_id_does_not_exists(self):
        user_exists = await self.repository.exists_by_id(1)

        assert user_exists is False

    async def test_exists_by_email_should_return_true_when_email_exists(self):
        saved_user = await self.repository.save(self._create_faker_user())

        user_exists = await self.repository.exists_by_email(saved_user.email)

        assert user_exists

    async def test_exists_by_email_should_return_false_when_email_does_not_exists(self):
        user_exists = await self.repository.exists_by_email('fake@email.com')

        assert user_exists is False

    async def test_exists_by_id_not_and_email_should_return_true_when_email_exists_with_different_id(self):
        saved_user = await self.repository.save(self._create_faker_user())

        user_exists = await self.repository.exists_by_id_not_and_email(saved_user.id + 1, saved_user.email)

        assert user_exists

    async def test_exists_by_id_not_and_email_should_return_false_when_email_does_not_exists_with_different_id(self):
        saved_user = await self.repository.save(self._create_faker_user())

        user_exists = await self.repository.exists_by_id_not_and_email(saved_user.id, 'fake@email.com')

        assert user_exists is False
