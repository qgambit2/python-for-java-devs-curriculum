"""Lesson 17d — SQLAlchemy ORM (≈ JPA EntityManager).

Run:
    uv run python lesson_17/04_sqlalchemy_orm.py

Practice:
    uv run python lesson_17/practice/02_sqlalchemy_crud.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from sqlalchemy import select
from sqlalchemy.orm import Session

from _lesson17_db import Book, book_to_dict, make_engine, seed_books


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java JPA map")

print("""
| JPA / Hibernate               | SQLAlchemy ORM                      |
|-------------------------------|-------------------------------------|
| @Entity class Book            | class Book(Base): __tablename__     |
| @Id @GeneratedValue           | Mapped[int] primary_key=True        |
| EntityManager.persist(book)   | session.add(book); session.commit() |
| em.find(Book.class, id)       | session.get(Book, id)               |
| JPQL / Criteria API           | select(Book).where(...)             |
| @Transactional                | with Session(engine) as session:    |
""")


engine = make_engine()

section("1. persist — add + commit")

with Session(engine) as session:
    book = Book(title="Clean Architecture", author="Martin")
    session.add(book)
    session.commit()
    session.refresh(book)
    print(f"persisted id={book.id} title={book.title}")


section("2. find and query")

with Session(engine) as session:
    seed_books(session)
    by_id = session.get(Book, 1)
    print(f"get: {book_to_dict(by_id) if by_id else None}")

    titles = session.scalars(select(Book.title).order_by(Book.title)).all()
    print("all titles:", titles)

    martin_books = session.scalars(
        select(Book).where(Book.author == "Martin")
    ).all()
    print("Martin:", [b.title for b in martin_books])


section("3. update and delete")

with Session(engine) as session:
    book = session.scalars(select(Book).where(Book.title == "Clean Code")).one()
    book.author = "Robert C. Martin"
    session.commit()

with Session(engine) as session:
    book = session.scalars(select(Book).where(Book.title == "Effective Java")).one()
    session.delete(book)
    session.commit()
    remaining = session.scalars(select(Book.title)).all()
    print("after delete:", remaining)
