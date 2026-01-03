from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    email: str


class UserPatchRequest(BaseModel):
    name: str | None = None
    email: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
