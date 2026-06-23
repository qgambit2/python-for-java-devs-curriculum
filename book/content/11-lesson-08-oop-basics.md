# Lesson 8 — Classes and OOP (part 1)

Coming from Java, three things trip you up first: there is no `new`, there are no access modifiers, and `self` is a parameter you type by hand. This chapter makes each feel normal before `@dataclass` (next chapter) hides most of the boilerplate.

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

- The `__init__` method is the initializer — called automatically on `Dog(...)`
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

> **Java:** `this` is implicit; `self` is the **explicit** first parameter of every instance method — you write it in the signature, but not at the call site (`rex.bark()`, not `rex.bark(rex)`).

### Encapsulation — convention, not keywords

```python
class Account:
    def __init__(self, balance: int) -> None:
        self.owner = "Ann"     # public
        self._balance = balance # "internal — hands off" (convention only)
        self.__pin = 1234       # name-mangled to _Account__pin
```

There is no `private` / `protected` / `public`. A leading `_` signals "internal"; a leading `__` triggers **name-mangling** (`__pin` becomes `_Account__pin`), which discourages accidental access but is **not** enforced privacy.

> **Java:** no access modifiers — leading underscores are a naming convention, not a compiler rule. Nothing stops a caller who really wants in.

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

Lookup walks the MRO (method resolution order) — like Java's superclass chain. Use `super()` to extend, not replace, parent behavior:

```python
class Animal:
    def __init__(self, legs: int) -> None:
        self.legs = legs

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(legs=4)   # like Java super(...)
        self.name = name
```

> **Java:** `super().__init__(...)` ≈ `super(...)`; `super().speak()` ≈ `super.speak()`. Unlike Java, `super()` is a callable returning a proxy, and the parent initializer is **not** called for you — you invoke `super().__init__()` explicitly.

---

## String representation (preview)

Classes can define special **methods** whose names start and end with double underscores:

- `__str__` method — human-readable string, like Java `toString()`
- `__repr__` method — developer/debug string (ideally valid-ish Python for the REPL)

The `__format__` method powers custom f-string formatting — see `lesson_08/03_str_repr_and_formatting.py` and practice `lesson_08/practice/03_string_formatting.py`.

> **Java:** one `toString()`; Python splits display vs debug across two methods (`__str__` and `__repr__`).

> **Key idea:** No `new`, no overloading, explicit `self`. Start with plain classes; reach for `@dataclass` when data dominates behavior (next chapter).

---

## Pause and practice

```bash
uv run python lesson_08/practice/01_classes.py
```

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_08/01_class_basics.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/01_class_basics.py)
- **Example:** [lesson_08/02_self_explained.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/02_self_explained.py)
- **Example:** [lesson_08/04_inheritance.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/04_inheritance.py)
- **Example:** [lesson_08/05_class_vs_instance.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/05_class_vs_instance.py)
- **Practice:** [lesson_08/practice/01_classes.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/practice/01_classes.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
