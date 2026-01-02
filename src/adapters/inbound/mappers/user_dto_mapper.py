from src.adapters.inbound.dtos import UserCreate
from src.domain import User


async def from_create_req(r: UserCreate) -> User:
    return User(**r.model_dump())
