from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserPatch(BaseModel):
    name: str | None = None
    email: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
