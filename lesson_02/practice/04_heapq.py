"""
Lesson 2 — heapq practice.

Fill in each function, then run:
    uv run python lesson_02/practice/04_heapq.py

import heapq only (stdlib min-heap).
"""

from __future__ import annotations

import heapq
import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: k smallest values (ascending order in result)
# k_smallest([5, 1, 9, 2, 7], 3) -> [1, 2, 5]
def k_smallest(nums: list[int], k: int) -> list[int]:
    pass


# Exercise 2: k largest values (descending order in result)
# k_largest([5, 1, 9, 2, 7], 2) -> [9, 7]
def k_largest(nums: list[int], k: int) -> list[int]:
    pass


# Exercise 3: Pop all items from a min-heap in sorted (ascending) order
# drain_heap([3, 1, 4]) -> [1, 3, 4]  — heapify, then repeated heappop
def drain_heap(nums: list[int]) -> list[int]:
    pass


# Exercise 4: Merge two sorted lists into one sorted list — heapq.merge
# merge_sorted([1, 4, 7], [2, 3, 8]) -> [1, 2, 3, 4, 7, 8]
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    pass


# Exercise 5: Highest score wins — max-heap via negation
# top_score([45, 90, 72]) -> 90
def top_score(scores: list[int]) -> int:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------

from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(k_smallest([5, 1, 9, 2, 7], 3), [1, 2, 5], "k_smallest")
    _check(k_smallest([1, 2, 3], 5), [1, 2, 3], "k_smallest — k > len")
    _check(k_smallest([], 2), [], "k_smallest — empty")

    _check(k_largest([5, 1, 9, 2, 7], 2), [9, 7], "k_largest")
    _check(k_largest([3], 1), [3], "k_largest — one")

    _check(drain_heap([3, 1, 4]), [1, 3, 4], "drain_heap")
    _check(drain_heap([]), [], "drain_heap — empty")

    _check(merge_sorted([1, 4, 7], [2, 3, 8]), [1, 2, 3, 4, 7, 8], "merge_sorted")
    _check(merge_sorted([], [1, 2]), [1, 2], "merge_sorted — one empty")

    _check(top_score([45, 90, 72]), 90, "top_score — max via negation")
    _check(top_score([5]), 5, "top_score — single")

    print("\nAll tests passed! heapq practice complete.")


if __name__ == "__main__":
    _run_tests()
