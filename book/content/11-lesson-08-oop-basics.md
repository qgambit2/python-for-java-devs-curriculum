# Lesson 8 — Classes and OOP (part 1)

Python classes feel like Java without access modifiers, `new`, or overloading.

**Run:**

```bash
uv run python lesson_08/01_class_basics.py
uv run python lesson_08/02_self_explained.py
uv run python lesson_08/04_inheritance.py
uv run python lesson_08/05_class_vs_instance.py
```

---

## Class basics

```python
class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"

rex = Dog("Rex", 3)    # no `new`
print(rex.bark())
```

- `__init__` is the initializer — called automatically on `Dog(...)`
- `self` is explicit first parameter — ≈ `this`, but you must write it
- Fields are public by convention (no `private` keyword)

> **Java:** one constructor with default args instead of overloads: `def __init__(self, name, age=0)`.

---

## self — instance vs class

Methods receive the instance as `self`. Calling `rex.bark()` passes `rex` as `self` behind the scenes.

Class attributes vs instance attributes:

```python
class Counter:
    total = 0              # class attribute — shared

    def __init__(self):
        self.count = 0     # instance attribute — per object
```

Mutating `Counter.total` affects all instances; `self.count` is per instance.

---

## Inheritance

```python
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"
```

Lookup walks the MRO (method resolution order) — like Java superclass chain. Use `super()` when extending parent behavior.

---

## String representation (preview)

`__str__` for human-readable; `__repr__` for developer/debug (ideally valid-ish Python).

Full formatting (`__format__`, f-string hooks) — `lesson_08/03_str_repr_and_formatting.py` and practice `lesson_08/practice/03_string_formatting.py`.

> **Key idea:** No `new`, no overloading, explicit `self`. Start with plain classes; reach for `@dataclass` when data dominates behavior (next chapter).

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_08/01_class_basics.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/01_class_basics.py)
- **Example:** [lesson_08/02_self_explained.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/02_self_explained.py)
- **Example:** [lesson_08/04_inheritance.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/04_inheritance.py)
- **Example:** [lesson_08/05_class_vs_instance.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/05_class_vs_instance.py)
- **Practice:** [lesson_08/practice/01_classes.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/01_classes.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
