from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import func, select

from db.db import get_engine
from models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    passkey: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False, default=func.now())
    updated_at: Mapped[str] = mapped_column(nullable=False, default=func.now())


engine = get_engine()


def create(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()


def find_by_id(id: int):
    statement = select(User).filter(User.id == id).order_by(User.id.desc()).limit(1)
    with Session(engine) as session:
        return session.execute(statement).fetchone()[0]
