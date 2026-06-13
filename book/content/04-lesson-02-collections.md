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

The same `[]` syntax reads and writes. Writing always works; reading throws if the key is absent unless you use `.get()`.

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

### Spread / merge

`**` inside `{...}` unpacks key-value pairs:

```python
defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
{**defaults, **user}     # user wins on conflict
```

> **Java:** `new HashMap<>(defaults); putAll(user);` — right-hand keys overwrite.

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
