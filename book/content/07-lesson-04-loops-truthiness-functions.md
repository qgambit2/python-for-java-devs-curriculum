# Lesson 4 — Loops, truthiness, and functions

Builds on **Lesson 1 control flow** (`lesson_01/03_control_flow.py`). Here: truthiness in `if`, `is` vs `==`, and `def` functions.

**Run:**

```bash
uv run python lesson_04/01_loops.py
uv run python lesson_04/02_truthiness.py
uv run python lesson_04/03_functions.py
```

---

## for and while

```python
for fruit in fruits:
    print(fruit)

for key, value in scores.items():   # need both? use .items()
    print(key, value)

for i in range(3):                  # 0, 1, 2 — stop exclusive
    print(fruits[i])
```

`range(start, stop, step)` matches slice semantics — **stop is exclusive**.

`break` and `continue` work like Java.

### for-else — no Java equivalent

```python
for fruit in fruits:
    if fruit == target:
        print("found")
        break
else:
    print("not found")    # runs only if loop did NOT break
```

> **Java:** simulate with a `found` flag.

---

## Truthiness — empty means false

These are **falsy:** `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`. Everything else is truthy.

```python
if name:           # False for ""
    ...
if scores:       # False for []
    ...
```

### `is` vs `==`

- `==` compares **values**
- `is` compares **identity** (same object in memory)

```python
x is None          # correct None check
x == None          # works but avoid — style guides prefer `is None`
```

Never use `is` for string or int content checks — only for singletons like `None`.

> **Java:** `==` on objects is identity; `.equals()` is value. Python splits this explicitly.

---

## Functions

```python
def greet(person: str, times: int = 1) -> str:
    return (f"Hi, {person}! ") * times

greet("Java dev")
greet("Java dev", times=3)
```

- No overloading — one `def` per name; use default args
- Type hints are optional at runtime
- Keyword args at call site: `times=3`

### Do not mutate caller's collections

```python
def merge_scores(left, right):
    result = right.copy()    # new dict
    for name, score in left.items():
        result[name] = result.get(name, 0) + score
    return result
```

Mutating `right` in place surprises callers — same as modifying a passed-in `HashMap`.

### Mutable default args — classic gotcha

```python
def add_item(item, bucket=None):   # NOT bucket=[]
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Default `[]` is created **once** at function definition time and shared across calls.

> **Key idea:** Copy before mutate; `None` for optional mutable defaults.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_04/01_loops.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/01_loops.py)
- **Example:** [lesson_04/02_truthiness.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/02_truthiness.py)
- **Example:** [lesson_04/03_functions.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/03_functions.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
