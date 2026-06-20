# Lesson 2 — Collections

Lists, dicts, tuples, and sets cover the majority of day-to-day Python — the same ground as `ArrayList`, `HashMap`, pairs, and `HashSet`, but with different syntax and a few surprises.

**Run:**

```bash
uv run python lesson_02/01_collections.py
```

Take it one section at a time. The file prints labeled blocks; match each block to the headings below.

---

## Lists — the ArrayList you already know

A **list** is ordered, mutable, and indexed from zero.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[0])   # apple
```

> **Java:** `List<String> fruits = new ArrayList<>(); fruits.add("date"); fruits.get(0);`

### Length — use `len()`, not `.size()`

Python has **no** `.size()` on lists (and no `.length()` like arrays or strings in Java). Use the built-in **`len()`**:

```python
len(fruits)   # 3 — works on list, str, dict, set, tuple, ...
```

| Java | Python |
|------|--------|
| `list.size()` | `len(list)` |
| `array.length` | `len(list)` |
| `string.length()` | `len(string)` |

`len` is a **function**, not a method on the object — one API for all sized types.

### indexOf becomes index — with a trap

```python
fruits.index("banana")   # first match — or ValueError if missing
"banana" in fruits       # safe membership test
```

Java's `indexOf` returns `-1` when absent. Python's `.index()` **raises** `ValueError`. The idiomatic guard is `in`.

For the **last** index, there is no `lastIndexOf`. A common trick (once you know slicing):

```python
len(fruits) - 1 - fruits[::-1].index("banana")
```

We return to `[::-1]` in the slicing chapter.

---

## Dicts — HashMap with insertion order

A **dict** maps keys to values. Literals use `{key: value}`.

### Reading and writing with brackets

```python
scores = {"alice": 95, "bob": 87}
scores["alice"]           # 95 — KeyError if missing
scores.get("carol", 0)    # 0 — like getOrDefault
order = {}
order["c"] = 3            # put — creates key without containsKey check
```

The same `[]` syntax reads and writes. Writing always works; reading raises `KeyError` on a missing key. Use `.get(key)` (returns `None`, like Java `null`) or `.get(key, default)` (like `getOrDefault`) instead.

> **Java:** `map.put("c", 3)` and `map.get("c")` — but `get` returns `null`, while `d["c"]` raises `KeyError`. Python is stricter on direct reads.

Insertion order is preserved when you iterate — like `LinkedHashMap`.

### Shallow copy — do not alias when you mean copy

```python
original = {"bob": 3, "carol": 7}
c = original.copy()      # new dict — same top-level keys/values
c["bob"] = 99
# original["bob"] still 3
```

Three equivalent styles appear in the lesson file:

```python
{**original}             # spread into new {}
dict(original)           # constructor — dict is a callable type
original.copy()          # method form — often clearest
```

`c = original` is **not** a copy. It is a second name for the same object.

> **Java:** `new HashMap<>(original)` for each form above. `{**d}` is like building a new map and `putAll`.

### Iterating a dict — what `list(d)` actually does

`list()` is not a special dict constructor. It accepts **any iterable** and collects what that iterable yields. When you iterate a dict, you get **keys only** — values are ignored:

```python
order = {"c": 3, "a": 1, "b": 2}
list(order)           # ["c", "a", "b"] — keys, insertion order
list(order.keys())    # same keys; .keys() is explicit
list(order.values())  # [3, 1, 2]
list(order.items())   # [("c", 3), ("a", 1), ("b", 2)]
```

> **Java:** `new ArrayList<>(map.keySet())` — but key order only if the map is `LinkedHashMap`. Python `dict` keeps insertion order (3.7+).

**Ordered dedupe** — a compact idiom once you know the above:

```python
items = ["b", "a", "b", "c", "a"]
list(dict.fromkeys(items))   # ["b", "a", "c"]
```

`dict.fromkeys(items)` builds `{"b": None, "a": None, "c": None}`. Dict keys must be unique, so later duplicates are dropped while **first-seen order** is kept. The `None` values are placeholders — we only want the key sequence, so `list(...)` extracts them.

> **Key idea:** `for k in d` and `list(d)` see keys. Need values? `d.values()`. Need pairs? `d.items()`.

For the same O(n) behavior with clearer steps, a `set` for “already seen” plus a result list is fine while you are learning (`lesson_02/practice/02_collections.py`, `dedupe_ordered`).

### Removal — list ends & dict entries

**Lists** — remove from ends or by value:

```python
stack = [10, 20, 30]
stack.pop()       # 30 — remove & return last (≈ ArrayDeque.removeLast)
stack.pop(0)      # 10 — remove & return first index
stack.remove(20)  # remove first matching value — ValueError if missing
```

**Dicts** — no `dict.remove(key)`. Java `map.remove(k)` maps to:

| Python | Returns | Notes |
|--------|---------|-------|
| `del d[k]` | nothing | `KeyError` if missing |
| `d.pop(k)` | **value** | optional default: `d.pop(k, None)` |
| `d.popitem()` | `(key, value)` | LIFO — last inserted; **no** `last=` on plain `dict` |
| Evict oldest (plain `dict`) | `k = next(iter(d)); del d[k]` | FIFO — `popitem(last=False)` is **OrderedDict** only |

**First key** without removing — O(1) on CPython when you only need the key:

```python
oldest_key = next(iter(d))
```

`iter(d)` and `next(...)` are **built-in functions**, not dict methods (≈ `map.keySet().iterator().next()`).

> **LRU caveat:** a plain `dict` keeps **insertion** order. Reading `d[k]` does **not** move `k` to the end. For access-order LRU, use delete+reinsert or `collections.OrderedDict.move_to_end` — see `lesson_08/09_ordered_dict_lru.py`.

### Spread / merge — `**` inside `{...}`

`**` inside a dict literal **unpacks** (spreads) another dict's key-value pairs into the new dict. Without `**`, you are **not** merging entries.

| Syntax | What it does |
|--------|----------------|
| `{**d}` | New dict with the same top-level entries as `d` (shallow copy) |
| `{**a, **b}` | Merge: start with `a`, overlay `b`; **right wins** on duplicate keys |
| `{d}` | **Not** a copy — Python treats this as a set literal; a dict is unhashable → `TypeError` |
| `{d.copy(), **b}` | **Wrong** — same problem; `d.copy()` without `**` does not spread |

**Rule of thumb:** inside `{ }`, a dict only contributes its **entries** when prefixed with `**`. Think Java `putAll`, not “put the whole map object as one value.”

**Shallow copy** (all three equivalent for a plain `dict`):

```python
{**original}
dict(original)
original.copy()
```

**Merge** (later `**` blocks overwrite earlier keys):

```python
defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
{**defaults, **user}     # {"theme": "dark", "lang": "en"}
```

> **Java:** `var out = new HashMap<>(defaults); out.putAll(user);` — right-hand keys overwrite.

### In-place merge — `dict.update()`

`out.update(other)` merges **into the existing dict** `out` (mutates it). It does **not** create a new dict and does **not** remove keys missing from `other`.

For each key in `other`:

- key already in `out` → value is **replaced**
- key not in `out` → entry is **added**

```python
out = {"theme": "light", "lang": "en"}
out.update({"theme": "dark", "notifications": True})
# out → {"theme": "dark", "lang": "en", "notifications": True}
```

Returns `None` — use `out` after the call. Also accepts keyword args: `out.update(theme="dark")`.

> **Java:** `out.putAll(other)` on a `HashMap`.

| Style | Creates new dict? | Mutates original? |
|-------|-------------------|---------------------|
| `{**a, **b}` | yes | no — `a` and `b` unchanged |
| `a.copy(); out.update(b)` | yes (via `copy`) | no — only `out` changes |
| `a.update(b)` | no | yes — `a` is modified in place |

Prefer **`{**a, **b}`** when you want a merged result without touching inputs (e.g. `merge_defaults`). Prefer **`update()`** when you are deliberately building or patching one dict over several steps.

**Filtered merge** (practice `merge_defaults` — ignore unknown user keys):

```python
def merge_defaults(defaults: dict, user: dict) -> dict:
    allowed = {k: user[k] for k in user if k in defaults}
    return {**defaults, **allowed}
```

These two are **not** equivalent:

```python
# ✓ spreads entries from defaults, then overlays filtered user keys
{**defaults, **{k: user[k] for k in user if k in defaults}}

# ✗ tries to put the whole dict object inside { } — TypeError
{defaults.copy(), **{k: user[k] for k in user if k in defaults}}
```

Imperative equivalent (same semantics):

```python
out = defaults.copy()
out.update({k: user[k] for k in user if k in defaults})
return out
```

All forms above are **shallow**: nested lists or dicts inside values are still shared. For deep trees, use `copy.deepcopy()` (later).

### Grouping with setdefault

```python
groups.setdefault(key, []).append(word)
```

> **Java:** `computeIfAbsent(key, k -> new ArrayList<>()).add(word)`

---

## Tuples — pairs, returns, and unpacking

A **tuple** is an immutable sequence. Often used for fixed small bundles:

```python
point = (3, 4)
person = ("Alice", 30, "alice@example.com")
```

### Unpacking — assign positions to names

```python
x, y = point
name, age, email = person
low, high = min_max([3, 1, 4])
```

A function that returns two numbers returns **one tuple**:

```python
def min_max(nums):
    return min(nums), max(nums)   # comma builds one tuple
```

> **Java:** you would introduce `MinMax`, `Pair`, or an `int[]`. Python callers unpack at the call site.

### One-element tuples — the comma rule

Parentheses do not make a tuple. **Commas do.**

```python
type((42))    # int
type((42,))   # tuple with one element
x, = (42,)    # unpack — comma on the left too
```

`return 42` returns an int; `return 42,` returns a one-tuple.

### Starred unpack for “the rest”

```python
first, *rest = (42, 33, 5)   # rest is [33, 5] — always a list
first, *_ = (42, 33, 5)      # ignore the rest
```

`x, = (42, 33, 5)` fails — only one target on the left.

### Index when you need one slot

```python
person[1]   # second value — zero-based, like arrays
```

---

## zip — pairs, dicts, and matrix transpose

`zip(a, b)` pairs elements by position into **tuples**:

```python
list(zip(["a", "b"], [1, 2]))   # [('a', 1), ('b', 2)]
dict(zip(["a", "b"], [1, 2]))   # {'a': 1, 'b': 2}
```

`zip` alone is an **iterator**. Use it in a `for` loop, or wrap with `list()` when you need indexing or reuse.

Already have pairs? `dict(pairs)` builds the map directly.

### Transpose with zip(*matrix)

```python
matrix = [[1, 2, 3], [4, 5, 6]]
[list(col) for col in zip(*matrix)]
# [[1, 4], [2, 5], [3, 6]]
```

`*` unpacks each row as a separate argument to `zip`. `zip` then groups by **column**. That is matrix **transpose** (rows and columns swap), not a 90-degree rotation.

> **Java:** nested loops `out[c][r] = matrix[r][c]` — or streams with indices. Python one-liner is idiomatic once `*` clicks.

---

## Sets — HashSet with operators

Sets are unordered collections of unique elements.

```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # union:        {1, 2, 3, 4, 5}
a & b   # intersection: {3}
a - b   # difference:   {1, 2}
a ^ b   # symmetric:    {1, 2, 4, 5}
```

**Identity worth remembering:**

```python
(a | b) - (a & b) == a ^ b   # always True for sets
```

Union minus overlap equals symmetric difference.

Lists use `+` for concatenation (duplicates stay). Sets use `|` for union (deduped).

> **Java:** `Sets.union`, `retainAll`, `removeAll`, `symmetricDifference`.

---

## Preview: generator inside `sorted()` (round-2 practice)

In `lesson_02/practice/02_collections.py` you will filter dict entries and sort names. **Both forms work** — prefer the one **without** `[]`:

```python
sorted([name for name, score in after.items() if before.get(name, 0) != score])
sorted(name for name, score in after.items() if before.get(name, 0) != score)  # preferred
```

Brackets build a list first; the bare `name for ...` is a **generator** fed straight to `sorted()` — no extra allocation. Full explanation in **Lesson 5 — Builtins, comprehensions, and functional style**.

> **Java:** `Stream.filter(...).sorted()` without an intermediate `.collect(toList())`.

### Preview: sort by tuple key (`rare_words` exercise)

Sort by **count first**, then **word** for ties — pass a **tuple** to `key=`:

```python
sorted(word_counts.keys(), key=lambda w: (word_counts[w], w))[:k]
```

Python compares tuples left to right: lower count first; if counts match, alphabetical word order.

> **Java:** `Comparator.comparingInt((String w) -> counts.get(w)).thenComparing(w -> w)` — same two-level sort. For large lists and small `k`, see **Lesson 5** § `heapq.nsmallest` (≈ `PriorityQueue` / partial top-k).

---

## Pause and practice

You have seen a lot of syntax in one lesson. Before slicing, run the file once end-to-end, then open practice:

```bash
uv run python lesson_02/practice/01_collections.py
uv run python lesson_02/practice/02_collections.py
```

If a line surprises you, find it in `lesson_02/01_collections.py` and change it. Prediction before execution is how you build Python reflexes.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_02/01_collections.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/01_collections.py)
- **Example:** [lesson_02/basics.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/basics.py)
- **Practice:** [lesson_02/practice/01_collections.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/practice/01_collections.py)
- **Practice:** [lesson_02/practice/02_collections.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/practice/02_collections.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
