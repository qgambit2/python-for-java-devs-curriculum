"""Lesson 17f — Transactions with DB-API sqlite3 (≈ JDBC / @Transactional).

The big surprise for Java devs: JDBC defaults to auto-commit ON, but
sqlite3 defaults to auto-commit OFF — a transaction opens implicitly before
the first data-modifying statement and stays open until YOU commit().

Run:
    uv run python lesson_17/06_transactions.py

Practice:
    uv run python lesson_17/practice/01_db_api.py
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from _lesson17_schema import connect_sqlite_memory


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


def count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) AS n FROM books").fetchone()["n"]


section("0. Java JDBC map")

print("""
| Java JDBC                          | Python DB-API (sqlite3)             |
|------------------------------------|-------------------------------------|
| autoCommit = true (default)        | autoCommit = false (default!)       |
| setAutoCommit(false)               | (no-op — txn already open)          |
| conn.commit()                      | conn.commit()                       |
| conn.rollback()                    | conn.rollback()                     |
| @Transactional method              | with conn:  (commit / rollback)     |
| Savepoint sp = conn.setSavepoint() | conn.execute("SAVEPOINT sp")        |
""")


section("1. The forgotten-commit gotcha")

# Java: with autoCommit ON this row would already be saved.
# Python: without commit() the implicit transaction is discarded on close.
conn = connect_sqlite_memory()
conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Ghost", "Nobody"))
print(f"rows before close, no commit: {count(conn)}")  # 1 — visible on THIS conn
conn.close()  # transaction never committed -> row is gone

conn2 = connect_sqlite_memory()  # fresh :memory: db, but proves the point
print("lesson: an uncommitted INSERT is rolled back when the conn closes")
conn2.close()


section("2. with conn: — commit on success (the idiom)")

# Java: ≈ @Transactional — happy path commits.
conn = connect_sqlite_memory()
with conn:
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Clean Code", "Martin"))
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Refactoring", "Fowler"))
# block exited cleanly -> both rows committed together
print(f"committed atomically: {count(conn)} rows")
conn.close()


section("3. with conn: — rollback on exception (all-or-nothing)")

conn = connect_sqlite_memory()
try:
    with conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Saved?", "A"))
        # NOT NULL on title -> IntegrityError propagates out of the block
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (None, "B"))
except sqlite3.IntegrityError as exc:
    print(f"caught: {exc}")
# the first INSERT rolled back too — either both land or neither does
print(f"after rollback: {count(conn)} rows (the 'Saved?' row did NOT persist)")
conn.close()


section("4. Explicit commit / rollback — JDBC-style by hand")

# Java: setAutoCommit(false); try { ...; commit(); } catch { rollback(); }
conn = connect_sqlite_memory()
try:
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Effective Java", "Bloch"))
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("DDD", "Evans"))
    conn.commit()
    print(f"explicit commit: {count(conn)} rows")
except sqlite3.Error:
    conn.rollback()
    raise
conn.close()


section("5. SAVEPOINT — partial rollback inside a transaction")

# Java: Savepoint sp = conn.setSavepoint(); ... conn.rollback(sp);
conn = connect_sqlite_memory()
conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Keep me", "X"))
conn.execute("SAVEPOINT sp1")
conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Undo me", "Y"))
print(f"inside savepoint: {count(conn)} rows")
conn.execute("ROLLBACK TO sp1")  # undo only since the savepoint
conn.execute("RELEASE sp1")
conn.commit()
print(f"after ROLLBACK TO savepoint + commit: {count(conn)} rows (only 'Keep me')")
conn.close()
