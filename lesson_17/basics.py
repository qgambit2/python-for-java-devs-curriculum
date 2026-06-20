"""Lesson 17 index — database access (DB-API, SQLAlchemy, Flask)."""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from _lesson_runner import run_lesson_index

LESSONS = [
    "01_db_api_sqlite.py",
    "02_schema_and_migrations.py",
    "03_sqlalchemy_core.py",
    "04_sqlalchemy_orm.py",
    "05_flask_sqlalchemy.py",
]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
