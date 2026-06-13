"""Lesson 8 index — classes, OOP & dataclasses."""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


from pathlib import Path

from _lesson_runner import run_lesson_index

LESSONS = [
    "01_class_basics.py",
    "02_self_explained.py",
    "03_str_repr_and_formatting.py",
    "04_inheritance.py",
    "05_class_vs_instance.py",
    "06_dataclass.py",
    "07_eq_and_hash.py",
    "08_collections_and_sorting.py",
]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
