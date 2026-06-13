# Lesson 5 — Builtins, comprehensions, and functional style

Python's "stdlib in the language" — `sorted`, `zip`, `enumerate`, `any`, `all` — plus comprehensions as a Stream-like idiom.

**Run:**

```bash
uv run python lesson_05/01_builtins.py
uv run python lesson_05/02_comprehensions.py
uv run python lesson_05/03_functional_style.py
```

---

## Builtins you will use daily

```python
len(nums)
min(nums), max(nums), sum(nums)
sorted(nums)                    # new list — original unchanged
sorted(scores, key=lambda n: scores[n])
```

| Call | Mutates? | Returns |
|------|----------|---------|
| `sorted(x)` | no | new `list` |
| `lst.sort()` | yes | `None` |

`sorted(d)` sorts **keys**. `sorted(d.items())` sorts `(key, value)` pairs.

```python
list(enumerate(items))    # [(0, a), (1, b), ...]
list(zip(names, scores))  # pairs — stop at shortest
any(pred(x) for x in xs)
all(pred(x) for x in xs)
```

> **Java:** `.stream().anyMatch()`, `IntStream.range`, `Comparator.comparing` via `key=`.

---

## List comprehensions

```python
evens = [n for n in nums if n % 2 == 0]
squares = [n * n for n in nums]
```

≈ `stream().filter().map().collect(toList())` — but **eager** (builds a list immediately).

### Dict and set comprehensions

```python
{word: len(word) for word in words}
{len(w) for w in words}                    # set comprehension
{k: sorted(v) for k, v in groups.items()}  # need .items() for k and v
```

Looping `for k, v in d` without `.items()` fails — dict iteration yields keys only.

### Generator expressions — lazy

```python
total = sum(n * n for n in nums if n % 2 == 1)
```

No brackets → lazy iterator, like a Stream pipeline consumed by `sum` / `any` / `max`.

### Nested flatten

```python
[x for row in matrix for x in row]
```

> **Key idea:** Comprehensions for transform/filter; plain `for` for side effects and complex logic.

---

## lambda, map, filter

```python
sorted(people, key=lambda p: p["age"])
list(map(str, nums))
list(filter(lambda n: n % 2 == 0, nums))
```

Prefer comprehensions over `map`/`filter` for readability in modern Python.

---

## Pause and practice

```bash
uv run python lesson_05/practice/01_builtins.py
uv run python lesson_05/practice/02_builtins.py
uv run python lesson_05/practice/03_comprehensions.py
```
---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_05/01_builtins.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/01_builtins.py)
- **Example:** [lesson_05/02_comprehensions.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/02_comprehensions.py)
- **Example:** [lesson_05/03_functional_style.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/03_functional_style.py)
- **Practice:** [lesson_05/practice/01_builtins.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/practice/01_builtins.py)
- **Practice:** [lesson_05/practice/02_builtins.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/practice/02_builtins.py)
- **Practice:** [lesson_05/practice/03_comprehensions.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_05/practice/03_comprehensions.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
