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
| method overloading | **no overloading** — a later `def` with the same name just rebinds it; use default args or `*args` |

```python
def greet(name: str, excited: bool = False) -> str:
    ...
```

Only one `__init__` method on a class — same rule.

---

## Default argument trap

```python
def add_item(item, bucket=None):  # never bucket=[]
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

> **Java:** Java has no analog — default values there are evaluated per call. In Python the default expression runs **once**, at `def` time, so a shared `bucket=[]` accumulates across calls. Always default to `None` and build the list inside.

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

> **Java:** Java culture is **LBYL** (Look Before You Leap) — you null-check and `containsKey` first, partly because exceptions are expensive and checked exceptions make `try` blocks heavy. Python's exceptions are cheap and unchecked, so reaching for the value and catching `KeyError`/`AttributeError` (EAFP) is idiomatic, not a code smell — it also avoids the time-of-check/time-of-use race that the check-then-act pattern hides.

---

## Cheat sheet mindset

Lesson 7's cheat sheet file is a **lookup**, not a second read. Use it when you forget:

- truthiness table
- slice grammar
- comprehension shapes
- `is` vs `==`

> **Key idea:** Python rewards reading code aloud. If a loop feels like indexed Java, there is usually a shorter form.

---

## Pause and practice

```bash
uv run python lesson_07/01_java_gotchas.py
uv run python lesson_07/02_pythonic_compactness.py
```

Run both, then convert a `range(len(...))` loop in your own code to `enumerate`, and rewrite one check-then-access (`if key in d`) as an EAFP `try`/`except KeyError` — decide which reads better in context.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_07/01_java_gotchas.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/01_java_gotchas.py)
- **Example:** [lesson_07/02_pythonic_compactness.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/02_pythonic_compactness.py)
- **Example:** [lesson_07/03_cheat_sheet.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_07/03_cheat_sheet.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
