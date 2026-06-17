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

> **Java:** `list.size()` → `len(list)`; `Collections.min/max` → `min`/`max` builtins. No `.size()` on Python lists — `len()` is the single length function for lists, strings, dicts, and sets.

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

### `sorted(..., key=...)` — one field or many

**Single field** — sort dict keys by their value in another map:

```python
sorted(scores, key=lambda name: scores[name])
```

**Multiple fields (tie-breakers)** — return a **tuple** from `key`. Python compares element by element (like `thenComparing`):

```python
# rarest words first: lowest count, then alphabetical (lesson_02/practice/02_collections.py)
sorted(word_counts.keys(), key=lambda w: (word_counts[w], w))

# people: age first, name for ties
sorted(people, key=lambda p: (p["age"], p["name"]))
```

| Python | Java |
|--------|------|
| `key=lambda w: (word_counts[w], w)` | `Comparator.comparingInt(w -> counts.get(w)).thenComparing(w -> w)` |
| `key=lambda p: (p["age"], p["name"])` | `Comparator.comparing(Person::getAge).thenComparing(Person::getName)` |

Use `reverse=True` when you want descending order on the whole sort key.

### `heapq` — top-k without sorting everything

For **small k, large n**, sorting the whole collection is wasteful. The **`heapq`** module (stdlib — `import heapq`) implements a **min-heap** — the same idea as Java’s **`PriorityQueue`**.

```python
import heapq

nums = [5, 1, 9, 2, 7, 1]

heapq.nsmallest(3, nums)                    # [1, 1, 2] — three smallest
heapq.nlargest(2, nums)                     # [9, 7]    — two largest

# Same key= as sorted — rare_words-style (lesson_02/practice/02_collections.py)
word_counts = {"aa": 1, "bb": 2, "cc": 2}
heapq.nsmallest(2, word_counts.keys(), key=lambda w: (word_counts[w], w))
# ['aa', 'bb']
```

| Approach | When | Rough cost |
|----------|------|------------|
| `sorted(xs, key=...)[:k]` | Small data, clarity, no import | O(n log n) |
| `heapq.nsmallest(k, xs, key=...)` | Large **n**, small **k** | O(n log k) |

**Manual heap** (like using `PriorityQueue` directly):

```python
import heapq

h = [5, 1, 9, 2]
heapq.heapify(h)          # rearrange list in-place into a min-heap
heapq.heappush(h, 0)      # offer(0)
heapq.heappop(h)          # poll() → 0 (smallest)
```

> **Java:** `PriorityQueue` (min-heap by default; pass `Comparator` for custom order). `heapq.nsmallest(k, xs)` ≈ stream sort + `limit(k)` for small exercises; for huge data ≈ maintaining a size-k priority queue or Guava `Ordering.leastOf(k, iterable)`. Python’s heap is **in a list** you pass to `heapq` functions — there is no separate `PriorityQueue` class in the stdlib.

**Lesson 2 practice** allows dict builtins only (no `heapq`). Use `sorted(...)[:k]` there; reach for `heapq` in production when performance matters.

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

No brackets → lazy iterator, like a Stream pipeline consumed by `sum` / `any` / `max` / `sorted`.

### `sorted([...])` vs `sorted(x for x in ...)` — both work; omit `[]` when you can

When a comprehension is only passed to a builtin that walks the iterable **once**, prefer a **generator** (no square brackets):

```python
before = {"alice": 50, "bob": 70}
after = {"alice": 50, "bob": 65, "carol": 40}

# Both return ["bob", "carol"] — same result
sorted([n for n, s in after.items() if before.get(n, 0) != s])
sorted(n for n, s in after.items() if before.get(n, 0) != s)   # preferred
```

| Form | Behavior |
|------|----------|
| `[x for x in xs if p(x)]` | **List comprehension** — builds the full list first |
| `x for x in xs if p(x)` inside `sorted(...)` | **Generator** — yields items on demand |

**Why skip `[]`?** `sorted()` will collect everything anyway. The list form allocates an intermediate list you do not need if you only use the result once.

Same rule for `any(...)`, `all(...)`, `sum(...)`, `max(...)`, `min(...)`.

> **Java:** like piping a `Stream` into `.sorted()` without `.collect(toList())` in between when you only need the sorted output once.

**Keep `[]` when:** you need the filtered list twice, index it before sorting, or return the list itself (not only passing it to one function).

You first meet this pattern in `lesson_02/practice/02_collections.py` (`score_changes`); Lesson 5 is the full treatment.

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
