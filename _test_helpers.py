"""Shared test helpers for python_learning practice files."""

import sys


def _fmt(value: object, max_len: int = 72) -> str:
    text = repr(value)
    if len(text) > max_len:
        return text[: max_len - 3] + "..."
    return text


def check_eq(actual: object, expected: object, label: str) -> None:
    if actual == expected:
        print(f"  ✓ {label}")
    else:
        print(f"  ✗ {label} — expected {_fmt(expected)}, got {_fmt(actual)}")
        sys.exit(1)


def check(condition: bool, label: str, *, detail: str = "") -> None:
    """For non-equality checks; optional detail when condition is false."""
    if condition:
        print(f"  ✓ {label}")
    else:
        suffix = f" — {detail}" if detail else ""
        print(f"  ✗ {label}{suffix}")
        sys.exit(1)
