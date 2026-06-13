"""Lesson 4 index — loops, truthiness, functions."""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


from pathlib import Path

from _lesson_runner import run_lesson_index

LESSONS = ["01_loops.py", "02_truthiness.py", "03_functions.py"]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
