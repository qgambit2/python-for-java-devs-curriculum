"""Lesson 16a — pytest ≈ JUnit 5 (primary track).

If you know JUnit 5, pytest will feel familiar: plain tests, assert*, assertThrows,
@ParameterizedTest, @BeforeEach — with less boilerplate than JUnit 4 / unittest.

Run this file (executes pytest on the tests below):
    uv run python lesson_16/01_pytest_junit5.py

Run from terminal:
    uv run pytest lesson_16/01_pytest_junit5.py -v

Legacy unittest (JUnit 4 shape): see 04_unittest_legacy.py — read-only, not the default.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _code_under_test import add, clamp, divide


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. JUnit 5 test class — mental model")

print(r"""
Java (JUnit 5) — typical class you would write in src/test/java:

    import org.junit.jupiter.api.*;
    import static org.junit.jupiter.api.Assertions.*;

    @DisplayName("Arithmetic")
    class ArithmeticTest {

        @Test
        @DisplayName("adds two integers")
        void add() {
            assertEquals(5, add(2, 3));
        }

        @Test
        void divide() {
            assertEquals(2.5, divide(10, 4), 0.001);
        }

        @Test
        void divideByZero() {
            assertThrows(ZeroDivisionError.class, () -> divide(1, 0));
        }

        @Test
        void clampEdges() {
            assertAll(
                () -> assertEquals(0, clamp(-5, 0, 10)),
                () -> assertEquals(10, clamp(99, 0, 10))
            );
        }

        @Disabled("demonstration only")
        @Test
        void skipped() { }
    }

Python pytest — same ideas, no class required (tests in this file below):
    def test_add():           assert add(2, 3) == 5
    def test_divide():        assert divide(10, 4) == 2.5
    with pytest.raises(...):  ≈ assertThrows
    multiple assert lines     ≈ assertAll (no extra API)
    @pytest.mark.skip        ≈ @Disabled
""")


section("1. @Test → def test_* — plain assert ≈ assertEquals")

# JUnit 5:  @Test void add() { assertEquals(5, add(2, 3)); }


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(10, 4) == 2.5


section("2. assertThrows → pytest.raises")

# JUnit 5:
#   assertThrows(ZeroDivisionError.class, () -> divide(1, 0));
# Optional message match:
#   var ex = assertThrows(ZeroDivisionError.class, () -> divide(1, 0));
#   assertTrue(ex.getMessage().contains("division"));


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)


def test_clamp_invalid_range() -> None:
    with pytest.raises(ValueError, match="lo must be <= hi"):
        clamp(5, 10, 0)


section("3. assertAll → multiple asserts in one test")

# JUnit 5 groups soft assertions:
#   assertAll(
#       () -> assertEquals(0, clamp(-5, 0, 10)),
#       () -> assertEquals(10, clamp(99, 0, 10))
#   );
# pytest: just write several asserts — first failure stops the test (same as assertAll default)


def test_clamp_edges() -> None:
    assert clamp(-5, 0, 10) == 0
    assert clamp(5, 0, 10) == 5
    assert clamp(99, 0, 10) == 10


section("4. @Disabled → @pytest.mark.skip")


@pytest.mark.skip(reason="demo — same idea as @Disabled on a JUnit @Test")
def test_skipped_demo() -> None:
    assert False, "should not run"


section("5. JUnit 5 ↔ pytest quick map")

print("""
| JUnit 5                         | pytest                              |
|---------------------------------|-------------------------------------|
| @Test                           | def test_*():                       |
| assertEquals(exp, act)          | assert act == exp                   |
| assertTrue / assertFalse        | assert condition                    |
| assertNull / assertNotNull      | assert x is None / is not None      |
| assertThrows(Ex.class, ()->…)   | with pytest.raises(Ex): …           |
| assertAll(() -> …, () -> …)     | multiple assert lines in one test   |
| @BeforeEach                     | @pytest.fixture (scope="function")  |
| @BeforeAll                      | @pytest.fixture (scope="module")    |
| @ParameterizedTest + @CsvSource | @pytest.mark.parametrize            |
| @Disabled                       | @pytest.mark.skip                   |
| @DisplayName("…")               | docstring on test_* (shown in -v)   |
| @Nested inner class             | optional class grouping (rare)      |
| mvn test                        | uv run pytest                       |
""")


section("6. How to run")

print("""
uv sync --group dev
uv run pytest lesson_16/01_pytest_junit5.py -v
uv run python lesson_16/01_pytest_junit5.py
""")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"] + sys.argv[1:]))
