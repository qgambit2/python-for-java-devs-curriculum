"""
Lesson 1 practice — YOUR turn.

Fill in each function below, then run:
    uv run python lesson_01/practice/01_practice.py

We'll review your answers together in chat.
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: Return a sentence like "My name is Alex and my favorite number is 7"
def introduce(name: str, favorite_number: int) -> str:
    return f"My name is {name} and my favorite number is {favorite_number}"


# Exercise 2: Return True if the number is even (hint: % operator works like Java)
def is_even(n: int) -> bool:
    return n % 2 == 0


# Exercise 3: Return the sum of all numbers in the list
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)



# Exercise 4: Return a dict counting how many times each word appears
# Example: count_words(["a", "b", "a"]) -> {"a": 2, "b": 1}
def count_words(words: list[str]) -> dict[str, int]:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts;



# ---------------------------------------------------------------------------
# Tests — run the file to check your work (don't edit below this line)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(
        introduce("Alex", 7),
        "My name is Alex and my favorite number is 7",
        "introduce — f-string pro",
    )
    _check(is_even(4), True, "is_even — four is even")
    _check(is_even(7), False, "is_even — seven stands firm")
    _check(sum_list([1, 2, 3, 4]), 10, "sum_list — adds up")
    _check(sum_list([]), 0, "sum_list — empty sums to zero")
    _check(count_words(["a", "b", "a"]), {"a": 2, "b": 1}, "count_words — frequency map")
    _check(count_words([]), {}, "count_words — empty input")
    print("\nAll tests passed! Core Lesson 1 practice complete.")


if __name__ == "__main__":
    _run_tests()
