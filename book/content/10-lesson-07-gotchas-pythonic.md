# Lesson 7 — Java gotchas and pythonic style

Habits that compile in your head but fail or surprise in Python.

**Run:**

```bash
uv run python lesson_07/01_java_gotchas.py
uv run python lesson_07/02_pythonic_compactness.py
uv run python lesson_07/03_cheat_sheet.py
```

---

## Syntax and naming

| Java | Python |
|------|--------|
| `else if` | `elif` |
| `true` / `false` | `True` / `False` |
| `i++` | `i += 1` |
| method overloading | **one** `def` — last wins; use defaults |

```python
def greet(name: str, excited: bool = False) -> str:
    ...
```

Only one `__init__` on a class — same rule.

---

## Default argument trap

```python
def add_item(item, bucket=None):  # never bucket=[]
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

---

## Pythonic patterns (prefer these)

```python
counts[w] = counts.get(w, 0) + 1
if key in d:
    ...
for i, item in enumerate(items):
    ...
names = [p["name"] for p in people if p["active"]]
```

Avoid:

```python
for i in range(len(items)):
    item = items[i]    # use enumerate or direct iteration
```

### EAFP vs LBYL

**Easier to Ask Forgiveness than Permission:**

```python
try:
    value = d[key]
except KeyError:
    value = default
```

Often cleaner than `if key in d` for one-off access — taste and context matter.

---

## Cheat sheet mindset

Lesson 7's cheat sheet file is a **lookup**, not a second read. Use it when you forget:

- truthiness table
- slice grammar
- comprehension shapes
- `is` vs `==`

> **Key idea:** Python rewards reading code aloud. If a loop feels like indexed Java, there is usually a shorter form.
---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_07/01_java_gotchas.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/01_java_gotchas.py)
- **Example:** [lesson_07/02_pythonic_compactness.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/02_pythonic_compactness.py)
- **Example:** [lesson_07/03_cheat_sheet.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/03_cheat_sheet.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
