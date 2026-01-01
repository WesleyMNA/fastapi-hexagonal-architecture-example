from dataclasses import asdict

from src.adapters.outbound.orms.user import UserOrm
from src.domain.models.user import User


class UserOrmMapper:
    @staticmethod
    def to_domain(u: UserOrm | type[UserOrm]) -> User:
        return User(u.name, u.email, u.id)

    @staticmethod
    def to_orm(u: User) -> UserOrm:
        return UserOrm(**asdict(u))
