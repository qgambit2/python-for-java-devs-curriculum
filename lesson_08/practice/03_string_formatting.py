"""
Lesson 2 — string formatting with classes (practice).

Read:
    uv run python lesson_08/03_str_repr_and_formatting.py
    lesson_03/01_strings.py  (basics)

Fill in each TODO, then run:
    uv run python lesson_08/practice/03_string_formatting.py
"""
import sys
from pathlib import Path
_p = Path(__file__).resolve().parent
while not (_p / '_lesson_runner.py').is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))
from dataclasses import dataclass

class PointLabel:

    def __init__(self, x: int, y: int) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

class Wallet:

    def __init__(self, name: str, balance: float) -> None:
        pass

    def summary(self) -> str:
        pass

class Temperature:

    def __init__(self, celsius: float) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.celsius:.1f}°C'

    def __format__(self, format_spec: str) -> str:
        pass

def report_header(title: str, width: int) -> str:
    pass

@dataclass
class Employee:
    name: str
    department: str
    salary: float

    def describe(self) -> str:
        pass

def debug_point(p: PointLabel) -> str:
    pass
# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq


def _run_tests() -> None:
    pt = PointLabel(3, 4)
    check_eq(str(pt), "(3, 4)", "PointLabel.__str__")
    check_eq(f"{pt}", "(3, 4)", "PointLabel in f-string")

    w = Wallet("Alice", 12.5)
    check_eq(w.summary(), "Alice: $12.50", "Wallet.summary")

    t = Temperature(23.456)
    check_eq(f"{t:.1f}", "23.5°C", "Temperature.__format__")
    check_eq(str(t), "23.5°C", "Temperature.__str__")

    header = report_header("Accounts", 10)
    check_eq(header, "==========\nAccounts\n==========", "report_header")

    emp = Employee("Bob", "Engineering", 120_000.0)
    check_eq(emp.describe(), "Bob (Engineering): $120,000", "Employee.describe")

    check_eq(debug_point(PointLabel(1, 2)), "debug=PointLabel(1, 2)", "debug_point — !r")

    print("\nAll tests passed! Lesson 2 string formatting practice complete.")


if __name__ == "__main__":
    _run_tests()
