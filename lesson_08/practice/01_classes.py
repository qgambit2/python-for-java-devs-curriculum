"""
Lesson 2 practice — classes & self.

Fill in each class below, then run:
    uv run python lesson_08/practice/01_classes.py
"""
import sys
from pathlib import Path
_p = Path(__file__).resolve().parent
while not (_p / '_lesson_runner.py').is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))
from dataclasses import dataclass

class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        pass

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class BankAccount:

    def __init__(self, owner: str, balance: float=0.0) -> None:
        pass

    def deposit(self, amount: float) -> None:
        pass

    def withdraw(self, amount: float) -> bool:
        pass

    def get_balance(self) -> float:
        pass

@dataclass
class Person:
    name: str
    age: int

class Employee(Person):

    def __init__(self, name: str, age: int, salary: float) -> None:
        pass

    def describe(self) -> str:
        pass
# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _test_helpers import check_eq as _check


def _run_tests() -> None:
    rect = Rectangle(4, 5)
    _check(rect.area(), 20, "Rectangle.area — self in action")
    _check(rect.perimeter(), 18, "Rectangle.perimeter — geometry checks out")

    acct = BankAccount("Alice", 100.0)
    acct.deposit(50.0)
    _check(acct.get_balance(), 150.0, "BankAccount.deposit — balance grows")
    _check(acct.withdraw(30.0), True, "BankAccount.withdraw — successful withdrawal")
    _check(acct.get_balance(), 120.0, "BankAccount — balance after withdrawal")
    _check(acct.withdraw(200.0), False, "BankAccount.withdraw — overdraft blocked")
    _check(acct.get_balance(), 120.0, "BankAccount — balance unchanged after reject")

    emp = Employee("Alice", 30, 95_000)
    _check(emp.describe(), "Alice, age 30, salary $95000", "Employee — inheritance works")

    print("\nAll tests passed! Lesson 2 practice complete.")


if __name__ == "__main__":
    _run_tests()
