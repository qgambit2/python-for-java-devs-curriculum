"""
Lesson 1 — string formatting practice.

Read:
    lesson_03/01_strings.py

Fill in each TODO, then run:
    uv run python lesson_03/practice/01_strings.py
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))



# Exercise 1: greet — f"Hello, {name}!"
def greet(name: str) -> str:
    # TODO
    pass


# Exercise 2: money — two decimal places, dollar sign
# money(12.5) → "$12.50"   (Java: String.format("$%.2f", amount))
def money(amount: float) -> str:
    # TODO
    pass


# Exercise 3: score_line — name left-aligned in 10 chars, score right-aligned in 4
# score_line("Alice", 95) → "Alice          95"
def score_line(name: str, score: int) -> str:
    # TODO: f"{name:<10}{score:>4}"
    pass


# Exercise 4: hex_byte — uppercase hex with 0x prefix
# hex_byte(255) → "0xFF"   (hint: f"0x{n:02X}")
def hex_byte(n: int) -> str:
    # TODO
    pass


# Exercise 5: join_tags — comma-separated from list
# join_tags(["a", "b", "c"]) → "a, b, c"
def join_tags(tags: list[str]) -> str:
    # TODO: ", ".join(tags)
    pass


# Exercise 6: legacy_line — use % formatting (older style, still readable in logs)
# legacy_line("Bob", 7) → "Bob has 7 items"
def legacy_line(name: str, count: int) -> str:
    # TODO: "%s has %d items" % (name, count)
    pass


# Exercise 7: format_template — str.format with named placeholders
# format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5)
#   → "Dear Ann, total=$9.50"
def format_template(template: str, **kwargs: object) -> str:
    # TODO: template.format(**kwargs)
    pass


# Exercise 8: debug_repr — use !r for a debug-style embedded string
# debug_repr("hi") → "value='hi'"  (literal quotes in output)
def debug_repr(value: str) -> str:
    # TODO: f"value={value!r}"
    pass


# Exercise 9: banner_line — repeat char n times (Java: String.valueOf(ch).repeat(n))
# banner_line('=', 5) → "====="
def banner_line(char: str, width: int) -> str:
    # TODO: char * width
    pass


# Exercise 10: debug_pair — dynamic "label=value" (f"{score=}" only works with literal var names)
# debug_pair("score", 95) → "score=95"
def debug_pair(label: str, value: int) -> str:
    # TODO: f"{label}={value}"
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq


def _run_tests() -> None:
    check_eq(greet("Alex"), "Hello, Alex!", "greet — f-string")
    check_eq(money(12.5), "$12.50", "money — .2f")
    check_eq(money(3), "$3.00", "money — pads cents")
    check_eq(score_line("Alice", 95), "Alice          95", "score_line — align")
    check_eq(hex_byte(255), "0xFF", "hex_byte — #04X")
    check_eq(hex_byte(0), "0x00", "hex_byte — zero")
    check_eq(join_tags(["a", "b", "c"]), "a, b, c", "join_tags")
    check_eq(legacy_line("Bob", 7), "Bob has 7 items", "legacy_line — %")
    check_eq(
        format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5),
        "Dear Ann, total=$9.50",
        "format_template — .format",
    )
    check_eq(debug_repr("hi"), "value='hi'", "debug_repr — !r")
    check_eq(banner_line("=", 5), "=====", "banner_line — repeat")
    check_eq(banner_line("-", 0), "", "banner_line — zero width")
    check_eq(debug_pair("score", 95), "score=95", "debug_pair — dynamic label=value")

    print("\nAll tests passed! String formatting practice complete.")


if __name__ == "__main__":
    _run_tests()
