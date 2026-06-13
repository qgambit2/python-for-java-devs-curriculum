"""Lesson 2e — class attributes vs instance attributes (≈ static vs instance fields)."""

from dataclasses import dataclass


class BankAccount:
    bank_name = "Python Federal"  # class attribute — shared by ALL instances (≈ static)

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner  # instance attribute — per object (set in __init__)
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount  # must use self — bare balance += would be UnboundLocalError


alice = BankAccount("Alice", 100.0)
bob = BankAccount("Bob", 50.0)
alice.deposit(25.0)

print(BankAccount.bank_name)  # via class — like BankAccount.bankName
print(alice.bank_name)        # via instance — falls back to class attribute
print(alice.balance)          # 125.0 — instance field
print(bob.balance)            # 50.0 — bob unchanged

# Missing attribute → AttributeError (object lookup, not local scope)
try:
    alice.age
except AttributeError as e:
    print(f"alice.age → {e}")


# Read vs write: self.attr += 1 READS class (fallback), WRITES instance (shadow)
class ReallyBad:
    call_count = 0

    def ping(self) -> None:
        self.call_count += 1


a_bad, b_bad = ReallyBad(), ReallyBad()
print(f"before ping: a.__dict__={a_bad.__dict__!r}")
a_bad.ping()
a_bad.ping()
b_bad.ping()
print(f"ReallyBad: a={a_bad.call_count}, b={b_bad.call_count}, class={ReallyBad.call_count}")
print(f"after ping: a.__dict__={a_bad.__dict__!r}, class still {ReallyBad.call_count}")


class ForgotSelfDemo:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def bad_deposit(self, amount: float) -> None:
        balance += amount  # forgot self — balance is a LOCAL; Java would use this.balance


try:
    ForgotSelfDemo(100).bad_deposit(5)
except UnboundLocalError as e:
    print(f"balance += amount (no self) → {e}")

# TRAP: mutable class attribute — ONE list shared by all instances
class BadBucket:
    items: list[int] = []  # noqa: RUF012 — intentional demo of the bug

    def add(self, x: int) -> None:
        self.items.append(x)


a = BadBucket()
b = BadBucket()
a.add(1)
print(f"BadBucket shared list: a.items={a.items}, b.items={b.items}")  # both [1]!

# FIX: per-instance list in __init__
class GoodBucket:
    def __init__(self) -> None:
        self.items: list[int] = []

    def add(self, x: int) -> None:
        self.items.append(x)


# @dataclass: fields LOOK class-level but are per-instance (generated self.name = name)
@dataclass
class Person:
    name: str
    age: int


p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30)
