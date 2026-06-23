# Lesson 6 — Types, math, datetime, and recursion

Beyond Lesson 1's variable intro: how Python's type model differs from Java's primitives-and-wrappers world. The payoff is concrete — once you internalize that *everything is an object* (no `int`/`Integer` split, no `char`), the rules for what can be a `dict` key, why money needs `Decimal`, and why deep recursion fails differently than in Java all fall out of one model instead of four special cases. This lesson covers the type model, exact-vs-float arithmetic, timezone-aware `datetime`, and recursion's hard ceiling.

**Run:**

```bash
uv run python lesson_06/01_types_and_datatypes.py
uv run python lesson_06/02_math_and_numbers.py
uv run python lesson_06/03_datetime.py
uv run python lesson_06/04_recursion.py
```

---

## Everything is an object

No `char` type — single characters are `str` of length 1. No separate `int` / `Integer` split at runtime.

```python
type(42)              # <class 'int'>
isinstance(42, int)   # prefer over type(x) == int — also matches subclasses
isinstance(value, (list, tuple))   # check several types at once
```

> **Java:** there is no `int`/`Integer` autoboxing distinction and no `char` — every value is a full object. `42` is an `int` object with methods; `"a"` is a length-1 `str`, not a `char`.

### Mutability

| Mutable | Immutable |
|---------|-----------|
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple`, `frozenset` |

Two distinct traps follow from this. Mutable objects are **unhashable**, so they cannot be `dict` keys or `set` members — use a `tuple` instead of a `list`. And a mutable **default argument** is created once and shared across every call (see Lesson 7's default-argument trap) — prefer `None` defaults and copy when you need to mutate.

---

## math and Decimal

```python
import math
math.sqrt(2)

from decimal import Decimal
Decimal("0.1") + Decimal("0.2")   # exact decimal arithmetic
```

> **Java:** `Math.sqrt`, `BigDecimal` for money — same motivation.

---

## datetime — java.time mindset

```python
from datetime import date, datetime, timedelta, timezone

today = date.today()
now = datetime.now(timezone.utc)
later = now + timedelta(days=7)
```

Prefer **timezone-aware** `datetime` for real systems — `naive` datetimes bite like `java.util.Date`.

> **Java:** `LocalDate`, `Instant`, `ZonedDateTime`, `Duration`.

---

## Recursion

```python
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

CPython default recursion limit ≈ **1000** frames — `RecursionError`, not `StackOverflowError`.

Deep recursion → iterative version or explicit stack.

> **Java:** the JVM also caps the call stack (`StackOverflowError`), but the limits differ in kind. Java's depends on thread stack size (often tens of thousands of frames) and there is no JIT tail-call elimination either; Python's is a deliberate, low default (≈1000) you can raise with `sys.setrecursionlimit`, but the Pythonic move is to rewrite deep recursion iteratively rather than lift the ceiling.

> **Key idea:** Types are checked by tools, not the interpreter. `datetime` and `Decimal` fill gaps plain `float` cannot.

---

## Pause and practice

```bash
uv run python lesson_06/01_types_and_datatypes.py
uv run python lesson_06/04_recursion.py
```

Run the demos, then experiment: use `isinstance` to guard a function against the wrong type, compare `Decimal("0.1") * 3` against the `float` result, and rewrite `factorial` as a loop so it survives an input that would blow the recursion limit.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_06/01_types_and_datatypes.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/01_types_and_datatypes.py)
- **Example:** [lesson_06/02_math_and_numbers.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/02_math_and_numbers.py)
- **Example:** [lesson_06/03_datetime.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/03_datetime.py)
- **Example:** [lesson_06/04_recursion.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/04_recursion.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
