"""Lesson 16d — unittest legacy (JUnit 4 shape) — read if you see old code.

**Default for new Python projects: pytest** (01_pytest_junit5.py) — maps to JUnit 5.

unittest in the stdlib mirrors **JUnit 4**: TestCase classes, setUp/tearDown,
self.assertEqual. You may see it in older codebases; you do not need it for new work.

Run:
    uv run python lesson_16/04_unittest_legacy.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _code_under_test import add, divide


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. When you still see unittest")

print("""
| JUnit 4              | unittest (stdlib)              |
|----------------------|--------------------------------|
| extends base class   | class TestFoo(unittest.TestCase) |
| @Before setUp()      | def setUp(self)                |
| assertEquals(e, a)   | self.assertEqual(a, e)  ← actual first! |
| assertThrows         | with self.assertRaises(Ex):    |

Prefer pytest for new tests. One-off to run legacy suite:
    uv run python -m unittest lesson_16/04_unittest_legacy.py -v
""")


class TestArithmeticLegacy(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
