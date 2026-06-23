# Lesson 2 — Slicing

Slicing is how Python takes sub-ranges of sequences — the familiar idea of `subList` in Java, but more uniform and more powerful.

**Run:**

```bash
uv run python lesson_02/02_slicing.py
```

Work through the printed lines in order. Predict each line before you scroll the terminal.

## The slice grammar

```python
sequence[start:stop:step]
```

All parts are optional. **`stop` is exclusive** — like `range(start, stop)`.

```python
nums = [10, 20, 30, 40, 50]
nums[1:4]    # [20, 30, 40]  — index 1 up to but not including 4
nums[:3]     # first three
nums[2:]     # from index 2 to end
nums[:]      # shallow copy of the whole list
```

> **Java:** `list.subList(1, 4)` — same exclusive end index.

Dicts have **no** slice operator. Shallow copy with `{**d}`, `d.copy()`, or `dict(d)` — see Lesson 2 collections § spread/merge (`**` required inside `{ }` to unpack entries).

## Negative indices — count from the end

```python
nums[-1]     # 50 — last element (scalar, not a list)
nums[-3:]    # [30, 40, 50] — last three
nums[:-1]    # all but the last
nums[:-2]    # all but the last two — general: items[:-k] drops last k elements
```

Rule: index `k` when negative means `len(nums) + k`. A **negative stop** counts from the end: `[:-k]` is everything **before** the last `k` slots.

| Slice | On `[1, 2, 3, 4, 5]` |
|-------|------------------------|
| `[-2:]` | `[4, 5]` — last 2 |
| `[:-2]` | `[1, 2, 3]` — all but last 2 |

> **Java:** `list.subList(0, list.size() - k)` ≈ `items[:-k]`; `list.subList(list.size() - k, list.size())` ≈ `items[-k:]`.

## Step — stride and reverse

```python
nums[::2]     # every second element
nums[::-1]    # reversed copy
```

`[::-1]` appears again when emulating `lastIndexOf`: reverse, find first match, convert index back.

Slicing **never mutates** the original. `copy = nums[:]` then `copy[0] = 999` leaves `nums` unchanged.

> **Key idea:** A slice always returns a **new** sequence — it never mutates the original. Reach for a slice before writing an index loop.

## Patterns you will reuse

**Top n after sort:**

```python
n = 2
sorted(nums, reverse=True)[:n]   # the n largest
```

**Chunking:**

```python
size = 2
items = ["a", "b", "c", "d", "e"]
for i in range(0, len(items), size):
    chunk = items[i : i + size]
```

> **Java:** `subList(i, min(i+size, n))` in a loop — Python's slice in a `range` step loop is the idiomatic chunk pattern.

**Rotate right by k** (practice `rotate_right`):

```python
items[-k:] + items[:-k]   # last k elements first, then the rest
```

**Rotate left by k** (practice `rotate_left`):

```python
items[k:] + items[:k]     # from k to end, then the first k
```

When `k` is larger than `len(items)`, reduce with `k % len(items)` first (a full rotation changes nothing).

## Bridge to practice

Slicing shows up in `rotate_right`, `rotate_left`, `chunk`, and `every_other` exercises. When you implement them, ask: can I express this as a slice instead of a manual index loop?

Next practice file:

```bash
uv run python lesson_02/practice/02_collections.py
```

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_02/02_slicing.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/02_slicing.py)
- **Practice:** [lesson_02/practice/02_collections.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/practice/02_collections.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
