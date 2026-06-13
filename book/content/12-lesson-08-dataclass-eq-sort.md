# Lesson 8 — Dataclasses, equality, and sorting (part 2)

Records, `equals`/`hashCode`, and sorting custom types — the Java topics Python solves with `@dataclass` and `key=`.

**Run:**

```bash
uv run python lesson_08/06_dataclass.py
uv run python lesson_08/07_eq_and_hash.py
uv run python lesson_08/08_collections_and_sorting.py
```

---

## @dataclass — like a Java record

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""

    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValueError("age must be non-negative")
```

Generates `__init__`, `__repr__`, `__eq__` for you.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

`frozen=True` — immutable; use `dataclasses.replace(p, x=5)` to "update".

> **Java:** `record Person(String name, int age) { }` — `@dataclass` is the daily Python equivalent.

Fields with defaults must come **after** required fields.

---

## __eq__ and __hash__

Same contract as Java: **equal objects must have equal hash codes** if used in `set` / `dict` keys.

- `@dataclass` generates `__eq__` by default
- `frozen=True` enables `__hash__`
- If you customize `__eq__` without `__hash__`, instances become unhashable (`__hash__ = None`)

Mutable objects should not be dict keys — Python may block with `TypeError`.

---

## Sorting with custom types

**Preferred:** `sorted(items, key=lambda p: (p.age, p.name))` — like `Comparator.comparing`.

**Alternative:** define `__lt__` for `@total_ordering` — ≈ `Comparable`.

```python
people = [{"name": "bob", "score": 87}, {"name": "alice", "score": 95}]
sorted(people, key=lambda p: p["score"], reverse=True)
```

Dicts sort by key; sort **items** or use `key=` on a list of objects.

---

## Pause and practice

```bash
uv run python lesson_08/practice/01_classes.py
uv run python lesson_08/practice/02_eq_hash.py
uv run python lesson_08/practice/03_string_formatting.py
```

> **Key idea:** `@dataclass` for data carriers; `key=` for sorting; understand eq/hash before putting objects in sets and dict keys.
---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_08/06_dataclass.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/06_dataclass.py)
- **Example:** [lesson_08/07_eq_and_hash.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/07_eq_and_hash.py)
- **Example:** [lesson_08/08_collections_and_sorting.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/08_collections_and_sorting.py)
- **Practice:** [lesson_08/practice/02_eq_hash.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/02_eq_hash.py)
- **Practice:** [lesson_08/practice/03_string_formatting.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/03_string_formatting.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
