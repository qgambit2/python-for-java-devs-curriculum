# Performance — making slow Python fast

Your algorithm can have the right big-O and still run several times too slow. This chapter is about the gap between "correct complexity" and "fast on CPython" — the constant factors that the JVM's JIT used to hide from you, and that you now manage by hand.

The theme throughout: when a piece of work sits inside a hot loop, CPython pays for it on *every* iteration. Removing that work doesn't change the big-O, but it can cut wall-clock time dramatically.

**Run (paste any snippet into a file, or use the one-liners):**

```bash
uv run python -m timeit -s 'data=list(range(1000))' 'sum(data)'
```

---

## The mental model: no JIT

The single biggest shift coming from Java: **CPython has no Just-In-Time compiler.** It is a straight bytecode interpreter. It does not profile your hot loops, it does not inline, and — crucially — it does not hoist loop-invariant expressions out of loops for you.

| | JVM (HotSpot) | CPython |
|------|---------------|---------|
| Hot loops | JIT-compiled to native after ~10k iterations | interpreted every iteration, forever |
| Loop-invariant code | hoisted automatically | runs every iteration as written |
| Inlining | yes | no |
| Method/field lookup | devirtualized, cached | dict lookup every time |

> **Java:** in Java you can write `obj.field` or recompute `a.length()` inside a loop and trust the JIT to hoist it. In Python that lookup *executes* on every pass. Optimizations the JIT did silently are now things **you** do deliberately.

This is why most of this chapter is one idea in different costumes: **stop doing redundant work in the hot loop** — in CPython, redundant work is never free.

---

## Step 0: measure before you touch anything

Premature optimization in Python is the same sin as in Java — guess wrong about the bottleneck and you complicate code for nothing. Measure first.

```python
import timeit

# micro-benchmark a single expression
timeit.timeit("sum(data)", setup="data=list(range(1000))", number=10000)
```

For finding *which* function is the bottleneck, use the profiler:

```bash
uv run python -m cProfile -s cumulative my_script.py
```

> **Java:** `timeit` ≈ JMH (without the warmup/fork machinery, because there is no JIT warmup to wait for). `cProfile` ≈ async-profiler or your IDE's sampling profiler. The workflow is identical: profile, find the hot path, optimize *that*, re-measure.

> **Key idea:** big-O tells you how the cost *scales*; the profiler tells you where the *constant* is. You need both.

---

## Hoist loop invariants by hand

Anything inside your hottest loop that does not change between iterations should be computed once, *above* the loop. The hotter the loop, the bigger the win — the inner loop of a nested O(n²) scan runs about n² times, so a single redundant operation gets multiplied by ~250,000 at n=500.

Here a value that depends only on the outer index `i` is recomputed on every inner pass:

```python
# Before — data[i] * 2 is recomputed on every inner iteration (n² times total)
for i in range(n):
    for j in range(n):
        if data[j] == data[i] * 2:
            handle(i, j)

# After — compute the i-dependent part once per outer pass (n times total)
for i in range(n):
    want = data[i] * 2        # invariant w.r.t. the inner loop — lifted out
    for j in range(n):
        if data[j] == want:
            handle(i, j)
```

Each `data[i]` is a real `__getitem__` call under the hood, not a cheap array dereference, and the multiply runs every pass too. Lifting it out turns ~n² operations into ~n.

> **Java:** the JIT would have hoisted `data[i] * 2` automatically once it proved the value loop-invariant. CPython will not — so you write the hoist yourself.

---

## Bind hot attributes and methods to locals

Local-variable access is the fastest name lookup CPython has (`LOAD_FAST`, a C-array index). Global and attribute lookups (`LOAD_GLOBAL`, `LOAD_ATTR`) walk dictionaries every time. In a tight loop, binding a method to a local name once is a measurable win.

```python
# Slow — attribute lookup of .append every iteration
result = []
for x in data:
    result.append(transform(x))

# Faster — bind the bound method once
result = []
append = result.append
for x in data:
    append(transform(x))
```

The same applies to module-level functions you call in a loop (`local_sqrt = math.sqrt`).

> **Java:** there is no parallel — the JVM resolves and caches call sites for you. This trick is pure CPython interpreter mechanics. Reach for it only in a proven hot loop; elsewhere it just hurts readability.

---

## Let C do the work: built-ins and comprehensions

CPython's built-ins (`sum`, `min`, `max`, `any`, `all`, `sorted`, `map`) and comprehensions run their loops in compiled C, not interpreted bytecode. A `for` loop that accumulates in Python pays interpreter overhead per element; the C-level equivalent does not.

```python
total = 0
for x in data:          # interpreted loop
    total += x

total = sum(data)       # C loop — same result, far less overhead
```

```python
# Comprehension: the loop runs in C, and it pre-sizes the list
squares = [x * x for x in data]          # faster than append in a Python loop
evens   = [x for x in data if x % 2 == 0]
```

> **Java:** comprehensions feel like Streams (`data.stream().map(...).collect(...)`), but the performance reason differs. Streams help via laziness and potential parallelism; comprehensions help because the iteration drops out of the interpreter into C. Prefer a comprehension over a manual `append` loop whenever you are *building a collection*.

### The catch: built-ins win only past a threshold

The C loop is faster *per element*, but calling the built-in has a **fixed setup cost** — the function call, building and consuming an iterator. That cost only pays off once there are enough elements to amortize it. On a tiny, fixed number of values, the plain operator wins.

```python
s = a + b + c            # three known scalars → just add; fastest and clearest
s = sum((a, b, c))       # slower — allocates a 3-tuple AND pays sum's call overhead

total = sum(big_list)    # a collection you already have → sum wins easily
```

Reaching for `sum((a, b, c))` is the trap: you allocate a throwaway tuple *and* pay the call overhead to replace two `+` operations. If that line sits in a hot loop, you allocate a fresh tuple every iteration — the opposite of fast. The rule is "let C iterate over a *meaningful number of elements*," not "avoid operators."

> **Key idea:** "use the C built-in" carries an unstated "...over enough elements to amortize the call." Combining a handful of scalars you'd otherwise write with `+`? Use `+`.

---

## Pick the data structure for the operation

Wrong container turns an O(1) operation into O(n). This is the most common way an "O(n) algorithm" is secretly O(n²).

```python
seen = set(haystack)        # O(1) membership
if needle in seen: ...

if needle in haystack_list: # O(n) — scans the whole list every time
```

| Operation | Wrong choice | Right choice |
|-----------|--------------|--------------|
| Membership test (`x in c`) | `list` — O(n) | `set` / `dict` — O(1) |
| Queue: pop from front | `list.pop(0)` — O(n) shift | `collections.deque.popleft()` — O(1) |
| Count occurrences | manual `dict` + `get` | `collections.Counter` |
| Repeated min-extraction | `sorted()` each time | `heapq` |

> **Java:** identical instincts — `HashSet.contains` over `ArrayList.contains`, `ArrayDeque` over removing from the head of an `ArrayList`. The complexity table is the same; only the names change (`deque` ≈ `ArrayDeque`, `Counter` ≈ `Map<T,Long>` via `groupingBy(counting())`).

---

## Build strings with `join`, never `+=` in a loop

Strings are immutable in Python, exactly as in Java. `s += piece` in a loop allocates a brand-new string each iteration and copies everything so far — classic accidental O(n²).

```python
# O(n²) — new string allocated and copied every iteration
s = ""
for piece in pieces:
    s += piece

# O(n) — collect, then join once
s = "".join(pieces)
```

> **Java:** this is the `String +=` in a loop vs `StringBuilder` lesson, one-to-one. Python's `"".join(iterable)` *is* the `StringBuilder` — it sizes the buffer once and copies each piece a single time. (CPython sometimes optimizes a simple `s += ` in narrow cases, but never rely on it — `join` is the contract.)

---

## Cache repeated work: memoization

When a pure function is called repeatedly with the same arguments, cache it. `functools.lru_cache` (or `functools.cache` for an unbounded version) turns exponential recomputation into linear with one decorator.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

> **Java:** equivalent to memoizing into a `HashMap` by hand, or Guava's `CacheBuilder`. The decorator does the map-lookup-or-compute dance for you; arguments must be hashable (the cache key), just as map keys must implement `hashCode`.

---

## Stop early when the answer can't improve

If you can prove you have found the best possible result, return immediately — don't run the rest of the loops. Searching for a pair that sums to a target, an exact hit is unbeatable, so there is nothing left to check:

```python
def find_pair(pairs, target):
    for a, b in pairs:
        if a + b == target:
            return (a, b)        # exact match — stop scanning
    return None
```

In a nested search, returning instead of merely `break`-ing the inner loop skips *all* the remaining outer work too. Early exit changes nothing about the worst case, but real inputs often hit the answer long before the end.

> **Java:** same instinct as returning out of nested `for` loops (or a labelled `break`) the moment a result is found, rather than setting a flag and finishing the iteration.

---

## Avoid in-band sentinels

A subtle bug that is *also* a small performance smell: using a real-looking value to mean "nothing recorded yet."

```python
best = 10000          # means "no result yet" ... until a real result is 10000
for candidate in candidates:
    if score(candidate) < score_of(best):
        best = candidate
```

If some legitimate candidate genuinely has the value `10000`, your "empty" marker is indistinguishable from a real answer — a correctness bug. And every iteration pays for the extra guard you inevitably add to special-case the sentinel. Use a value that can never be a real result, or seed with a genuine first candidate:

```python
best = None                       # out-of-band marker + an explicit guard
best_score = float("inf")         # no real distance equals infinity
# or simply seed best with the first real element before the loop
```

> **Java:** the in-band sentinel is the `return -1` / `Integer.MIN_VALUE` anti-pattern. The Python-clean equivalents are `float('inf')` for distances/bounds and `None` with an explicit guard — values that can never be a legitimate result.

---

## Putting it together

None of the techniques in this chapter improve big-O — they attack the constant factor. The recurring question is always the same:

| Technique | What it removes from the hot loop |
|-----------|-----------------------------------|
| Hoist loop invariants | repeated computation that never changes |
| Bind methods/globals to locals | repeated dict-based name lookups |
| Built-ins & comprehensions | per-element interpreter overhead |
| Right data structure | accidental O(n) inside an O(n) loop |
| `join` over `+=` | repeated string reallocation/copy |
| Memoization | repeated calls with identical arguments |
| Early exit | the entire remaining search |

> **Key idea:** once your big-O is optimal but you are still slow, the question is always *"what am I recomputing inside the hottest loop that doesn't change?"* — because unlike the JVM, CPython will not hoist it for you.

---

## Pause and practice

Compare `join` against `+=` accumulation directly:

```bash
uv run python -m timeit -s 's=[str(i) for i in range(1000)]' '"".join(s)'
uv run python -m timeit -s 's=[str(i) for i in range(1000)]' 'r=""
for x in s: r+=x'
```

Then, in your own code:

1. Find a loop that recomputes something invariant and lift it out; `timeit` before and after.
2. Replace one `x in some_list` membership test with a `set`.
3. Rewrite one `s += piece` accumulation loop as `"".join(...)`.

Measure each change — the goal is to build the instinct of *seeing* the hot loop, not to optimize blindly.
