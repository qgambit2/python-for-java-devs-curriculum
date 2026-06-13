"""
Lesson 1 — collections challenge practice (round 2).

New scenarios, same patterns: zip, comprehensions, sorted key=, setdefault,
{**merge}, .copy(), | on keys, zip(*matrix), tuple sort keys.

Fill in each function, then run:
    uv run python lesson_02_collections_practice_2.py

Built-ins + list/dict methods only. No imports.
"""


# Exercise 1: Remove duplicates, keep first-seen order
# dedupe_ordered(["b", "a", "b", "c", "a"]) -> ["b", "a", "c"]
def dedupe_ordered(items: list[str]) -> list[str]:
    pass


# Exercise 2: Parallel lists to dict (you've done this before — make it automatic)
# zip_to_dict(["alice", "bob"], [95, 87]) -> {"alice": 95, "bob": 87}
def zip_to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
    pass


# Exercise 3: Per-key maximum of two score maps — new dict, don't mutate inputs
# merge_max({"alice": 10, "bob": 5}, {"bob": 8, "carol": 3})
#   -> {"alice": 10, "bob": 8, "carol": 3}
def merge_max(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    pass


# Exercise 4: Names whose score CHANGED between before and after (iterate after)
# Compare with before.get(name, 0). Return names sorted alphabetically.
# score_changes({"alice": 50, "bob": 70}, {"alice": 50, "bob": 65, "carol": 40})
#   -> ["bob", "carol"]
def score_changes(
    before: dict[str, int], after: dict[str, int]
) -> list[str]:
    pass


# Exercise 5: Keep only keys from allowlist that exist in data (preserve allowlist order)
# pick_keys({"a": 1, "b": 2, "c": 3}, ["c", "a", "z"])
#   -> {"c": 3, "a": 1}
def pick_keys(data: dict[str, int], allowlist: list[str]) -> dict[str, int]:
    pass


# Exercise 6: Group words by first letter (case-insensitive); words in each group sorted
# group_by_first_letter(["Banana", "apple", "apricot", "cherry"])
#   -> {"a": ["apple", "apricot"], "b": ["Banana"], "c": ["cherry"]}
def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    pass


# Exercise 7: Rotate list LEFT by k (k may exceed len; 0 or full turn -> unchanged)
# rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
def rotate_left(items: list[int], k: int) -> list[int]:
    pass


# Exercise 8: k rarest words — lowest frequency first; ties: alphabetical
# rare_words(["cc", "bb", "aa", "bb", "cc"], 2) -> ["aa", "bb"]
# rare_words(["aa", "bb", "cc", "cc"], 2) -> ["aa", "bb"]  (cc not taken — higher freq)
def rare_words(words: list[str], k: int) -> list[str]:
    pass


# Exercise 9: Sum each row of a matrix
# sum_rows([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
def sum_rows(matrix: list[list[int]]) -> list[int]:
    pass


# Exercise 10: Character frequency in a string (ignore spaces)
# char_counts("hello world") -> {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
def char_counts(text: str) -> dict[str, int]:
    pass


# Exercise 11: Names whose score WENT DOWN (iterate after; before.get(name, 0) > after score)
# slipped_names({"alice": 80, "bob": 70}, {"alice": 90, "bob": 65}) -> ["bob"]
def slipped_names(before: dict[str, int], after: dict[str, int]) -> list[str]:
    pass


# Exercise 12: Overlay user onto defaults — unknown user keys ignored (configure pattern)
# merge_defaults(
#     {"theme": "light", "lang": "en", "notifications": True},
#     {"theme": "dark", "hacker": True},
# ) -> {"theme": "dark", "lang": "en", "notifications": True}
def merge_defaults(
    defaults: dict[str, object], user: dict[str, object]
) -> dict[str, object]:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(dedupe_ordered(["b", "a", "b", "c", "a"]), ["b", "a", "c"], "dedupe_ordered — keep first")
    _check(dedupe_ordered([]), [], "dedupe_ordered — empty")
    _check(dedupe_ordered(["solo"]), ["solo"], "dedupe_ordered — one item")

    _check(
        zip_to_dict(["alice", "bob"], [95, 87]),
        {"alice": 95, "bob": 87},
        "zip_to_dict — parallel lists",
    )
    _check(zip_to_dict([], []), {}, "zip_to_dict — empty")

    _check(
        merge_max({"alice": 10, "bob": 5}, {"bob": 8, "carol": 3}),
        {"alice": 10, "bob": 8, "carol": 3},
        "merge_max — per-key max",
    )
    _check(merge_max({}, {"x": 1}), {"x": 1}, "merge_max — from empty")

    _check(
        score_changes({"alice": 50, "bob": 70}, {"alice": 50, "bob": 65, "carol": 40}),
        ["bob", "carol"],
        "score_changes — new or different",
    )
    _check(score_changes({"a": 1}, {"a": 1}), [], "score_changes — no changes")
    _check(score_changes({}, {}), [], "score_changes — empty")

    _check(
        pick_keys({"a": 1, "b": 2, "c": 3}, ["c", "a", "z"]),
        {"c": 3, "a": 1},
        "pick_keys — allowlist order",
    )
    _check(pick_keys({}, ["a"]), {}, "pick_keys — empty data")

    _check(
        group_by_first_letter(["Banana", "apple", "apricot", "cherry"]),
        {"a": ["apple", "apricot"], "b": ["Banana"], "c": ["cherry"]},
        "group_by_first_letter — case insensitive",
    )
    _check(group_by_first_letter([]), {}, "group_by_first_letter — empty")

    _check(rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2], "rotate_left — spin it")
    _check(rotate_left([1, 2, 3], 3), [1, 2, 3], "rotate_left — full rotation")
    _check(rotate_left([1, 2, 3], 4), [2, 3, 1], "rotate_left — k > len")
    _check(rotate_left([], 3), [], "rotate_left — empty")

    _check(rare_words(["cc", "bb", "aa", "bb", "cc"], 2), ["aa", "bb"], "rare_words — lowest freq")
    _check(
        rare_words(["aa", "bb", "cc", "cc"], 2),
        ["aa", "bb"],
        "rare_words — skip higher freq",
    )
    _check(rare_words([], 3), [], "rare_words — empty")

    _check(sum_rows([[1, 2, 3], [4, 5, 6]]), [6, 15], "sum_rows — row totals")
    _check(sum_rows([]), [], "sum_rows — empty matrix")
    _check(sum_rows([[42]]), [42], "sum_rows — single cell")

    _check(
        char_counts("hello world"),
        {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
        "char_counts — ignore spaces",
    )
    _check(char_counts(""), {}, "char_counts — empty string")
    _check(char_counts("aaa"), {"a": 3}, "char_counts — repeated")

    _check(
        slipped_names({"alice": 80, "bob": 70}, {"alice": 90, "bob": 65}),
        ["bob"],
        "slipped_names — score dropped",
    )
    _check(slipped_names({"a": 1}, {"a": 2}), [], "slipped_names — improved only")
    _check(slipped_names({}, {}), [], "slipped_names — empty")

    _check(
        merge_defaults(
            {"theme": "light", "lang": "en", "notifications": True},
            {"theme": "dark"},
        ),
        {"theme": "dark", "lang": "en", "notifications": True},
        "merge_defaults — overlay",
    )
    _check(
        merge_defaults(
            {"theme": "light", "lang": "en", "notifications": True},
            {"theme": "dark", "hacker": True},
        ),
        {"theme": "dark", "lang": "en", "notifications": True},
        "merge_defaults — ignore unknown keys",
    )

    print("\nAll tests passed! Collections round 2 complete.")


if __name__ == "__main__":
    _run_tests()
