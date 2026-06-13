"""Lesson 0 index — environment setup (read before Lesson 1)."""

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
    "01_setup_mac_linux.py",
    "02_setup_windows.py",
    "03_verify_environment.py",
]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
