"""Lesson 1u — recursion & stack depth.

Python has no tail-call optimization. Deep recursion → RecursionError.

Run:
    uv run python lesson_06/04_recursion.py
"""

import sys


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Classic recursion — base case required")

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"factorial(5): {factorial(5)}")
# Java: same shape — each call adds a stack frame


section("2. Stack depth limit — sys.getrecursionlimit()")

print(f"default recursion limit: {sys.getrecursionlimit()}")
# CPython default often ~1000 — Java stack is usually much deeper (platform JVM)


def countdown(n: int) -> None:
    if n <= 0:
        return
    countdown(n - 1)


try:
    countdown(2000)
except RecursionError as e:
    print(f"RecursionError around deep call: {e}")


section("3. No tail-call optimization — prefer iteration for deep paths")

def factorial_loop(n: int) -> int:
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


print(f"factorial_loop(5): {factorial_loop(5)}")
# Java: same advice — deep recursion risks StackOverflowError


section("4. When recursion is still fine — shallow trees / divide-and-conquer")

def sum_nested(items: list) -> int:
    total = 0
    for x in items:
        if isinstance(x, list):
            total += sum_nested(x)
        else:
            total += x
    return total


nested = [1, [2, [3, 4]], 5]
print(f"sum_nested: {sum_nested(nested)}")


section("5. Increasing limit — rarely do this")

# sys.setrecursionlimit(3000)  # use only if you know why; can crash on C stack overflow
print("Prefer iteration or explicit stack (deque) for deep traversal")
