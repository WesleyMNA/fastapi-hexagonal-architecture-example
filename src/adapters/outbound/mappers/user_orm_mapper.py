from dataclasses import asdict

from src.adapters.outbound.orms import UserOrm
from src.domain import User


class UserOrmMapper:
    @staticmethod
    def to_domain(u: UserOrm) -> User:
        return User(
            id=u.id,
            name=u.name,
            email=u.email,
        )

    @staticmethod
    def to_orm(u: User) -> UserOrm:
        return UserOrm(**asdict(u))
