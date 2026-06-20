"""Lesson 1c — collections: list, dict, tuple, set.

Java: ArrayList, HashMap/LinkedHashMap, Pair/tuple, HashSet — all in one place.

Run:
    uv run python lesson_02/01_collections.py
"""

from __future__ import annotations


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. list — ArrayList")

fruits = ["apple", "banana", "cherry", "banana"]
fruits.append("date")
print(fruits[0])

# indexOf / lastIndexOf — Java: list.indexOf(x), list.lastIndexOf(x)
#
#   lst.index(x)       first index of x — missing → ValueError (not -1)
#   x in lst           membership — like indexOf != -1
#   lst.index(x, start)   optional start index (like indexOf(x, fromIndex))
#
# No built-in lastIndexOf. Idiom: reverse a copy, find first, convert index:
#   len(lst) - 1 - lst[::-1].index(x)
#   [::-1] = reversed copy (see lesson_02/02_slicing.py for full walkthrough)
#   Mirror: original index i  ↔  reversed index (len - 1 - i)

print(fruits.index("banana"))                          # 1 — first (≈ indexOf)
print("banana" in fruits)                              # True
print(len(fruits) - 1 - fruits[::-1].index("banana"))  # 3 — last (≈ lastIndexOf)

# Remove from ends & by value — Java: remove(int), remove(Object), removeLast/removeFirst (Deque)
#
#   lst.pop()       remove & return LAST element — ArrayDeque.removeLast()
#   lst.pop(0)      remove & return at index 0 — removeFirst / remove(0)
#   lst.remove(x)   remove first matching VALUE — ValueError if missing (not boolean)
#
# No list.remove() with no args — unlike dict.popitem().

stack = [10, 20, 30]
print(stack.pop())       # 30 — last
print(stack.pop(0))      # 10 — first
stack.remove(20)         # by value
print(stack)             # []


section("2. dict — HashMap + LinkedHashMap insertion order")

# Bracket notation for dicts (same syntax as lists, different meaning):
#
#   d[key] = value   insert or UPDATE  — Java: map.put(key, value)
#   d[key]           READ (key must exist) — missing key → KeyError (not null)
#   d.get(key, default)   safe READ — Java: map.getOrDefault(key, default)
#
# You do NOT need "if key not in d" before assigning; a new key is created automatically.
# Literal: {"alice": 95}  —  empty: {}  (not set(); use set() or {1, 2} for sets)

scores = {"alice": 95, "bob": 87}
print(scores["alice"])          # read — KeyError if "alice" missing
print(scores.get("carol", 0))   # read with default — no KeyError
print(scores.keys())
print(sorted(scores))           # sorted(keys), not insertion order

order: dict[str, int] = {}
order["c"] = 3                  # put — creates key "c"
order["a"] = 1
order["b"] = 2
print(list(order.keys()))       # insertion order: c, a, b (≈ LinkedHashMap)
order["a"] = 99                 # put — overwrites existing key, order unchanged
print(list(order.keys()))       # still c, a, b
print({"b": 2, "a": 1} == {"a": 1, "b": 2})

# list(dict) — list() iterates any iterable; iterating a dict yields KEYS only (not values)
#   list(order) == list(order.keys())  —  Java: new ArrayList<>(linkedHashMap.keySet())
# Ordered dedupe: list(dict.fromkeys(["b", "a", "b", "c"]))  →  ["b", "a", "c"]
#   fromkeys: {key: None, ...} — None is placeholder; we only want the key sequence

# Shallow copy — three equivalent ways (new dict; original unchanged when copy is mutated)
#
#   WRONG:  c = original          same object — c["bob"]=99 changes original too
#   RIGHT:  c = original.copy()   new dict — shallow copy (values shared if mutable)
#
# Loop syntax:
#   for copy_fn in (fn1, fn2, fn3):   tuple of callables; each iteration copy_fn = next fn
#   c = copy_fn(original)             CALL copy_fn with one argument — like fn.apply(original)
#
# Three copy_fn values (same outcome for flat dicts with int values):
#
#   1. lambda d: {**d}
#        lambda d: expr  — anonymous function; d is the PARAMETER (defined here, not elsewhere)
#        {**d}           — dict spread/unpack: copy all key→value pairs into a new {}
#        copy_fn(original)  →  d=original, returns {**original}
#
#   2. dict
#        dict is the dict CLASS — types are callable in Python (like a constructor reference)
#        copy_fn(original)  →  dict(original)  — Java: new HashMap<>(original)
#
#   3. dict.copy
#        bound .copy method — copy_fn(original)  →  dict.copy(original) ≈ original.copy()
#
original = {"bob": 3, "carol": 7}
for copy_fn in (lambda d: {**d}, dict, dict.copy):
    c = copy_fn(original)       # new shallow copy each iteration
    c["bob"] = 99               # mutate copy only
    assert original["bob"] == 3 # original untouched
print(original, "ok — shallow copies don't mutate source")

def merge_scores(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    result = right.copy()
    for name, score in left.items():
        result[name] = result.get(name, 0) + score
    return result

left = {"alice": 10, "bob": 5}
right = {"bob": 3, "carol": 7}
print(merge_scores(left, right))
print(left, right)

groups: dict[str, list[str]] = {}
for word in ["eat", "tea", "tan"]:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)
print(groups)
print({k: sorted(v) for k, v in groups.items()})

defaults = {"theme": "light", "lang": "en", "notifications": True}
user = {"theme": "dark"}
print({**defaults, **user})


section("2b. dict — removal; first & last key (insertion order)")

# No dict.remove(key) — Java map.remove(k) maps to del / pop / popitem, not .remove()
#
#   del d[k]              remove entry — KeyError if missing (void, no return)
#   d.pop(k)              remove & return VALUE — optional default if missing
#   d.popitem()           remove & return (key, value) — LIFO (last inserted); no args
#
# Evict OLDEST on a plain dict — popitem(last=False) is OrderedDict only:
#   k = next(iter(d)); del d[k]   — or use OrderedDict (lesson_08/09_ordered_dict_lru.py)
#   next(iter(d))   — iter(d) yields keys; next() takes first — Java: iterator().next()
#   iter and next are BUILT-INS — not dict methods (no d.next()).

cache: dict[str, int] = {"oldest": 1, "middle": 2, "newest": 3}
del cache["middle"]
print(cache.pop("newest"))           # 3 — value returned
print(cache.pop("nope", None))      # None — default, key left absent

fresh = {"a": 1, "b": 2, "c": 3}
print(fresh.popitem())                  # ('c', 3) — LIFO (last inserted)

oldest_demo = {"x": 10, "y": 20}
oldest_key = next(iter(oldest_demo))    # peek first key — Java: iterator().next()
del oldest_demo[oldest_key]             # FIFO evict on plain dict
print(f"evicted {oldest_key!r} → {oldest_demo}")

# iter and next are BUILT-INS — not dict methods (no d.next()).

# Plain dict: d[k] read and d[k]=v update do NOT move k to the end.
# True LRU on get needs delete+reinsert or collections.OrderedDict.move_to_end — lesson_08/09_ordered_dict_lru.py


section("3. tuple — immutable ordered sequence (≈ Pair / Map.entry)")

# Tuple sizes at a glance:
#   ()       empty tuple (0 elements)
#   (42,)    1-tuple — trailing comma REQUIRED (see § one-element tuple below)
#   (1, 2)   2-tuple — comma between elements
#   (a,b,c)  n-tuple — one comma between each pair of values

# Tuple unpacking (destructuring) — assign each position to its own variable:
#
#   x, y = point              unpack a tuple (or any sequence of known length)
#   name, age, email = person   one name per slot — left count must match right count
#   low, high = min_max(nums)   unpack a function that returns multiple values
#
# Java (no built-in until you name fields):
#   int x = point[0]; int y = point[1];
#   var r = minMax(nums); int low = r.min(); int high = r.max();  // holder / Pair / record
#
# return a, b  — comma builds ONE tuple; caller unpacks with low, high = f()
# Also works on lists: a, b = [1, 2]   and in loops: for k, v in d.items()
#
# One slot only (e.g. second of three) — index is zero-based, same as Java arrays:
#   person[1]        second value — Java: person[1] on Object[] / array
#   _, age, _ = person   or unpack and ignore other slots with _

point = (3, 4)
person = ("Alice", 30, "alice@example.com")
#           0       1          2
print(point[0])                 # index 0 — first (≈ array[0])
print(person[1])                # index 1 — second value in a 3-tuple
x, y = point                    # unpack 2-tuple → two variables
name, age, email = person       # unpack 3-tuple → three variables
_, age_only, _ = person         # second slot only — ignore 1st and 3rd
print(x, y, name, age_only)

def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)  # comma = one tuple value, not two return statements

low, high = min_max([3, 1, 4, 1, 5])  # unpack return value — no temp Pair variable
print(low, high)

# zip — pair parallel sequences; list(zip(...)) → list of tuples; dict(zip(...)) → map
pairs = list(zip(["a", "b"], [1, 2]))  # [('a', 1), ('b', 2)]
print(pairs)

# zip(*matrix) — matrix TRANSPOSE (rows ↔ columns; not 90° rotation)
#
#   Before 2×3:              After 3×2:
#   [1, 2, 3]                [1, 4]
#   [4, 5, 6]                [2, 5]
#                            [3, 6]
#
#   *matrix unpacks each ROW as a separate zip argument:
#     zip(*[[1,2,3],[4,5,6]])  ==  zip([1,2,3], [4,5,6])
#   zip pairs by COLUMN index → (1,4), (2,5), (3,6)
#   list comprehension turns each column tuple into a list row
#
#   Java: for (c) for (r) out[c][r] = matrix[r][c]
#   Alt without *: [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(col) for col in zip(*matrix)]  # [[1, 4], [2, 5], [3, 6]]
print(transposed)

# --- One-element tuple (1-tuple) — trailing comma is required ---
#
# Parentheses do NOT make a tuple — the COMMA does:
#
#   Expression    type     len    notes
#   ----------    ----     ---    -----
#   (42)          int      —      grouping only (like (2+3)*4 in math)
#   (42,)         tuple    1      1-tuple — comma marks "this is a tuple"
#   ()            tuple    0      empty tuple
#   (1, 2)        tuple    2      comma BETWEEN values (no trailing comma needed)
#
# Unpack 1-tuple:  x, = (42,)   comma on LEFT too — otherwise x gets the whole tuple
# Return 1-tuple:   return 42,    comma after value — return 42 returns int, not tuple
#
# Java: no 1-tuple — Collections.singletonList(42) is a mutable List, not (42,)

not_a_tuple = (42)    # int — parentheses ignored
is_a_tuple = (42,)    # 1-tuple — trailing comma is the tuple marker
also_a_tuple = 42,    # same — comma outside parens also builds a 1-tuple
print(type(not_a_tuple), type(is_a_tuple), type(also_a_tuple))
print(len(is_a_tuple), is_a_tuple[0])

x, = (42,)            # unpack 1-tuple → x is int 42 (not the tuple)
whole = (42,)         # keep as tuple — no comma on left
print(x, whole, type(x), type(whole))

def single() -> tuple[int, ...]:
    return 42,         # (42,) — comma makes it a tuple return

print(single(), len(single()))

# --- Starred unpack (*) — variable-length unpacking ---
#
#   x, = (42,)           exactly 1 value → x=42  (comma on LEFT = one target)
#   x, = (42, 33, 5)     ValueError — too many values (expected 1), NOT the same!
#
#   * on the LEFT collects "the rest" into a LIST (can be empty):
#   first, *rest = (42, 33, 5)   → first=42, rest=[33, 5]
#   first, *_ = (42, 33, 5)      → first=42, ignore rest (_ = throwaway name)
#   *_, last = (42, 33, 5)       → last=5, ignore leading values
#   a, *mid, z = (1, 2, 3, 4)    → a=1, mid=[2, 3], z=4
#
#   * elsewhere (not unpack): zip(*matrix), {**d}, [*a, *b] — spread into call/literal

x, = (42,)                      # 1 target, 1 value — OK
first, *rest = (42, 33, 5)      # *rest soaks up middle+end as a list
first, *_ = (42, 33, 5)         # *_ = "rest goes here but we ignore it"
*_, last = (42, 33, 5)          # only want last element
a, *mid, z = (1, 2, 3, 4)
print(x, first, rest, last, a, mid, z)


section("4. set — HashSet")

tags = {"python", "java", "python"}
print(tags)
print("python" in tags)
print(set([1, 2, 2, 3, 3, 3]))

# Set algebra — Java: HashSet addAll / retainAll / removeAll / Sets.symmetricDifference
#
#   a = {1, 2, 3}     b = {3, 4, 5}     shared: 3
#
#   a | b   union              {1, 2, 3, 4, 5}  — either set (OR)
#   a & b   intersection       {3}             — both sets (AND)
#   a - b   difference           {1, 2}          — in a, not in b
#   a ^ b   symmetric diff       {1, 2, 4, 5}    — one but not both (XOR)
#
#   Identity: (a | b) - (a & b) == a ^ b
#             union minus overlap = symmetric difference
#
#   Sets only — NOT lists:  [1,2] + [2,3]  concat;  {1,2} | {2,3}  union

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b, a & b, a - b, a ^ b)
print((a | b) - (a & b) == a ^ b)   # True — union - intersection = symmetric diff
print([1, 2] + [2, 3])              # list: + keeps duplicates
print({1, 2} | {2, 3})              # set: | dedupes

left = {"alice": 10, "bob": 5}
right = {"bob": 3, "carol": 7}
print(left.keys() | right.keys())

def unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(unique_preserve_order(["b", "a", "b", "c", "a"]))
