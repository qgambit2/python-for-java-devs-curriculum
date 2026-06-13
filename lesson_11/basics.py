"""Lesson 11 index — Flask REST API server."""

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
    "01_hello_flask.py",
    "02_routes_and_methods.py",
    "03_json_bodies.py",
    "04_path_and_query_params.py",
    "05_status_codes_and_errors.py",
    "06_crud_rest_service.py",
]

if __name__ == "__main__":
    run_lesson_index(LESSONS, lesson_dir=Path(__file__).parent)
