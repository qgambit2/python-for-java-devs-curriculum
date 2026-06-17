"""
Lesson 2 — __eq__ / __hash__ practice (≈ Java equals / hashCode).

Contract (same as Java equals/hashCode): if a == b then hash(a) == hash(b).
  == uses __eq__ only; hash() uses __hash__ only; set/dict keys use BOTH.
  See lesson §3, §3a-bis, §7 (BrokenEq).

Read:
    lesson_08/07_eq_and_hash.py

Fill in each TODO, then run:
    uv run python lesson_08/practice/02_eq_hash.py
"""
import sys
from pathlib import Path
_p = Path(__file__).resolve().parent
while not (_p / '_lesson_runner.py').is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))
from dataclasses import dataclass

class Point2D:

    def __init__(self, x: int, y: int) -> None:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __repr__(self) -> str:
        return f'Point2D({self.x}, {self.y})'

def unique_point_count(points: list[Point2D]) -> int:
    pass

class PlayingCard:

    def __init__(self, rank: str, suit: str) -> None:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

def count_cards(cards: list[PlayingCard]) -> dict[PlayingCard, int]:
    pass

def same_object(a: object, b: object) -> bool:
    pass

class MutableVec:

    def __init__(self, x: int, y: int) -> None:
        pass

    def __eq__(self, other: object) -> bool:
        pass

def is_hashable(obj: object) -> bool:
    pass

@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

def tag_count(colors: list[Color]) -> dict[Color, int]:
    pass
# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check, check_eq


def _run_tests() -> None:
    p1 = Point2D(1, 2)
    p2 = Point2D(1, 2)
    p3 = Point2D(3, 4)
    check(p1 == p2, "Point2D.__eq__ — equal coordinates")
    check(p1 != p3, "Point2D.__eq__ — different coordinates")
    check(hash(p1) == hash(p2), "Point2D.__hash__ — equal objects same hash")
    check_eq(unique_point_count([p1, p3, p2]), 2, "unique_point_count — set dedupe")

    ace = PlayingCard("A", "spades")
    ace2 = PlayingCard("A", "spades")
    king = PlayingCard("K", "hearts")
    check(ace == ace2, "PlayingCard.__eq__")
    check(hash(ace) == hash(ace2), "PlayingCard.__hash__")
    counts = count_cards([ace, ace2, king])
    check_eq(len(counts), 2, "count_cards — two distinct keys")
    check_eq(counts[ace], 2, "count_cards — ace appears twice")
    check_eq(counts[king], 1, "count_cards — king once")

    lst = [1, 2, 3]
    check(same_object(lst, lst), "same_object — same reference")
    check(not same_object(lst, [1, 2, 3]), "same_object — equal but not same")

    mv1 = MutableVec(1, 2)
    mv2 = MutableVec(1, 2)
    check(mv1 == mv2, "MutableVec.__eq__ — value equal")
    check(not is_hashable(mv1), "MutableVec — unhashable without __hash__")
    check(is_hashable(p1), "Point2D — hashable")

    red = Color(255, 0, 0)
    blue = Color(0, 0, 255)
    tc = tag_count([red, blue, red])
    check_eq(tc[red], 2, "tag_count — frozen dataclass as dict key")
    check_eq(tc[blue], 1, "tag_count — blue once")

    print("\nAll tests passed! __eq__ / __hash__ practice complete.")


if __name__ == "__main__":
    _run_tests()
