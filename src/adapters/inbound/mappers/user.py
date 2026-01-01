from src.adapters.inbound.dtos.user import UserCreate
from src.domain.models.user import User


def from_create_req(r: UserCreate) -> User:
    return User(**r.model_dump())