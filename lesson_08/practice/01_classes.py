"""
Lesson 2 practice — classes & self.

Fill in each class below, then run:
    uv run python lesson_08/practice/01_classes.py
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


from dataclasses import dataclass


# Exercise 1: A Rectangle with width/height, area() and perimeter() methods
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        # TODO
        pass

    def area(self) -> float:
        # TODO
        pass

    def perimeter(self) -> float:
        # TODO
        pass


# Exercise 2: BankAccount with deposit/withdraw; no negative balance allowed
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # TODO
        pass

    def deposit(self, amount: float) -> None:
        # TODO
        pass

    def withdraw(self, amount: float) -> bool:
        # TODO: return True if successful, False if insufficient funds
        pass

    def get_balance(self) -> float:
        # TODO
        pass


# Exercise 3: Employee extends Person (dataclass); add salary and a describe() method
@dataclass
class Person:
    name: str
    age: int


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float) -> None:
        # TODO: call parent __init__
        pass

    def describe(self) -> str:
        # TODO: return "Alice, age 30, salary $95000"
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
