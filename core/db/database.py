from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    lat: Mapped[float]
    lon: Mapped[float]

    last_name: Mapped[Optional[str]]
    username: Mapped[Optional[str]]


engine = create_engine("sqlite:///users_db.sqlite3")


Base.metadata.create_all(engine)
