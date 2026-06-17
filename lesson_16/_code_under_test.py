"""Small functions and classes for Lesson 16 testing demos — not production code."""

from __future__ import annotations


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def clamp(n: int, lo: int, hi: int) -> int:
    if lo > hi:
        raise ValueError("lo must be <= hi")
    return max(lo, min(hi, n))


class ScoreBoard:
    """Mutable score tracker — used for fixture / lifecycle demos."""

    def __init__(self) -> None:
        self._scores: dict[str, int] = {}

    def add(self, name: str, points: int) -> None:
        self._scores[name] = self._scores.get(name, 0) + points

    def get(self, name: str) -> int:
        return self._scores.get(name, 0)

    def top(self, n: int) -> list[tuple[str, int]]:
        ranked = sorted(self._scores.items(), key=lambda kv: (-kv[1], kv[0]))
        return ranked[:n]


class Greeter:
    """Depends on an external name provider — useful for mocking demos."""

    def __init__(self, name_provider) -> None:
        self._name_provider = name_provider

    def greet(self) -> str:
        name = self._name_provider.get_name()
        return f"Hello, {name}!"
