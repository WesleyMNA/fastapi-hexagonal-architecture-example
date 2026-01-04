from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.outbound.config import Base


class UserOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    def __repr__(self):
        return f'UserOrm(id={self.id}, name={self.name!r}, email={self.email!r})'
