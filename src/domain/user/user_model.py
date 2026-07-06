from dataclasses import dataclass


@dataclass
class User:
    name: str
    id: int | None = None
    email: str | None = None
    email_hash: str | None = None
    email_encrypted: str | None = None
