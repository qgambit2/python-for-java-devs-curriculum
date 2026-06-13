"""
Lesson 1 — comprehensions & tuples practice.

Run:
    uv run python lesson_05/practice/03_comprehensions.py
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))



# Exercise 1: Squares of even numbers only
# even_squares([1, 2, 3, 4]) -> [4, 16]
def even_squares(nums: list[int]) -> list[int]:
    return [num*num for num in nums if num % 2 == 0]


# Exercise 2: Dict mapping each word to its length
# word_lengths(["hi", "hey"]) -> {"hi": 2, "hey": 3}
def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


# Exercise 3: Set of unique first letters (lowercase)
# first_letters(["Apple", "apricot", "Banana"]) -> {"a", "b"}
def first_letters(words: list[str]) -> set[str]:
   return {word[0].lower() for word in words}

# Exercise 4: Flatten list of lists one level
# flatten([[1, 2], [3]]) -> [1, 2, 3]
def flatten(nested: list[list[int]]) -> list[int]:
    return sum(nested, [])


# Exercise 5: Return (min, max) tuple — or (None, None) if empty
def min_max_tuple(nums: list[int]) -> tuple[int | None, int | None]:
    if not nums:
        return (None, None)
    return (min(nums), max(nums))


# Exercise 6: Swap keys and values (duplicate values: last key wins)
# invert({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
def invert(mapping: dict[str, int]) -> dict[int, str]:
    return {v:k for k,v in mapping.items()}


# Exercise 7: Names of people aged 18+ from parallel lists
# adults(["Ann", "Bob", "Cy"], [21, 16, 18]) -> ["Ann", "Cy"]
def adults(names: list[str], ages: list[int]) -> list[str]:
    return [name for name, age in zip(names, ages) if age >= 18]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(even_squares([1, 2, 3, 4]), [4, 16], "even_squares — filter + map")
    _check(even_squares([]), [], "even_squares — empty")

    _check(word_lengths(["hi", "hey"]), {"hi": 2, "hey": 3}, "word_lengths — dict comp")
    _check(word_lengths([]), {}, "word_lengths — empty")

    _check(first_letters(["Apple", "apricot", "Banana"]), {"a", "b"}, "first_letters — set comp")
    _check(first_letters([]), set(), "first_letters — empty")

    _check(flatten([[1, 2], [3]]), [1, 2, 3], "flatten — nested comp")
    _check(flatten([[], [1]]), [1], "flatten — empty inner")
    _check(flatten([]), [], "flatten — empty")

    _check(min_max_tuple([3, 1, 4]), (1, 4), "min_max_tuple — return a pair")
    _check(min_max_tuple([]), (None, None), "min_max_tuple — empty")

    _check(invert({"a": 1, "b": 2}), {1: "a", 2: "b"}, "invert — dict comp")
    _check(invert({"a": 1, "b": 1}), {1: "b"}, "invert — duplicate values")

    _check(adults(["Ann", "Bob", "Cy"], [21, 16, 18]), ["Ann", "Cy"], "adults — zip + filter")
    _check(adults([], []), [], "adults — empty")

    print("\nAll tests passed! Comprehensions practice complete.")


if __name__ == "__main__":
    _run_tests()
