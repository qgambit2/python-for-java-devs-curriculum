"""
Lesson 3 — string operations practice.

Read:
    lesson_03/01_strings.py  (sections 12–20)

Fill in each function, then run:
    uv run python lesson_03/practice/02_string_ops.py

Built-in str methods; `import re` allowed for exercises 11–12.
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: Split on comma, strip each field
# parse_fields("a, b , c") -> ["a", "b", "c"]
def parse_fields(line: str) -> list[str]:
    pass


# Exercise 2: Collapse any run of whitespace to single spaces; trim ends
# collapse_whitespace("  hello   world  ") -> "hello world"
def collapse_whitespace(text: str) -> str:
    pass


# Exercise 3: Count non-overlapping occurrences of sub in text
# count_substring("mississippi", "iss") -> 2
def count_substring(text: str, sub: str) -> int:
    pass


# Exercise 4: Per-character counts; skip spaces (uses .count — see lesson §19)
# char_counts("hello world") -> {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
def char_counts(text: str) -> dict[str, int]:
    pass


# Exercise 5: True if filename ends with .py (case-sensitive)
def is_python_file(filename: str) -> bool:
    pass


# Exercise 6: Replace every space with a dash
# dash_case("hello world") -> "hello-world"
def dash_case(text: str) -> str:
    pass


# Exercise 7: First whitespace-delimited token; empty string if text is blank/whitespace
# first_token("  foo bar  ") -> "foo"
def first_token(text: str) -> str:
    pass


# Exercise 8: Number of words — whitespace-separated tokens; "" -> 0
# word_count("one two three") -> 3
def word_count(text: str) -> int:
    pass


# Exercise 9: Slice out the file extension without the dot; "" if no dot
# extension("report.csv") -> "csv"
def extension(filename: str) -> str:
    pass


# Exercise 10: Case-insensitive membership — use .lower() on both sides
# contains_ignore_case("Hello World", "WORLD") -> True
def contains_ignore_case(text: str, needle: str) -> bool:
    pass


# Exercise 11: All digit runs — re.findall (see lesson §20)
# extract_numbers("a1b22c3") -> ["1", "22", "3"]
def extract_numbers(text: str) -> list[str]:
    pass


# Exercise 12: Remove every digit — re.sub
# strip_digits("a1b2c") -> "abc"
def strip_digits(text: str) -> str:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq


def _run_tests() -> None:
    check_eq(parse_fields("a, b , c"), ["a", "b", "c"], "parse_fields")
    check_eq(parse_fields("solo"), ["solo"], "parse_fields — one field")
    check_eq(parse_fields(" x , y "), ["x", "y"], "parse_fields — edge spaces")

    check_eq(
        collapse_whitespace("  hello   world  "),
        "hello world",
        "collapse_whitespace",
    )
    check_eq(collapse_whitespace("one"), "one", "collapse_whitespace — no extra spaces")
    check_eq(collapse_whitespace("   "), "", "collapse_whitespace — blank")

    check_eq(count_substring("hello", "l"), 2, "count_substring — letter")
    check_eq(count_substring("mississippi", "iss"), 2, "count_substring — overlap")
    check_eq(count_substring("abc", "z"), 0, "count_substring — missing")

    check_eq(
        char_counts("hello world"),
        {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
        "char_counts — skip spaces",
    )
    check_eq(char_counts(""), {}, "char_counts — empty")
    check_eq(char_counts("aaa"), {"a": 3}, "char_counts — repeated")

    check_eq(is_python_file("main.py"), True, "is_python_file — match")
    check_eq(is_python_file("main.PY"), False, "is_python_file — case")
    check_eq(is_python_file("readme.md"), False, "is_python_file — other ext")

    check_eq(dash_case("hello world"), "hello-world", "dash_case")
    check_eq(dash_case("already"), "already", "dash_case — no spaces")

    check_eq(first_token("  foo bar  "), "foo", "first_token")
    check_eq(first_token("solo"), "solo", "first_token — one word")
    check_eq(first_token("   "), "", "first_token — blank")

    check_eq(word_count("one two three"), 3, "word_count")
    check_eq(word_count(""), 0, "word_count — empty")
    check_eq(word_count("   "), 0, "word_count — whitespace only")

    check_eq(extension("report.csv"), "csv", "extension")
    check_eq(extension("archive.tar.gz"), "gz", "extension — last segment")
    check_eq(extension("noext"), "", "extension — none")

    check_eq(
        contains_ignore_case("Hello World", "WORLD"),
        True,
        "contains_ignore_case",
    )
    check_eq(
        contains_ignore_case("Hello World", "planet"),
        False,
        "contains_ignore_case — missing",
    )

    check_eq(extract_numbers("a1b22c3"), ["1", "22", "3"], "extract_numbers")
    check_eq(extract_numbers("no digits"), [], "extract_numbers — empty")

    check_eq(strip_digits("a1b2c"), "abc", "strip_digits")
    check_eq(strip_digits("hello"), "hello", "strip_digits — none")

    print("\nAll tests passed! String operations practice complete.")


if __name__ == "__main__":
    _run_tests()
