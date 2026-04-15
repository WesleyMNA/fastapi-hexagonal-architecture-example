from sqlalchemy import String, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.outbound.config import Base


class UserOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email_encrypted: Mapped[str] = mapped_column(TEXT, nullable=False)
    email_hash: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    def __repr__(self):
        return f'UserOrm(id={self.id}, name={self.name!r})'
