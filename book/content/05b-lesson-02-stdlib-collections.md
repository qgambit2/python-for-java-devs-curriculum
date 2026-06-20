# Lesson 2 — `collections` module (stdlib)

Built-in `list`, `dict`, `tuple`, and `set` cover most day-to-day work. The stdlib **`collections`** package adds specialized containers — roughly the extras you might reach for from Guava or `java.util` beyond the basics.

**Run:**

```bash
uv run python lesson_02/03_collections_stdlib.py
```

Prerequisites: `lesson_02/01_collections.py`.

---

## `defaultdict` — `computeIfAbsent` without boilerplate

```python
from collections import defaultdict

groups: defaultdict[str, list[str]] = defaultdict(list)
groups["aet"].append("eat")   # key created with empty list — no manual check
```

| Java | Python |
|------|--------|
| `map.computeIfAbsent(k, k -> new ArrayList<>()).add(x)` | `defaultdict(list)[k].append(x)` |
| count with `getOrDefault` + `put` | `defaultdict(int)` then `counts[k] += 1` |

The factory (`list`, `int`, `set`, or a custom callable) runs **once** when a missing key is first accessed.

---

## `Counter` — frequency map

```python
from collections import Counter

freq = Counter(["apple", "banana", "apple"])
freq["apple"]        # 2 — missing keys return 0
freq.most_common(2)  # [('apple', 2), ('banana', 1)]
```

≈ Guava `Multiset` or `stream.collect(Collectors.groupingBy(..., counting()))`.

---

## `deque` — double-ended queue (`ArrayDeque`)

```python
from collections import deque

dq = deque([10, 20, 30])
dq.appendleft(5)    # addFirst
dq.popleft()        # removeFirst — O(1)
```

`list.pop(0)` is **O(n)** (elements shift). Use `deque` when you need fast pops from **both** ends. `deque(maxlen=n)` gives a bounded sliding window.

> **Java:** `ArrayDeque` — `addFirst` / `removeFirst` / `addLast` / `removeLast`.

---

## `OrderedDict` — access-order preview

Plain `dict` keeps **insertion** order; reading a key does **not** move it. `OrderedDict` adds:

- `move_to_end(key)` — promote to MRU (tail)
- `popitem(last=False)` — evict LRU (front)

For LRU caches you can use **either**:

1. **`OrderedDict`** — `move_to_end` reads clearly
2. **Plain `dict`** — `val = d.pop(k); d[k] = val` on access (reinsert at tail)

Full walkthrough: `lesson_08/09_ordered_dict_lru.py` (both implementations).

> **Java:** `LinkedHashMap(accessOrder=true)`.

---

## On GitHub

- **Example:** [lesson_02/03_collections_stdlib.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/03_collections_stdlib.py)
- **LRU (dict + OrderedDict):** [lesson_08/09_ordered_dict_lru.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_08/09_ordered_dict_lru.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
