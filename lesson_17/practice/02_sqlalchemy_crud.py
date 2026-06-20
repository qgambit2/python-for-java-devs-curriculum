"""
Lesson 17 — SQLAlchemy ORM practice (≈ JPA).

Read:
    lesson_17/04_sqlalchemy_orm.py

Fill in each function, then run:
    uv run python lesson_17/practice/02_sqlalchemy_crud.py
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

from sqlalchemy import select
from sqlalchemy.orm import Session

from _lesson17_db import Book, make_engine


# Exercise 1: Create book, persist, return id
def add_book(session: Session, title: str, author: str = "") -> int:
    pass


# Exercise 2: Return titles sorted A→Z
def list_titles(session: Session) -> list[str]:
    pass


# Exercise 3: Delete by id; return True if deleted, False if id missing
def delete_book(session: Session, book_id: int) -> bool:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq


def _run_tests() -> None:
    engine = make_engine()
    with Session(engine) as session:
        id1 = add_book(session, "Clean Code", "Martin")
        check_eq(id1, 1, "add_book — id")
        add_book(session, "Effective Java", "Bloch")
        check_eq(
            list_titles(session),
            ["Clean Code", "Effective Java"],
            "list_titles",
        )
        check_eq(delete_book(session, 99), False, "delete_book — missing")
        check_eq(delete_book(session, id1), True, "delete_book — ok")
        check_eq(list_titles(session), ["Effective Java"], "after delete")

    print("\nAll tests passed! SQLAlchemy ORM practice complete.")


if __name__ == "__main__":
    _run_tests()
