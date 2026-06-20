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
while not (_p / '_lesson_runner.py').is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

def greet(name: str) -> str:
    pass

def money(amount: float) -> str:
    pass

def score_line(name: str, score: int) -> str:
    pass

def hex_byte(n: int) -> str:
    # f"0x{n:02X}"  — Java: String.format("0x%02X", n)
    # 255 → 0xFF,  15 → 0x0F (pad),  0 → 0x00
    pass

def join_tags(tags: list[str]) -> str:
    pass

def legacy_line(name: str, count: int) -> str:
    pass

def format_template(template: str, **kwargs: object) -> str:
    # template.format(**kwargs)  — see Lesson 4 / book § **kwargs
    pass

def debug_repr(value: str) -> str:
    pass

def banner_line(char: str, width: int) -> str:
    pass

def debug_pair(label: str, value: int) -> str:
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
    check_eq(score_line("Alice", 95), "Alice       95", "score_line — align")
    check_eq(hex_byte(255), "0xFF", "hex_byte — 02X")
    check_eq(hex_byte(15), "0x0F", "hex_byte — pad 15")
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
