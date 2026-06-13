"""Lesson 2a — class basics (Java comparison).

No constructor overloading — one __init__ only. Use default args instead:
  def __init__(self, name: str, age: int = 0)
See lesson_07/01_java_gotchas.py and faq.md § no constructor overloading.
"""


class Dog:
    """Like a Java class, but no access modifiers (public/private)."""

    def __init__(self, name: str, age: int) -> None:
        # __init__ — fixed special name; Python calls it on Dog(...) (no `new`)
        # ≈ Java constructor. You never call rex.__init__(...) yourself.
        # See faq.md § Lesson 2 — OOP for __post_init__ (@dataclass only).
        self.name = name  # self ≈ this; must be explicit
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"


rex = Dog("Rex", 3)          # no `new` keyword
print(rex.bark())
print(rex.name)              # fields are public by convention
