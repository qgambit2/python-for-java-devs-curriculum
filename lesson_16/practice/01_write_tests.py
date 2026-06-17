"""
Lesson 16 — write pytest tests (JUnit 5 parallel).

Read:
    lesson_16/01_pytest_junit5.py
    lesson_16/02_fixtures_and_parametrize.py
    lesson_16/03_mocking.py

Replace each pytest.fail("TODO") with a real test, then run:
    uv run pytest lesson_16/practice/01_write_tests.py -v

Or:
    uv run python lesson_16/practice/01_write_tests.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _code_under_test import Greeter, add, clamp, divide  # noqa: E402


# ---------------------------------------------------------------------------
# Exercises — replace pytest.fail("TODO") with real tests
# ---------------------------------------------------------------------------


# Exercise 1: assert add(2, 3) == 5
def test_add_basic() -> None:
    pytest.fail("TODO: assert add(2, 3) == 5")


# Exercise 2: assert divide(10, 4) == 2.5
def test_divide_normal() -> None:
    pytest.fail("TODO: assert divide(10, 4) == 2.5")


# Exercise 3: divide(1, 0) raises ZeroDivisionError (use pytest.raises + match=)
def test_divide_by_zero() -> None:
    pytest.fail("TODO: with pytest.raises(ZeroDivisionError, match='division by zero'):")


# Exercise 4: clamp(5, 0, 10) == 5 and clamp(-1, 0, 10) == 0 in one test
def test_clamp() -> None:
    pytest.fail("TODO: two asserts for middle and below-range")


# Exercise 5: parametrize — (a, b, want): (1, 1, 2), (10, -3, 7)
@pytest.mark.parametrize(
    "a,b,want",
    [
        (1, 1, 2),
        (10, -3, 7),
    ],
)
def test_add_parametrized(a: int, b: int, want: int) -> None:
    pytest.fail("TODO: assert add(a, b) == want")


# Exercise 6: MagicMock name provider → Greeter.greet() == "Hello, Pat!"
def test_greeter_mock() -> None:
    pytest.fail("TODO: provider = MagicMock(); provider.get_name.return_value = 'Pat'")


# Exercise 7: clamp(5, 10, 0) raises ValueError (invalid lo/hi)
def test_clamp_invalid_range() -> None:
    pytest.fail("TODO: pytest.raises(ValueError)")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"]))
