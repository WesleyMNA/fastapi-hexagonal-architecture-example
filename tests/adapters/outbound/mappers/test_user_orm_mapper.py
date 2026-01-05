import pytest

from src.adapters.outbound import UserOrm
from src.adapters.outbound.mappers.user_orm_mapper import UserOrmMapper
from src.domain import User


@pytest.mark.anyio
class TestUserOrmMapper:

    @pytest.fixture(autouse=True)
    async def _setup(self, get_faker):
        self.mapper = UserOrmMapper()
        self.faker = get_faker

    async def test_to_orm(self):
        domain_user = User(**self._create_base_user_data())

        orm_user = await UserOrmMapper.to_orm(domain_user)

        assert isinstance(orm_user, UserOrm)
        assert orm_user.id == domain_user.id
        assert orm_user.name == domain_user.name
        assert orm_user.email == domain_user.email

    def _create_base_user_data(self) -> dict:
        return {
            'id': self.faker.random_digit(),
            'name': self.faker.name(),
            'email': self.faker.email(),
        }

    async def test_to_domain(self):
        orm_user = UserOrm(**self._create_base_user_data())

        domain_user = await UserOrmMapper.to_domain(orm_user)

        assert isinstance(domain_user, User)
        assert domain_user.id == orm_user.id
        assert domain_user.name == orm_user.name
        assert domain_user.email == orm_user.email
