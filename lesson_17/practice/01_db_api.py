"""
Lesson 17 — DB-API practice (sqlite3 ≈ JDBC).

Read:
    lesson_17/01_db_api_sqlite.py

Fill in each function, then run:
    uv run python lesson_17/practice/01_db_api.py

Use sqlite3 with ? placeholders only — no f-string SQL.
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

_lesson = Path(__file__).resolve().parent.parent
if str(_lesson) not in sys.path:
    sys.path.insert(0, str(_lesson))

from _lesson17_schema import connect_sqlite_memory


# Exercise 1: Return number of rows in books (assume schema exists)
def count_books(conn) -> int:
    pass


# Exercise 2: Insert a book; return new row id (lastrowid)
def insert_book(conn, title: str, author: str) -> int:
    pass


# Exercise 3: Return titles sorted alphabetically
def list_titles(conn) -> list[str]:
    pass


# Exercise 4: Find author by exact title, or None if missing
def find_author(conn, title: str) -> str | None:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq


def _run_tests() -> None:
    conn = connect_sqlite_memory()
    check_eq(count_books(conn), 0, "count_books — empty")

    book_id = insert_book(conn, "Clean Code", "Martin")
    check_eq(book_id, 1, "insert_book — first id")
    insert_book(conn, "Effective Java", "Bloch")
    check_eq(count_books(conn), 2, "count_books — after inserts")

    check_eq(
        list_titles(conn),
        ["Clean Code", "Effective Java"],
        "list_titles — sorted",
    )
    check_eq(find_author(conn, "Clean Code"), "Martin", "find_author — hit")
    check_eq(find_author(conn, "Missing"), None, "find_author — miss")
    conn.close()

    print("\nAll tests passed! DB-API practice complete.")


if __name__ == "__main__":
    _run_tests()
