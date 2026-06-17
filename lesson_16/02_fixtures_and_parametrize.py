"""Lesson 16b — fixtures & @ParameterizedTest (JUnit 5 ↔ pytest).

@Run:
    uv run python lesson_16/02_fixtures_and_parametrize.py
    uv run pytest lesson_16/02_fixtures_and_parametrize.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _code_under_test import ScoreBoard, add


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. @BeforeEach → @pytest.fixture")

print(r"""
JUnit 5:

    class ScoreBoardTest {
        private ScoreBoard board;

        @BeforeEach
        void setUp() {
            board = new ScoreBoard();
            board.add("alice", 10);
        }

        @Test
        void aliceScore() {
            assertEquals(10, board.get("alice"));
        }
    }

pytest:

    @pytest.fixture
    def board():
        b = ScoreBoard()
        b.add("alice", 10)
        return b

    def test_alice_score(board):
        assert board.get("alice") == 10
""")


@pytest.fixture
def board() -> ScoreBoard:
    """Fresh ScoreBoard — like @BeforeEach setUp()."""
    b = ScoreBoard()
    b.add("alice", 10)
    return b


def test_alice_score(board: ScoreBoard) -> None:
    assert board.get("alice") == 10


def test_board_is_isolated(board: ScoreBoard) -> None:
    """scope=function (default): each test gets its own board."""
    board.add("bob", 5)
    assert board.get("bob") == 5
    assert board.get("alice") == 10


section("1. @ParameterizedTest + @CsvSource")

print(r"""
JUnit 5:

    @ParameterizedTest
    @CsvSource({"2, 3, 5", "0, 0, 0", "-1, 1, 0"})
    void add(int a, int b, int want) {
        assertEquals(want, add(a, b));
    }
""")


@pytest.mark.parametrize(
    "a,b,want",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_add_parametrized(a: int, b: int, want: int) -> None:
    assert add(a, b) == want


@pytest.mark.parametrize(
    "names,points,expected_top",
    [
        (["alice", "bob", "alice"], [10, 5, 3], [("alice", 13), ("bob", 5)]),
    ],
)
def test_scoreboard_top(
    names: list[str], points: list[int], expected_top: list[tuple[str, int]]
) -> None:
    board = ScoreBoard()
    for name, pts in zip(names, points, strict=True):
        board.add(name, pts)
    assert board.top(2) == expected_top


section("2. @BeforeAll → fixture scope module / session")

print("""
| JUnit 5     | pytest                          |
|-------------|---------------------------------|
| @BeforeEach | @pytest.fixture()               |
| @BeforeAll  | @pytest.fixture(scope="module") |
| @AfterEach  | yield fixture — code after yield runs teardown |
""")


_module_tokens: list[str] = []


@pytest.fixture(scope="module")
def module_token() -> str:
    """One token per test module — like @BeforeAll static setup."""
    token = f"module-{len(_module_tokens) + 1}"
    _module_tokens.append(token)
    return token


def test_module_token_a(module_token: str) -> None:
    assert module_token.startswith("module-")


def test_module_token_same_for_module(module_token: str) -> None:
    assert module_token == _module_tokens[0]


@pytest.fixture
def board_with_teardown() -> ScoreBoard:
    """yield fixture ≈ @BeforeEach + @AfterEach in one."""
    b = ScoreBoard()
    b.add("carol", 1)
    yield b
    # teardown would run here (close files, rollback DB, etc.)
    b.add("_teardown", 0)


def test_carol_before_teardown(board_with_teardown: ScoreBoard) -> None:
    assert board_with_teardown.get("carol") == 1


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"] + sys.argv[1:]))
