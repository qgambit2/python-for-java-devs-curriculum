"""Lesson 1s — math & numbers.

Java: Math.*, %, integer division. Python: math module, //, %, **, divmod.

Run:
    uv run python lesson_06/02_math_and_numbers.py
"""

import math
from decimal import Decimal


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Operators — //, %, **")

print(7 / 2)    # 3.5  — true division (Java: 7 / 2.0)
print(7 // 2)   # 3    — floor division (Java: 7 / 2 on ints)
print(7 % 2)    # 1
print(2 ** 10)  # 1024 — Java: Math.pow (returns double)

q, r = divmod(7, 2)
print(f"divmod(7, 2): quotient={q}, remainder={r}")


section("2. math module — import math (not java.lang.Math static)")

print(math.sqrt(16))       # Math.sqrt
print(math.ceil(2.3))      # Math.ceil
print(math.floor(2.9))     # no Math.floor in older Java — but exists in Java
print(math.pi, math.e)
print(math.log(math.e))    # natural log


section("3. round, abs, min, max — builtins (no import)")

print(round(2.5), round(3.14159, 2))
print(abs(-7), min(3, 1, 4), max([1, 5, 2]))


section("4. Float gotcha — like Java double precision")

print(0.1 + 0.2)                    # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3))  # True — compare floats with tolerance
# Money: use Decimal, not float (Java: BigDecimal)
price = Decimal("19.99") + Decimal("0.01")
print(f"Decimal money: {price}")


section("5. random — import random (Java: java.util.Random)")

import random

print(random.randint(1, 6))     # inclusive both ends — Java: nextInt(6) + 1
print(random.choice(["a", "b", "c"]))
