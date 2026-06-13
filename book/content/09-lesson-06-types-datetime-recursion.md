# Lesson 6 — Types, math, datetime, and recursion

Beyond Lesson 1's variable intro: how Python's type model differs from Java's primitives-and-wrappers world.

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
type(42)           # <class 'int'>
isinstance(x, int) # prefer over type(x) == int for subclasses
```

`isinstance(x, (list, tuple))` checks multiple types.

### Mutability

| Mutable | Immutable |
|---------|-----------|
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple`, `frozenset` |

Mutable objects as default args or dict keys cause bugs — copies and `None` defaults matter.

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

> **Key idea:** Types are checked by tools, not the interpreter. `datetime` and `Decimal` fill gaps plain `float` cannot.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_06/01_types_and_datatypes.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/01_types_and_datatypes.py)
- **Example:** [lesson_06/02_math_and_numbers.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/02_math_and_numbers.py)
- **Example:** [lesson_06/03_datetime.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/03_datetime.py)
- **Example:** [lesson_06/04_recursion.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_06/04_recursion.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
