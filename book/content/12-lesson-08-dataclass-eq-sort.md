# Lesson 8 — Dataclasses, equality, and sorting (part 2)

Records, `equals`/`hashCode`, and sorting custom types — the Java topics Python solves with `@dataclass` and `key=`.

**Run:**

```bash
uv run python lesson_08/06_dataclass.py
uv run python lesson_08/07_eq_and_hash.py
uv run python lesson_08/08_collections_and_sorting.py
uv run python lesson_08/09_ordered_dict_lru.py
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

`__post_init__` is a hook method — runs after the generated `__init__` method (like a post-constructor check).

Generates `__init__`, `__repr__`, and `__eq__` methods for you.

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

## `__eq__` and `__hash__` methods

Same contract as Java: **equal objects must have equal hash codes** if used in `set` / `dict` keys.

- `@dataclass` generates an `__eq__` method by default
- `frozen=True` enables an `__hash__` method
- If you customize `__eq__` without `__hash__`, instances become unhashable (`__hash__ = None`)

Mutable objects should not be dict keys — Python may block with `TypeError`.

---

## Sorting with custom types

**Preferred:** `sorted(items, key=lambda p: (p.age, p.name))` — tuple key: compare `age` first, `name` on ties (≈ `Comparator.comparing(...).thenComparing(...)`).

**Alternative:** define an `__lt__` method with `@total_ordering` — ≈ `Comparable`.

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

## OrderedDict & LRU (access-order)

Lesson 2 covers **insertion** order and removal (`del`, `pop`, `popitem`, `next(iter(d))`). A plain `dict` does **not** promote a key on `get` — only `OrderedDict` (or delete+reinsert) gives **access-order** like `LinkedHashMap(accessOrder=true)`:

```python
from collections import OrderedDict

od: OrderedDict[str, int] = OrderedDict()
od["a"], od["b"], od["c"] = 1, 2, 3
od.move_to_end("a")              # promote to MRU (tail)
k, v = od.popitem(last=False)    # evict LRU (front)
```

`lesson_08/09_ordered_dict_lru.py` walks through a minimal `LRUCache` class — the pattern behind your `lesson_02/practice/LRUCache.py` side exercise.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_08/06_dataclass.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/06_dataclass.py)
- **Example:** [lesson_08/07_eq_and_hash.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/07_eq_and_hash.py)
- **Example:** [lesson_08/08_collections_and_sorting.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/08_collections_and_sorting.py)
- **Example:** [lesson_08/09_ordered_dict_lru.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/09_ordered_dict_lru.py)
- **Practice:** [lesson_08/practice/02_eq_hash.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/02_eq_hash.py)
- **Practice:** [lesson_08/practice/03_string_formatting.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/03_string_formatting.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
