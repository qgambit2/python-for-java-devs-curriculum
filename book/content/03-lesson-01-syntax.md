# Lesson 1 — Syntax and variables

Before collections, two syntax habits must become automatic: **indentation as block structure** and **`print()` with flexible arguments**.

Run alongside this chapter:

```bash
uv run python lesson_01/01_syntax.py
uv run python lesson_01/02_variables.py
```

## Indentation instead of braces

Java uses braces to delimit blocks. Python uses **consistent indentation** — typically four spaces.

```python
x = 10
if x > 0:
    print("positive")
```

The line `print("positive")` belongs to the `if` because it is indented under it. Remove the indentation and the program means something else — or fails to run.

> **Java:** `if (x > 0) { System.out.println("positive"); }` — the `{ }` are explicit. Python trusts whitespace. Your IDE should show whitespace; never mix tabs and spaces.

## print() is not println()

`print()` accepts **any number** of arguments. Each value is converted to a string and joined with a space by default.

```python
print("hello", "world")      # hello world
print("a", "b", sep="-")     # a-b
```

> **Java:** `System.out.println("a" + " " + b)` builds one string. Python separates the values for you.

## Variables and dynamic typing

Assignment uses `=`. Types are not declared at runtime:

```python
name = "Alice"
count = 42
price = 19.99
active = True
```

You *may* add type hints for documentation and tooling:

```python
score: int = 95
```

The interpreter ignores hints at runtime. Wrong-type assignments still run until something breaks.

> **Java:** `int score = 95;` is enforced by the compiler. Python hints are for humans and `mypy`, not the runtime.

## None, not null

Use `None` for absence of value. Test with `is`:

```python
value = None
if value is None:
    print("missing")
```

> **Java:** `if (value == null)` — in Python prefer `is None` for identity with the singleton `None`.

## What to take into Lesson 2

You need comfortable reading of `if`, assignment, and `print`. Lesson 2 introduces the four collection types that replace most of `java.util` for everyday scripts.
---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_01/01_syntax.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_01/01_syntax.py)
- **Example:** [lesson_01/02_variables.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_01/02_variables.py)
- **Practice:** [lesson_01/practice/01_practice.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_01/practice/01_practice.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
