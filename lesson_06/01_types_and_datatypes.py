"""Lesson 1r — types & datatypes (beyond the 02_variables intro).

Java: primitives vs wrappers vs objects. Python: everything is an object;
no char type; dynamic typing at runtime.

Run:
    uv run python lesson_06/01_types_and_datatypes.py
"""

from collections.abc import Mapping, Sequence


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Core built-in types — no declarations")

samples = {
    "int": 42,
    "float": 3.14,
    "bool": True,
    "str": "hello",
    "NoneType": None,
    "list": [1, 2],
    "tuple": (1, 2),
    "dict": {"a": 1},
    "set": {1, 2},
}
for name, value in samples.items():
    print(f"{name:10} {type(value).__name__:8} {value!r}")

# Java int/long/double/boolean/char/String — Python folds most into int/float/bool/str
# No separate char — single-character str


section("2. type() vs isinstance() — prefer isinstance")

x = 42
print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True — works with subclasses too
# Java: x instanceof Integer (Python ints are not boxed unless you box them yourself)


section("3. Mutability — critical for Java habits")

# Mutable: list, dict, set — passed by object reference (like Java object refs)
lst = [1, 2]
other = lst
other.append(3)
print(f"shared list mutation: {lst}")  # [1, 2, 3]

# Immutable: int, str, tuple, frozenset — "changing" makes a new object
s = "hi"
# s[0] = "H"  # TypeError
s = "Hi"      # rebinds name — new str object


section("4. str vs bytes — no Java char[]; use str or bytes")

text = "café"
raw = b"\xc3\xa9"   # bytes literal — ASCII-ish only in source; use escapes for non-ASCII
print(text, raw, raw.decode("utf-8"))
# Java: String (UTF-16) vs byte[] — Python str is Unicode; encode/decode explicitly


section("5. Casting / parsing — int(), float(), str(), bool()")

print(int("42"), float("3.14"), str(99), bool(0), bool(""))
# Java: Integer.parseInt, Double.parseDouble, String.valueOf
try:
    int("3.14")
except ValueError as e:
    print(f"int('3.14'): {e}")  # unlike (int) double cast in Java


section("6. Type hints — documentation only (not enforced at runtime)")

def greet(name: str, times: int = 1) -> str:
    return (f"Hi, {name}! ") * times

print(greet("Java dev", 2))
# Java: compiler enforces types; Python: mypy/pyright optional


section("7. ABC checks — Sequence, Mapping (optional but useful)")

data: list[int] = [1, 2, 3]
print(isinstance(data, Sequence))   # True — list is a Sequence
print(isinstance({"a": 1}, Mapping))  # True — dict is a Mapping
# Java: instanceof List / Map on concrete classes
