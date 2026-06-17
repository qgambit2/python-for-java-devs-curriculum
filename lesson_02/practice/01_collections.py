"""
Lesson 1 — lists & dicts challenge practice.

Fill in each function, then run:
    uv run python lesson_02/practice/01_collections.py

Built-ins + list/dict methods only. No imports.
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))



# Exercise 1: Flatten one level — [[1, 2], [3]] -> [1, 2, 3]
def flatten(nested: list[list[int]]) -> list[int]:
    pass



# Exercise 2: Split items into chunks of size n (last chunk may be smaller)
# chunk(["a", "b", "c", "d", "e"], 2) -> [["a", "b"], ["c", "d"], ["e"]]
def chunk(items: list[str], size: int) -> list[list[str]]:
    pass



# Exercise 3: Rotate list right by k places (k may be larger than len)
# rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
# rotate_right([1, 2, 3], 0) -> [1, 2, 3]
# rotate_right([], 3) -> []
def rotate_right(items: list[int], k: int) -> list[int]:
    pass



# Exercise 4: Group words by their length
# group_by_length(["hi", "hey", "yo", "a"]) -> {1: ["a"], 2: ["hi", "yo"], 3: ["hey"]}
# Keys in result must be sorted ascending when converted to dict iteration order
# (build with sorted keys, or rely on insertion order from processing sorted lengths)
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    pass




# Exercise 5: Invert a dict — keys become values and values become keys
# invert({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
# If duplicate values exist, later keys win (like Java HashMap merge overwrite)
# invert({"a": 1, "b": 1}) -> {1: "b"}
def invert(mapping: dict[str, int]) -> dict[int, str]:
    pass



# Exercise 6: Merge two score dicts — add values for shared keys
# merge_scores({"alice": 10, "bob": 5}, {"bob": 3, "carol": 7})
#   -> {"alice": 10, "bob": 8, "carol": 7}
# Use right.copy() — don't mutate the caller's dict (see 04_collections.py, 06_functions.py)
# Loop: result[k] = result.get(k, 0) + v   OR one-liner with left.keys() | right.keys() (12_sets.py)
def merge_scores(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    pass




# Exercise 7: From parallel lists, keep only pairs where score >= threshold
# filter_passing(["alice", "bob", "carol"], [90, 55, 88], 60)
#   -> {"alice": 90, "carol": 88}
def filter_passing(
    pass

) -> dict[str, int]:
    if not names:
        return {}
    return {name: score for name, score in zip(names, scores) if score >= threshold}


# Exercise 8: Return top k words by frequency (highest first). Ties: alphabetical
# top_words(["bb", "aa", "bb", "cc", "aa", "aa"], 2) -> ["aa", "bb"]
def top_words(words: list[str], k: int) -> list[str]:
    pass




# Exercise 9: Transpose rows of a matrix (ragged rows OK — use zip(*rows, strict=False) in 3.10+)
# Java: nested for (col) for (row) — see faq.md § zip(*matrix)
# For this exercise, all rows have equal length.
# transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    pass


# Exercise 10: Group words that are anagrams of each other
# Return dict keyed by the sorted letters of each word, values are sorted word lists
# Key pattern: "".join(sorted(word))  — Java: Arrays.sort(word.toCharArray())
# see lesson_03/01_strings.py
# anagram_groups(["eat", "tea", "tan", "ate", "nat", "bat"])
#   -> {"aet": ["ate", "eat", "tea"], "ant": ["nat", "tan"], "abt": ["bat"]}
# (key order in dict does not matter for tests — we compare as dicts)
def anagram_groups(words: list[str]) -> dict[str, list[str]]:
    pass



# Exercise 11: Pipeline — return names whose scores improved AND final score >= 60
# Iterate after (final scores) — no separate names list needed; use before.get(name, 0)
# improved_names(
#     {"alice": 50, "bob": 70, "carol": 40},
#     {"alice": 80, "bob": 65, "carol": 55},
#     min_final=60,
# ) -> ["alice"]   # only alice improved (50->80) and final >= 60
def improved_names(
    pass

) -> list[str]:
    return [
        name
        for name, score in after.items()
        if score >= min_final and before.get(name, 0) < score
    ]



# Exercise 12: Start with defaults, overlay user values — never drop default keys
# configure({"theme": "light", "lang": "en", "notifications": True}, {"theme": "dark"})
#   -> {"theme": "dark", "lang": "en", "notifications": True}
# User can only override existing default keys; unknown user keys are ignored
# {**defaults, **user} merges dicts — see 04_collections.py + faq.md § ** dict unpacking
# Must filter: {**defaults, **{k: user[k] for k in user if k in defaults}}
def configure(defaults: dict[str, object], user: dict[str, object]) -> dict[str, object]:
    pass



# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    _check(flatten([[1, 2], [3]]), [1, 2, 3], "flatten — one level down")
    _check(flatten([[], [1], [2, 3]]), [1, 2, 3], "flatten — empty inner lists")
    _check(flatten([]), [], "flatten — nothing to flatten")

    _check(
        chunk(["a", "b", "c", "d", "e"], 2),
        [["a", "b"], ["c", "d"], ["e"]],
        "chunk — split into batches",
    )
    _check(chunk(["solo"], 3), [["solo"]], "chunk — smaller than size")
    _check(chunk([], 2), [], "chunk — empty")

    _check(rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3], "rotate_right — spin it")
    _check(rotate_right([1, 2, 3], 3), [1, 2, 3], "rotate_right — full rotation")
    _check(rotate_right([1, 2, 3], 4), [3, 1, 2], "rotate_right — k > len")
    _check(rotate_right([], 3), [], "rotate_right — empty")

    _check(
        group_by_length(["hi", "hey", "yo", "a"]),
        {1: ["a"], 2: ["hi", "yo"], 3: ["hey"]},
        "group_by_length — dict of lists",
    )
    _check(group_by_length([]), {}, "group_by_length — no words")

    _check(invert({"a": 1, "b": 2}), {1: "a", 2: "b"}, "invert — flip the map")
    _check(invert({"a": 1, "b": 1}), {1: "b"}, "invert — duplicate values, last wins")
    _check(invert({}), {}, "invert — empty map")

    _check(
        merge_scores({"alice": 10, "bob": 5}, {"bob": 3, "carol": 7}),
        {"alice": 10, "bob": 8, "carol": 7},
        "merge_scores — add shared keys",
    )
    _check(merge_scores({}, {"x": 1}), {"x": 1}, "merge_scores — from empty")

    _check(
        filter_passing(["alice", "bob", "carol"], [90, 55, 88], 60),
        {"alice": 90, "carol": 88},
        "filter_passing — zip and filter",
    )
    _check(filter_passing([], [], 0), {}, "filter_passing — empty")

    _check(top_words(["bb", "aa", "bb", "cc", "aa", "aa"], 2), ["aa", "bb"], "top_words — frequency ranking")
    _check(
        top_words(["bb", "aa", "bb", "aa"], 2),
        ["aa", "bb"],
        "top_words — frequency tie breaks alphabetically",
    )
    _check(
        top_words(["cc", "bb", "aa", "cc", "bb", "aa"], 2),
        ["aa", "bb"],
        "top_words — three-way tie, top 2 alphabetically",
    )
    _check(
        top_words(["aa", "bb", "cc", "cc"], 2),
        ["cc", "aa"],
        "top_words — frequency beats alphabetical (cc wins, then aa over bb)",
    )
    _check(top_words(["solo"], 5), ["solo"], "top_words — k > unique count")
    _check(top_words([], 3), [], "top_words — empty")

    _check(
        transpose([[1, 2, 3], [4, 5, 6]]),
        [[1, 4], [2, 5], [3, 6]],
        "transpose — zip boss defeated",
    )
    _check(transpose([[42]]), [[42]], "transpose — 1x1 matrix")
    _check(transpose([]), [], "transpose — empty matrix")

    groups = anagram_groups(["eat", "tea", "tan", "ate", "nat", "bat"])
    _check(
        groups,
        {"aet": ["ate", "eat", "tea"], "ant": ["nat", "tan"], "abt": ["bat"]},
        "anagram_groups — sorted-letter keys",
    )
    _check(anagram_groups([]), {}, "anagram_groups — empty")

    _check(
        improved_names(
            {"alice": 50, "bob": 70, "carol": 40},
            {"alice": 80, "bob": 65, "carol": 55},
            min_final=60,
        ),
        ["alice"],
        "improved_names — pipeline logic",
    )
    _check(
        improved_names(
            {"alice": 50, "bob": 70, "dave": 90},
            {"alice": 80, "bob": 65},
            min_final=60,
        ),
        ["alice"],
        "improved_names — dave only in before, bob score dropped",
    )
    _check(improved_names({}, {}, 0), [], "improved_names — empty")

    defaults = {"theme": "light", "lang": "en", "notifications": True}
    _check(
        configure(defaults, {"theme": "dark"}),
        {"theme": "dark", "lang": "en", "notifications": True},
        "configure — overlay user prefs",
    )
    _check(
        configure(defaults, {"theme": "dark", "hacker": True}),
        {"theme": "dark", "lang": "en", "notifications": True},
        "configure — ignore unknown keys",
    )

    print("\nAll tests passed! Collections challenge conquered.")


if __name__ == "__main__":
    _run_tests()
