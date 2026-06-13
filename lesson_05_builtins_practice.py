"""
Lesson 1 built-ins practice.

Fill in each function, then run:
    uv run python lesson_05_builtins_practice.py
"""


# Exercise 1: Return a list of even numbers from 0 up to (but not including) n
# Example: evens_up_to(6) -> [0, 2, 4]
def evens_up_to(n: int) -> list[int]:
    return list(range(0, n, 2))


# Exercise 2: Return the index of the highest score, or -1 if list is empty
# Example: index_of_max([40, 90, 55]) -> 1
def index_of_max(scores: list[int]) -> int:
    if not scores:
        return -1
    return scores.index(max(scores))


# Exercise 3: Return a dict pairing each name with its score using zip
# Example: pair_names_scores(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
def pair_names_scores(names: list[str], scores: list[int]) -> dict[str, int]:
    return dict(zip(names, scores))


# Exercise 4: Return True if ALL strings have length >= min_length
# Example: all_long_enough(["hi", "hey"], 2) -> True
def all_long_enough(words: list[str], min_length: int) -> bool:
    return all(len(word) >= min_length for word in words)


# Exercise 5: Return a list of "index:value" strings using enumerate
# Example: with_indexes(["a", "b"]) -> ["0:a", "1:b"]
def with_indexes(items: list[str]) -> list[str]:
    return [f"{index}:{value}" for index, value in enumerate(items)]


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(evens_up_to(6), [0, 2, 4], "evens_up_to(6) — nice range work")
    _check(evens_up_to(7), [0, 2, 4, 6], "evens_up_to(7) — upper bound nailed")
    _check(evens_up_to(2), [0], "evens_up_to(2) — small inputs count")
    _check(evens_up_to(1), [0], "evens_up_to(1) — zero is even!")
    _check(evens_up_to(0), [], "evens_up_to(0) — empty edge case")

    _check(index_of_max([40, 90, 55]), 1, "index_of_max — found the winner")
    _check(index_of_max([5]), 0, "index_of_max — index 0 is valid")
    _check(index_of_max([]), -1, "index_of_max — empty list guarded")
    _check(index_of_max([90, 40, 90]), 0, "index_of_max — ties handled")

    _check(pair_names_scores(["a", "b"], [1, 2]), {"a": 1, "b": 2}, "pair_names_scores — zip magic")
    _check(pair_names_scores([], []), {}, "pair_names_scores — empty zip")
    _check(
        pair_names_scores(["a", "b", "c"], [1, 2]),
        {"a": 1, "b": 2},
        "pair_names_scores — shorter list wins",
    )

    _check(all_long_enough(["hi", "hey"], 2), True, "all_long_enough — all pass")
    _check(all_long_enough(["hi", "x"], 2), False, "all_long_enough — one failure")
    _check(all_long_enough([], 1), True, "all_long_enough — empty is vacuously true")
    _check(all_long_enough(["a"], 0), True, "all_long_enough — zero min length")

    _check(with_indexes(["a", "b"]), ["0:a", "1:b"], "with_indexes — enumerate rocks")
    _check(with_indexes(["only"]), ["0:only"], "with_indexes — solo item")
    _check(with_indexes([]), [], "with_indexes — empty list")

    print("\nAll tests passed! Lesson 1 built-ins practice complete.")


if __name__ == "__main__":
    _run_tests()
