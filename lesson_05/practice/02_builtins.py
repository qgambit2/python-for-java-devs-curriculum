"""
Lesson 1 built-ins — extra practice (larger set).

Fill in each function, then run:
    uv run python lesson_05/practice/02_builtins.py

Uses built-ins only — no imports required.
"""
import sys
from pathlib import Path
_p = Path(__file__).resolve().parent
while not (_p / '_lesson_runner.py').is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

def top_n(values: list[int], n: int) -> list[int]:
    pass

def indexed_pairs(items: list[str]) -> list[tuple[int, str]]:
    pass

def running_totals(numbers: list[int]) -> list[int]:
    pass

def has_passing(scores: list[int], threshold: int) -> bool:
    pass

def count_passing(scores: list[int], threshold: int) -> int:
    pass

def every_other(items: list[str]) -> list[str]:
    pass

def merge_parallel(keys: list[str], values: list[int]) -> dict[str, int]:
    pass

def unique_sorted(words: list[str]) -> list[str]:
    pass

def second_largest(numbers: list[int]) -> int | None:
    pass

def sort_people(people: list[dict[str, object]]) -> list[dict[str, object]]:
    pass
# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(top_n([3, 1, 4, 1, 5], 3), [5, 4, 3], "top_n — sorted descending")
    _check(top_n([3, 1, 4, 1, 5], 0), [], "top_n — zero items requested")
    _check(top_n([3, 1, 4, 1, 5], 10), [5, 4, 3, 1, 1], "top_n — n larger than list")
    _check(top_n([], 3), [], "top_n — empty input")

    _check(indexed_pairs(["a", "b"]), [(0, "a"), (1, "b")], "indexed_pairs — enumerate pairs")
    _check(indexed_pairs([]), [], "indexed_pairs — empty")

    _check(running_totals([1, 2, 3, 4]), [1, 3, 6, 10], "running_totals — cumulative sum")
    _check(running_totals([]), [], "running_totals — empty")
    _check(running_totals([5]), [5], "running_totals — single value")

    _check(has_passing([40, 55, 90], 60), True, "has_passing — someone passed")
    _check(has_passing([40, 55, 59], 60), False, "has_passing — nobody passed")
    _check(has_passing([], 60), False, "has_passing — empty roster")

    _check(count_passing([40, 55, 90], 60), 1, "count_passing — one graduate")
    _check(count_passing([90, 91, 92], 60), 3, "count_passing — full house")
    _check(count_passing([], 60), 0, "count_passing — empty")

    _check(every_other(["a", "b", "c", "d", "e"]), ["a", "c", "e"], "every_other — stride two")
    _check(every_other(["solo"]), ["solo"], "every_other — one item")
    _check(every_other([]), [], "every_other — empty")

    _check(merge_parallel(["a", "b"], [1, 2]), {"a": 1, "b": 2}, "merge_parallel — parallel merge")
    _check(merge_parallel([], []), {}, "merge_parallel — empty")
    _check(
        merge_parallel(["a", "b", "c"], [1, 2]),
        {"a": 1, "b": 2},
        "merge_parallel — unequal lengths",
    )

    _check(
        unique_sorted(["banana", "Apple", "apple", "banana"]),
        ["Apple", "apple", "banana"],
        "unique_sorted — dedupe and sort",
    )
    _check(unique_sorted([]), [], "unique_sorted — empty")

    _check(second_largest([5, 1, 5, 3]), 3, "second_largest — distinct runner-up")
    _check(second_largest([7, 7, 7]), None, "second_largest — all same")
    _check(second_largest([42]), None, "second_largest — only one value")
    _check(second_largest([]), None, "second_largest — empty")

    people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 30}]
    _check(
        sort_people(people),
        [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 30}],
        "sort_people — lambda sort with tie-break",
    )
    _check(sort_people([]), [], "sort_people — empty")

    print("\nAll tests passed! Built-ins extra practice crushed.")


if __name__ == "__main__":
    _run_tests()
