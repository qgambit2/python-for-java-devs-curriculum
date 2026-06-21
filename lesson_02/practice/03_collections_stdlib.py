"""
Lesson 2 — stdlib collections practice (round 3).

Uses types from lesson_02/03_collections_stdlib.py:
  defaultdict, Counter, deque, OrderedDict, namedtuple, ChainMap, UserDict, UserList, UserString

Fill in each function (and class methods), then run:
    uv run python lesson_02/practice/03_collections_stdlib.py

Allowed imports: collections module only (plus typing if you like).
"""

from __future__ import annotations

import sys
from collections import (
    ChainMap,
    Counter,
    OrderedDict,
    UserDict,
    UserList,
    UserString,
    defaultdict,
    deque,
    namedtuple,
)
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: Group words by sorted letters (anagram buckets) — defaultdict(list)
# group_anagrams(["eat", "tea", "tan"]) -> {"aet": ["eat", "tea"], "ant": ["tan"]}
# Return a plain dict (convert before return if you use defaultdict).
def group_anagrams(words: list[str]) -> dict[str, list[str]]:
    pass


# Exercise 2: Count page hits — defaultdict(int)
# page_hits(["/", "/home", "/", "/about"]) -> {"/": 2, "/home": 1, "/about": 1}
def page_hits(pages: list[str]) -> dict[str, int]:
    pass


# Exercise 3: Word frequencies — Counter
# word_freq(["a", "b", "a", "c", "b", "a"]) -> {"a": 3, "b": 2, "c": 1}
def word_freq(words: list[str]) -> dict[str, int]:
    pass


# Exercise 4: Top n words by frequency — Counter.most_common
# top_n_words(["x", "y", "x", "z", "y", "x"], 2) -> ["x", "y"]
def top_n_words(words: list[str], n: int) -> list[str]:
    pass


# Exercise 5: Letters in a more often than in b — Counter subtraction
# extra_letters("aab", "ab") -> {"a": 1}
# extra_letters("abc", "abc") -> {}
def extra_letters(a: str, b: str) -> dict[str, int]:
    pass


# Exercise 6: Last n items seen — deque(maxlen=...)
# tail([1, 2, 3, 4, 5], 3) -> [3, 4, 5]
# tail([1, 2], 5) -> [1, 2]
def tail(items: list[int], n: int) -> list[int]:
    pass


# Exercise 7: Palindrome check using deque popleft + pop (ignore case)
# is_palindrome_deque("Racecar") -> True
# is_palindrome_deque("ab") -> False
def is_palindrome_deque(text: str) -> bool:
    pass


# Exercise 8: After touching keys in order, return OrderedDict key order
# keys_after_access([("a", 1), ("b", 2), ("c", 3)], ["a", "c"])
#   -> ["b", "a", "c"]  — a and c promoted to tail in order
def keys_after_access(
    pairs: list[tuple[str, int]], access: list[str]
) -> list[str]:
    pass


# Exercise 9: FIFO-evict n oldest entries from OrderedDict; return remaining keys
# fifo_evict([("a", 1), ("b", 2), ("c", 3)], 2) -> ["c"]
def fifo_evict(pairs: list[tuple[str, int]], evict_n: int) -> list[str]:
    pass


# Exercise 10: Parse "x,y" into a namedtuple Point(x, y)
Point = namedtuple("Point", ["x", "y"])


def parse_point(text: str) -> Point:
    pass


# Exercise 11: Layered config lookup — ChainMap(overrides, defaults)
# config_lookup({"theme": "light"}, {"theme": "dark", "lang": "en"}, "lang") -> "en"
# config_lookup({"theme": "light"}, {"theme": "dark"}, "theme") -> "dark"
def config_lookup(
    defaults: dict[str, str], overrides: dict[str, str], key: str
) -> str | None:
    pass


# Exercise 12: Case-insensitive dict — UserDict subclass
class InsensitiveDict(UserDict):
    """Store and read keys case-insensitively (normalize to lower)."""

    def __setitem__(self, key: str, value: int) -> None:
        pass

    def __getitem__(self, key: str) -> int:
        pass


def merge_scores_insensitive(
    scores: InsensitiveDict, player: str, points: int
) -> None:
    """Add points to player (case-insensitive key)."""
    pass


# Exercise 13: Double each item in order — UserList
def double_items(items: list[int]) -> list[int]:
    """Return [1,1,2,2,3,3] for input [1,2,3] using UserList."""
    pass


# Exercise 14: Center a title — UserString subclass
class PaddedTitle(UserString):
    """UserString wrapper with a center(width) helper."""

    def center_in(self, width: int) -> str:
        pass


def banner(title: str, width: int) -> str:
    return PaddedTitle(title).center_in(width)


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------

from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(
        group_anagrams(["eat", "tea", "tan"]),
        {"aet": ["eat", "tea"], "ant": ["tan"]},
        "group_anagrams — defaultdict list",
    )
    _check(group_anagrams([]), {}, "group_anagrams — empty")

    _check(
        page_hits(["/", "/home", "/", "/about"]),
        {"/": 2, "/home": 1, "/about": 1},
        "page_hits — defaultdict int",
    )
    _check(page_hits([]), {}, "page_hits — empty")

    _check(
        word_freq(["a", "b", "a", "c", "b", "a"]),
        {"a": 3, "b": 2, "c": 1},
        "word_freq — Counter",
    )
    _check(word_freq([]), {}, "word_freq — empty")

    _check(
        top_n_words(["x", "y", "x", "z", "y", "x"], 2),
        ["x", "y"],
        "top_n_words — most_common",
    )
    _check(top_n_words(["solo"], 3), ["solo"], "top_n_words — fewer than n")

    _check(extra_letters("aab", "ab"), {"a": 1}, "extra_letters — multiset diff")
    _check(extra_letters("abc", "abc"), {}, "extra_letters — equal")

    _check(tail([1, 2, 3, 4, 5], 3), [3, 4, 5], "tail — deque maxlen")
    _check(tail([1, 2], 5), [1, 2], "tail — n larger than len")
    _check(tail([], 3), [], "tail — empty")

    _check(is_palindrome_deque("Racecar"), True, "is_palindrome_deque — yes")
    _check(is_palindrome_deque("ab"), False, "is_palindrome_deque — no")
    _check(is_palindrome_deque("a"), True, "is_palindrome_deque — single")

    _check(
        keys_after_access([("a", 1), ("b", 2), ("c", 3)], ["a", "c"]),
        ["b", "a", "c"],
        "keys_after_access — move_to_end",
    )
    _check(
        keys_after_access([("x", 1)], ["missing"]),
        ["x"],
        "keys_after_access — missing touch ignored",
    )

    _check(
        fifo_evict([("a", 1), ("b", 2), ("c", 3)], 2),
        ["c"],
        "fifo_evict — popitem last=False",
    )
    _check(fifo_evict([("a", 1)], 0), ["a"], "fifo_evict — evict zero")
    _check(fifo_evict([], 1), [], "fifo_evict — empty")

    _check(parse_point("3, 4"), Point(3, 4), "parse_point — namedtuple")
    _check(parse_point("-1,0"), Point(-1, 0), "parse_point — negatives")

    _check(
        config_lookup({"theme": "light", "lang": "en"}, {"theme": "dark"}, "lang"),
        "en",
        "config_lookup — falls through to defaults",
    )
    _check(
        config_lookup({"theme": "light"}, {"theme": "dark"}, "theme"),
        "dark",
        "config_lookup — override wins",
    )
    _check(
        config_lookup({"a": "1"}, {}, "missing"),
        None,
        "config_lookup — missing key",
    )

    book = InsensitiveDict()
    merge_scores_insensitive(book, "Alice", 10)
    merge_scores_insensitive(book, "alice", 5)
    merge_scores_insensitive(book, "BOB", 3)
    _check(book["alice"], 15, "InsensitiveDict — same key any case")
    _check(book["bob"], 3, "InsensitiveDict — read lower")

    _check(double_items([1, 2, 3]), [1, 1, 2, 2, 3, 3], "double_items — UserList")
    _check(double_items([]), [], "double_items — empty")

    _check(banner("hi", 6), "  hi  ", "banner — UserString center")
    _check(banner("go", 2), "go", "banner — already fits")

    print("\nAll tests passed! Collections stdlib practice complete.")


if __name__ == "__main__":
    _run_tests()
