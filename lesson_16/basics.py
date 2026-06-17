"""Lesson 16 index — unit testing (JUnit 5 / pytest primary)."""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from _lesson_runner import run_lesson_index

LESSONS = [
    "01_pytest_junit5.py",
    "02_fixtures_and_parametrize.py",
    "03_mocking.py",
    "04_unittest_legacy.py",
    "05_flask_testing.py",
]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
