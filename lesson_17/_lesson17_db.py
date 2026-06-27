"""Lesson 17 — SQLAlchemy engine, models, and helpers."""

from __future__ import annotations

from _lesson17_schema import DEMO_DB_PATH
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

__all__ = [
    "Base",
    "Book",
    "DEMO_DB_PATH",
    "book_to_dict",
    "make_engine",
    "seed_books",
]


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str] = mapped_column(default="")


def make_engine(url: str = "sqlite:///:memory:", *, echo: bool = False):
    engine = create_engine(url, echo=echo)
    Base.metadata.create_all(engine)
    return engine


def seed_books(session: Session) -> None:
    if session.scalars(select(Book)).first() is not None:
        return
    session.add_all(
        [
            Book(title="Clean Code", author="Martin"),
            Book(title="Effective Java", author="Bloch"),
        ]
    )
    session.commit()


def book_to_dict(book: Book) -> dict[str, object]:
    return {"id": book.id, "title": book.title, "author": book.author}
