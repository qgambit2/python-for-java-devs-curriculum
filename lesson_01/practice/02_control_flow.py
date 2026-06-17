"""
Lesson 1 — control flow practice.

Read:
    lesson_01/03_control_flow.py

Fill in each function, then run:
    uv run python lesson_01/practice/02_control_flow.py
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: Return "positive", "negative", or "zero"
def sign(n: int) -> str:
    pass


# Exercise 2: Return letter grade — A>=90, B>=80, C>=70, else F
def letter_grade(score: int) -> str:
    pass


# Exercise 3: Sum integers in nums (for loop)
def sum_list(nums: list[int]) -> int:
    pass


# Exercise 4: Return first value > threshold, or None if none
def first_above(nums: list[int], threshold: int) -> int | None:
    pass


# Exercise 5: Count down from n to 1 using while; return "done"
def countdown(n: int) -> str:
    pass


# Exercise 6: HTTP status label — use match/case (see lesson §6)
# http_status(200) -> "ok", 404 -> "missing", 500|502|503 -> "server error", else -> "other"
def http_status(code: int) -> str:
    pass


# Exercise 7: Command label — match on string (Java switch on String)
# command_action("start") -> "run", "stop" -> "halt", else -> "unknown"
def command_action(cmd: str) -> str:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
from _test_helpers import check_eq


def _run_tests() -> None:
    check_eq(sign(5), "positive", "sign — positive")
    check_eq(sign(-1), "negative", "sign — negative")
    check_eq(sign(0), "zero", "sign — zero")

    check_eq(letter_grade(95), "A", "letter_grade — A")
    check_eq(letter_grade(85), "B", "letter_grade — B")
    check_eq(letter_grade(72), "C", "letter_grade — C")
    check_eq(letter_grade(50), "F", "letter_grade — F")

    check_eq(sum_list([1, 2, 3]), 6, "sum_list")
    check_eq(sum_list([]), 0, "sum_list — empty")

    check_eq(first_above([1, 5, 3], 4), 5, "first_above")
    check_eq(first_above([1, 2], 10), None, "first_above — none")

    check_eq(countdown(3), "done", "countdown")
    check_eq(countdown(0), "done", "countdown — zero")

    check_eq(http_status(200), "ok", "http_status — 200")
    check_eq(http_status(404), "missing", "http_status — 404")
    check_eq(http_status(502), "server error", "http_status — 502")
    check_eq(http_status(999), "other", "http_status — other")

    check_eq(command_action("start"), "run", "command_action — start")
    check_eq(command_action("stop"), "halt", "command_action — stop")
    check_eq(command_action("pause"), "unknown", "command_action — unknown")

    print("\nAll tests passed! Control flow practice complete.")


if __name__ == "__main__":
    _run_tests()
