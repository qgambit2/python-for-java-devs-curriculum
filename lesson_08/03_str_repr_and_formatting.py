"""Lesson 2c — __str__, __repr__, and OOP string formatting.

Part A: two conversion paths (str vs repr).
Part B: __format__, formatting methods, objects in f-strings.

Lesson 1 string basics (f-strings, specifiers, join): lesson_03/01_strings.py

Run:
    uv run python lesson_08/03_str_repr_and_formatting.py

Practice:
    uv run python lesson_08/practice/03_string_formatting.py
"""

from dataclasses import dataclass


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("A1. Two conversion paths — not print=__str__, repr=__repr__")

#   str path:  print(p), str(p), f"{p}"  →  __str__ (or fallback to __repr__)
#   repr path: repr(p), debugger, REPL   →  __repr__ only


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


p = Point(3, 4)
print(p)
print(str(p))
print(repr(p))
print(p.__str__())
print(p.__repr__())


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def describe_short(self) -> str:
        return f"{self.width}x{self.height}"

    def describe_long(self) -> str:
        return f"Rectangle {self.describe_short()}"


print(Rectangle(4, 5).describe_long())


class OnlyRepr:
    def __init__(self, label: str) -> None:
        self.label = label

    def __repr__(self) -> str:
        return f"OnlyRepr(label={self.label!r})"

    def __str__(self) -> str:
        return self.__repr__()


print(OnlyRepr("demo"))


class OnlyStr:
    def __str__(self) -> str:
        return "nice for print"


print(OnlyStr())
print(repr(OnlyStr()))


class OnlyReprNoStr:
    def __repr__(self) -> str:
        return "OnlyReprNoStr(debug)"


o = OnlyReprNoStr()
print(o)
print(str(o) == repr(o))


section("B1. Objects in f-strings — !r uses repr path")

print(f"user sees: {p}")
print(f"debug: {p!r}")


section("B2. Formatting methods (≈ toString variants)")

class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def summary(self) -> str:
        return f"{self.owner}: ${self.balance:.2f}"

    def __str__(self) -> str:
        return self.summary()


acct = BankAccount("Alice", 1234.5)
print(acct)
print(f"Account → {acct}")


section("B3. __format__ — custom format specs")

class Money:
    def __init__(self, amount: float, currency: str = "USD") -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:.2f}"

    def __format__(self, format_spec: str) -> str:
        if format_spec in ("", "s"):
            return str(self)
        return f"{self.currency} {format(self.amount, format_spec)}"


m = Money(99.5)
print(f"default: {m}")
print(f"two decimals: {m:.2f}")
print(format(m, ".2f"))


section("B4. @dataclass + inheritance formatting")

@dataclass
class Person:
    name: str
    age: int

    def greeting(self) -> str:
        return f"Hi, I'm {self.name} ({self.age})"


@dataclass
class Employee(Person):
    salary: float

    def describe(self) -> str:
        return f"{self.greeting()}, salary ${self.salary:,.0f}"


person = Person("Bob", 25)
print(person)
print(person.greeting())
print(Employee("Carol", 30, 95_000.0).describe())


section("B5. Multi-line reports")

def account_report(accounts: list[BankAccount]) -> str:
    line = "-" * 40
    rows = [f"  {a.summary()}" for a in accounts]
    return f"Account report\n{line}\n" + "\n".join(rows) + f"\n{line}"


print(account_report([acct, BankAccount("Bob", 50.0)]))
