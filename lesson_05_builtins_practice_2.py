"""
Lesson 1 built-ins — extra practice (larger set).

Fill in each function, then run:
    uv run python lesson_05_builtins_practice_2.py

Uses built-ins only — no imports required.
"""


# Exercise 1: Return the n largest values, highest first
# Example: top_n([3, 1, 4, 1, 5], 3) -> [5, 4, 3]
def top_n(values: list[int], n: int) -> list[int]:
    return sorted(values, reverse=True)[:n]


# Exercise 2: Return list of (index, value) tuples for each item
# Example: indexed_pairs(["a", "b"]) -> [(0, "a"), (1, "b")]
def indexed_pairs(items: list[str]) -> list[tuple[int, str]]:
    return list(enumerate(items))


# Exercise 3: Return running totals — each element is sum so far
# Example: running_totals([1, 2, 3, 4]) -> [1, 3, 6, 10]
def running_totals(numbers: list[int]) -> list[int]:
    # TODO: loop with accumulator, or clever sum/slicing
    list_of_totals = []
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
        list_of_totals.append(total)
    return list_of_totals

# Exercise 4: Return True if ANY score is >= threshold (use any())
# Example: has_passing([40, 55, 90], 60) -> True
def has_passing(scores: list[int], threshold: int) -> bool:
    return any(score >= threshold for score in scores)


# Exercise 5: Return how many scores are >= threshold
# Example: count_passing([40, 55, 90], 60) -> 1
def count_passing(scores: list[int], threshold: int) -> int:
    return sum(1 for score in scores if score >= threshold)


# Exercise 6: Return items at even indexes only (0, 2, 4, ...)
# Example: every_other(["a", "b", "c", "d", "e"]) -> ["a", "c", "e"]
def every_other(items: list[str]) -> list[str]:
    return items[::2]


# Exercise 7: Merge parallel lists into one dict (names -> scores)
# If lengths differ, zip uses the shorter length
# Example: merge_parallel(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
def merge_parallel(keys: list[str], values: list[int]) -> dict[str, int]:
    return dict(zip(keys, values))


# Exercise 8: Return unique words sorted alphabetically (case-sensitive)
# Example: unique_sorted(["banana", "Apple", "apple", "banana"]) -> ["Apple", "apple", "banana"]
def unique_sorted(words: list[str]) -> list[str]:
    # TODO: hint — sorted(set(words))
    return sorted(list(set(words)))


# Exercise 9: Return the second-largest distinct value, or None if impossible
# Example: second_largest([5, 1, 5, 3]) -> 3
# Example: second_largest([7, 7, 7]) -> None
# Example: second_largest([42]) -> None
def second_largest(numbers: list[int]) -> int | None:
    sorted_numbers = sorted(list(set(numbers)), reverse=True)
    if (len(sorted_numbers) < 2):
        return None
    return sorted_numbers[1]


# Exercise 10: Sort people dicts by age ascending, then by name ascending for ties
# Example: sort_people([{"name": "Bob", "age": 30}, {"name": "Alice", "age": 30}])
#          -> [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 30}]
def sort_people(people: list[dict[str, object]]) -> list[dict[str, object]]:
    return sorted(people, key=lambda p: (p["age"], p["name"]))


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
