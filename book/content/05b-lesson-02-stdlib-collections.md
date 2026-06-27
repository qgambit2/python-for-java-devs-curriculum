# Lesson 2 — `collections` module (complete tour)

Built-in `list`, `dict`, `tuple`, and `set` cover most day-to-day work. The stdlib **`collections`** package adds nine specialized container types — ships with Python, **no pip install**. You `import` them explicitly (unlike built-in `dict`).

**Run:**

```bash
uv run python lesson_02/03_collections_stdlib.py
```

Prerequisites: `lesson_02/01_collections.py`.

---

## Overview

| Type | One-line purpose |
|------|------------------|
| `defaultdict` | `dict` that auto-creates missing keys |
| `Counter` | frequency / multiset counts |
| `deque` | fast queue at **both** ends |
| `OrderedDict` | `move_to_end`, `popitem(last=False)` |
| `namedtuple` | immutable record with named fields |
| `ChainMap` | lookup across a **stack** of dicts |
| `UserDict` / `UserList` / `UserString` | safe wrappers for subclassing |

> **Java:** built-ins ≈ `ArrayList` / `HashMap` / `HashSet`; `collections` ≈ `ArrayDeque`, `LinkedHashMap` patterns, Guava `Multiset`, stacked property sources.

**Not in this lesson:** `collections.abc` (`Mapping`, `Sequence`, …) — abstract base classes for typing and protocols; covered in later lessons.

---

## `defaultdict` — `computeIfAbsent`

`defaultdict(factory)` subclasses `dict`. On a missing key it calls `factory()` and **stores** the result.

```python
from collections import defaultdict

groups: defaultdict[str, list[str]] = defaultdict(list)
groups["aet"].append("eat")   # key created with [] — no if-check

hits: defaultdict[str, int] = defaultdict(int)
hits["home"] += 1             # missing → 0, then increment
```

| Java | Python |
|------|--------|
| `computeIfAbsent(k, k -> new ArrayList<>()).add(x)` | `defaultdict(list)[k].append(x)` |
| count with `getOrDefault` + `put` | `defaultdict(int)` then `counts[k] += 1` |

**Details:**

- Factory can be `list`, `int`, `set`, or any **zero-arg callable**.
- `.get(key, default)` does **not** trigger the factory (key stays absent).
- `dict(dd)` converts to a plain dict when done building.

---

## `Counter` — frequency map

`Counter` is a `dict` subclass: keys = elements, values = integer counts.

```python
from collections import Counter

freq = Counter(["apple", "banana", "apple"])
freq["apple"]           # 2
freq["missing"]         # 0 — returns 0, does NOT insert
freq.most_common(2)     # [('apple', 2), ('banana', 1)]
list(freq.elements())   # repeats each key by its count
```

**Multiset math:** `c1 + c2` (add counts), `c1 - c2` (drop zero/negative), `c1 & c2` (min), `c1 | c2` (max).

≈ Guava `Multiset` or `Collectors.groupingBy(..., counting())`.

---

## `deque` — `ArrayDeque`

Doubly-linked blocks — **O(1)** `append` / `pop` at **both** ends. `list.pop(0)` is **O(n)**.

```python
from collections import deque

dq = deque([10, 20, 30])
dq.appendleft(5)      # addFirst
dq.popleft()          # removeFirst
dq.extend([40, 50])
dq.rotate(1)          # circular shift right

window = deque(maxlen=3)   # bounded — auto-evicts oldest
```

| deque | list |
|-------|------|
| O(1) both-end push/pop | O(1) end only; O(n) at front |
| O(n) random index | O(1) index |

> **Java:** `ArrayDeque` — `addFirst` / `removeFirst` / `addLast` / `removeLast`.

---

## `OrderedDict` — access-order hooks

Since 3.7, plain `dict` keeps insertion order. `OrderedDict` still adds:

- `move_to_end(key, last=True|False)` — promote or demote in order
- `popitem(last=False)` — FIFO evict (**plain `dict.popitem()` has no `last=`**)
- Order-sensitive `==` between `OrderedDict` instances

```python
from collections import OrderedDict

od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")              # MRU tail
k, v = od.popitem(last=False)    # LRU front
```

LRU cache — two approaches in `lesson_08/09_ordered_dict_lru.py`:

1. `OrderedDict` + `move_to_end`
2. Plain `dict` + `pop` / reinsert on access

> **Java:** `LinkedHashMap(accessOrder=true)`.

---

## `namedtuple` — lightweight record

Factory for an **immutable** tuple subclass with named fields.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x, p[0]              # attribute and index
p2 = p._replace(x=10)  # new instance — original unchanged
p._asdict()            # field → value mapping
```

≈ Java `record Point(int x, int y)` or `Map.entry`. For mutable classes with methods → Lesson 8 `@dataclass`.

---

## `ChainMap` — layered dict lookup

`ChainMap(m1, m2, …)` searches left-to-right; **first hit wins**. Writes/deletes only the **leftmost** map.

```python
from collections import ChainMap

defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
settings = ChainMap(user, defaults)

settings["theme"]   # dark — from user
settings["lang"]    # en — from defaults
```

`new_child()` pushes a fresh dict on the left (scope chain). ≈ stacked config / `Properties` with parent defaults.

---

## `UserDict` / `UserList` / `UserString`

Wrappers with a `.data` attribute holding the inner `dict` / `list` / `str`. Use when **subclassing** built-ins would fight C-level method implementations.

```python
from collections import UserDict

class LowerDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
```

≈ Java `AbstractMap` / `AbstractList` — extend the wrapper, not the raw C-backed type.

---

## Cheat sheet

| Reach for | When |
|-----------|------|
| `defaultdict` | grouping, nested lists/sets, auto-zero counts |
| `Counter` | word freq, vote tallies, multiset diff |
| `deque` | BFS queue, sliding window, undo stack at both ends |
| `OrderedDict` | explicit LRU / FIFO eviction |
| `namedtuple` | small frozen data bag before you need a full class |
| `ChainMap` | config layers, scoped overrides |
| `UserDict`/`UserList` | custom mapping/sequence behavior via inheritance |
| `heapq` | top-k, priority queue, repeatedly pull the smallest |
| `bisect` | binary search / insertion point on a **sorted** list |

---

## heapq — min-heap (`PriorityQueue`)

**Not** in `collections` — `import heapq`. Operates on a **list in place**; `h[0]` is always the smallest.

```python
import heapq

heapq.heapify(nums)       # build heap O(n)
heapq.heappush(h, x)      # offer — O(log n)
heapq.heappop(h)          # poll min — O(log n)
heapq.nsmallest(k, data)  # top-k smallest
heapq.nlargest(k, data)   # top-k largest
```

**Max-heap:** negate values, or use `nlargest`. **Custom priority:** push `(priority, item)` tuples — compared left-to-right.

> **Java:** `PriorityQueue` — default min-heap; `offer` / `poll` / `peek`.

> **Key idea:** `heapq` is **functions over a plain list**, not a class. `h[0]` is the min; there is **no max-heap** — negate values or use `nlargest`.

**Lesson:** `lesson_02/04_heapq.py`

---

## bisect — binary search on a sorted list

Like `heapq`, **`bisect`** is functions over a plain list — but the list must already be **sorted**. It finds, in `O(log n)`, the index where a value belongs.

```python
import bisect

a = [10, 20, 30, 40, 50]

bisect.bisect_left(a, 30)    # 2 — leftmost spot for 30
bisect.bisect_right(a, 30)   # 3 — rightmost spot (just past equal items)
bisect.insort(a, 35)         # insert keeping order -> [10, 20, 30, 35, 40, 50]
```

> **Java:** `Collections.binarySearch(list, key)` / `Arrays.binarySearch(arr, key)`.

### Two differences that bite Java developers

**1. The return value means different things.** `bisect` **always** returns a non-negative *insertion point* — it never signals "found" or "not found." Java's `binarySearch` returns the **found index** when present, or a **negative encoded miss** `-(insertion point) - 1` when absent. So a Java dev's "negative means not found" reflex does not transfer:

```python
a = [10, 20, 30]
i = bisect.bisect_left(a, 25)   # 2 — NOT -3; 25 is absent but you only get the slot
found = i < len(a) and a[i] == 25   # you check membership yourself
```

```java
int i = Collections.binarySearch(list, 25);   // -3  (= -(2) - 1)
boolean found = i >= 0;                        // Java tells you directly
int insertionPoint = i >= 0 ? i : -(i + 1);    // decode the miss
```

**2. Duplicates are explicit, not arbitrary.** `bisect_left` lands **before** equal elements, `bisect_right` **after** — so you can find the first or last occurrence deterministically. Java's `binarySearch` returns *some* matching index when duplicates exist, with **no guarantee** which one.

| Goal | Python `bisect` | Java |
|------|-----------------|------|
| Find insertion index | `bisect_left(a, x)` / `bisect_right(a, x)` | `binarySearch` then decode `-(i+1)` on miss |
| "Is `x` present?" | `i = bisect_left(a, x); a[i:i+1] == [x]` | `binarySearch(...) >= 0` |
| Insert keeping order | `bisect.insort(a, x)` | `binarySearch` + `list.add(idx, x)` (no one-call form) |
| Search by a field | `bisect_left(a, x, key=...)` (3.10+) | `binarySearch(list, key, Comparator)` |
| Count items `< x` | `bisect_left(a, x)` | manual |

> **Key idea:** `bisect` finds **where a value goes**, not **whether it is there**. The list must be sorted first; the result is always a valid index, so test `a[i] == x` yourself to confirm membership.

**Lesson:** `lesson_08/08_collections_and_sorting.py` (§ bisect on a sorted list)

---

## Practice

```bash
uv run python lesson_02/practice/03_collections_stdlib.py
uv run python lesson_02/practice/04_heapq.py
```

---

## On GitHub

- **Example:** [lesson_02/03_collections_stdlib.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/03_collections_stdlib.py)
- **Example:** [lesson_02/04_heapq.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/04_heapq.py)
- **Practice:** [lesson_02/practice/03_collections_stdlib.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/practice/03_collections_stdlib.py)
- **LRU (dict + OrderedDict):** [lesson_08/09_ordered_dict_lru.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/09_ordered_dict_lru.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
