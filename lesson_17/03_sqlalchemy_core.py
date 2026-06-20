"""Lesson 17c — SQLAlchemy Core (≈ JdbcTemplate / explicit SQL).

Run:
    uv run python lesson_17/03_sqlalchemy_core.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from sqlalchemy import bindparam, insert, select, text, update

from _lesson17_db import Book, make_engine


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java map — SQLAlchemy Core")

print("""
| Java                          | SQLAlchemy Core                     |
|-------------------------------|-------------------------------------|
| DataSource / HikariCP         | create_engine("sqlite:///...")      |
| JdbcTemplate.queryForList     | conn.execute(select(...))           |
| JdbcTemplate.update(sql, ...) | conn.execute(text(...), params)     |
| RowMapper                     | row._mapping or row tuples          |
""")


engine = make_engine()

section("1. Raw SQL with text() — bound parameters")

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO books (title, author) VALUES (:title, :author)"),
        {"title": "Domain-Driven Design", "author": "Evans"},
    )
    conn.commit()
    row = conn.execute(
        text("SELECT title FROM books WHERE author = :author"),
        {"author": "Evans"},
    ).one()
    print(f"found: {row.title}")


section("2. SQL expression API — insert / select")

with engine.connect() as conn:
    conn.execute(
        insert(Book),
        [
            {"title": "Clean Code", "author": "Martin"},
            {"title": "Effective Java", "author": "Bloch"},
        ],
    )
    conn.commit()
    rows = conn.execute(select(Book.title).order_by(Book.title)).all()
    print("titles:", [r.title for r in rows])


section("3. update with bindparam")

with engine.connect() as conn:
    conn.execute(
        update(Book).where(Book.title == bindparam("t")).values(author="Updated"),
        [{"t": "Clean Code"}],
    )
    conn.commit()
    author = conn.execute(
        select(Book.author).where(Book.title == "Clean Code")
    ).scalar_one()
    print(f"Clean Code author now: {author}")

print("\nCore = SQL-first. Use when you want JdbcTemplate-style control without ORM entities.")
