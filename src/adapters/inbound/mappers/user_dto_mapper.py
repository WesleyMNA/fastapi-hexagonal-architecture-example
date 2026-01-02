from src.adapters.inbound.dtos import UserCreate, UserPatch
from src.domain import User


async def from_create_req(r: UserCreate) -> User:
    return User(**r.model_dump())


async def from_patch_req(r: UserPatch) -> User:
    return User(**r.model_dump())
