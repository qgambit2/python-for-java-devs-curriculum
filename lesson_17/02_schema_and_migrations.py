"""Lesson 17b — schema DDL, transactions, migrations (Alembic ≈ Flyway).

Run:
    uv run python lesson_17/02_schema_and_migrations.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from _lesson17_schema import BOOKS_DDL, connect_sqlite_memory


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java migrations map")

print("""
| Java                          | Python                              |
|-------------------------------|-------------------------------------|
| Flyway / Liquibase SQL files  | Alembic revision scripts            |
| @Entity schema from JPA       | SQLAlchemy metadata.create_all()    |
| conn.setAutoCommit(false)     | conn.execute("BEGIN") / commit()    |
""")


section("1. DDL — CREATE TABLE")

with connect_sqlite_memory() as conn:
    conn.executescript(BOOKS_DDL)
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    print("tables:", [t["name"] for t in tables])


section("2. Transactions — commit vs rollback")

conn = connect_sqlite_memory()
try:
    conn.execute("BEGIN")
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Draft", "Nobody"))
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Also Draft", "Nobody"))
    # simulate error before commit:
    raise ValueError("business rule failed")
    conn.commit()  # noqa: B012 — unreachable demo
except ValueError:
    conn.rollback()
    print("rolled back — no rows persisted")

count = conn.execute("SELECT COUNT(*) AS n FROM books").fetchone()["n"]
print(f"count after rollback: {count}")

conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Saved", "Author"))
conn.commit()
print(f"count after commit: {conn.execute('SELECT COUNT(*) AS n FROM books').fetchone()['n']}")
conn.close()


section("3. Schema change — manual migration step")

# Alembic would version this as V002__add_published_year.sql
MIGRATION_V2 = "ALTER TABLE books ADD COLUMN published_year INTEGER;"

conn = connect_sqlite_memory()
conn.executescript(BOOKS_DDL)
conn.execute(MIGRATION_V2)
conn.execute(
    "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
    ("Refactoring", "Fowler", 1999),
)
conn.commit()
row = conn.execute("SELECT title, published_year FROM books").fetchone()
print(f"after migration: {row['title']} ({row['published_year']})")
conn.close()

print("""
Alembic (production):
  alembic revision -m "add published_year"
  alembic upgrade head
≈ Flyway migrate — versioned SQL or autogenerate from SQLAlchemy models.
""")
