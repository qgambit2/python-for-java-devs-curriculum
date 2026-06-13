"""Lesson 2i — collections & sorting with custom types (Java Collections bridge).

Lesson 1 taught list/dict/set syntax and sorted(key=...) on dicts.
This lesson ties **custom classes** to collections — where equals/hash vs ordering matter.

Topics:
  - Two separate contracts: equality (__eq__/__hash__) vs ordering (__lt__/key=)
  - Which collection uses which hook (list vs set vs dict keys/values)
  - sorted() / list.sort() with key=  ≈ Comparator
  - @dataclass(order=True) / __lt__  ≈ Comparable
  - No stdlib TreeSet — sorted(list) or key= each time

Prerequisites: lesson_08/07_eq_and_hash.py, lesson_05/01_builtins.py

Run:
    uv run python lesson_08/08_collections_and_sorting.py
"""

from dataclasses import dataclass
from functools import total_ordering


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Two contracts — don't mix them up")

# Java Collections uses TWO different mechanisms on objects:
#
#   HashSet / HashMap key     →  equals() + hashCode()     (equality contract)
#   TreeSet / Collections.sort with Comparable  →  compareTo()  (ordering)
#   Collections.sort with Comparator            →  external key (like key=)
#
# Python mirrors this:
#
#   set / dict KEY            →  __eq__ + __hash__
#   sorted(xs) on objects     →  __lt__ (or other rich comparisons) OR key=
#
# Sorting does NOT use __eq__/__hash__.  Hash collections do NOT use __lt__.

print("Equality  → set, dict keys, list 'in' (via ==)")
print("Ordering  → sorted(), min(), max(), list.sort() (via < or key=)")


section("2. Custom types in each collection")

class Point:
    """Hashable value object — lesson 07 pattern."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# list — membership scans with == (__eq__); no __hash__
print(f"p2 in [p1]: {p2 in [p1]}")          # True — O(n) scan
print(f"[p1] == [p2]: {[p1] == [p2]}")      # True — element-wise ==

# set — __hash__ (bucket) then __eq__ (verify)
print(f"set dedupe: { {p1, p2, p3} }")      # two elements

# dict — keys need hash+eq; values can be anything (lists, mutable objects)
ledger: dict[Point, str] = {p1: "a", p3: "b"}
print(f"dict lookup: {ledger[p2]}")         # p2 equals p1 as key


section("2b. dict insertion order — like LinkedHashMap (not plain HashMap)")

# Python 3.7+: every dict remembers INSERTION ORDER when you iterate keys/values/items.
# Lookup is still hash-based (HashMap speed); iteration order is LinkedHashMap-like.
# Re-assigning an existing key updates the value but does NOT move the key's position.
#
# Equality ignores key order: {"b": 2, "a": 1} == {"a": 1, "b": 2}  → True
# Iteration/print use insertion order — not sorted order.

order: dict[str, int] = {}
order["c"] = 3
order["a"] = 1
order["b"] = 2
print(f"keys after insert c,a,b: {list(order.keys())}")  # ['c', 'a', 'b']

order["a"] = 99   # update value — key stays in same slot
print(f"keys after order['a']=99: {list(order.keys())}")  # still ['c', 'a', 'b']

# sorted(d) sorts keys alphabetically — does NOT change the dict's internal order
print(f"sorted(order): {sorted(order)}")   # ['a', 'b', 'c'] — new list, dict unchanged
print(f"dict still: {list(order.keys())}")  # ['c', 'a', 'b']

# Lesson 2 full demo: lesson_02/01_collections.py


section("3. sorted() on objects — TypeError without ordering or key=")

points = [Point(3, 1), Point(1, 2), Point(2, 0)]

try:
    sorted(points)
except TypeError as e:
    print(f"sorted(points) fails: {e}")
    # Point defines == but not < — no natural order (unlike int/str/tuple)

# Fix A: key=  ≈  Comparator.comparing(p -> p.getX()).thenComparing(p -> p.getY())
by_xy = sorted(points, key=lambda p: (p.x, p.y))
print(f"sorted(key=lambda): {by_xy}")

# Fix B: define ordering on the class (next sections) — then sorted(points) works


section("4. key= — external Comparator (Lesson 1 recap, now with objects)")

people = [
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Carol", "age": 25},
]

# Dict rows — bracket access (Lesson 1 practice style)
print(sorted(people, key=lambda p: (p["age"], p["name"])))

@dataclass
class Person:
    name: str
    age: int

team = [Person("Bob", 30), Person("Alice", 25), Person("Carol", 25)]
# Object rows — dot access
print(sorted(team, key=lambda p: (p.age, p.name)))

# key= does NOT require __lt__ on Person — compares the lambda's return values
# Java: Collections.sort(list, Comparator.comparing(...))


section("5. @dataclass(order=True) — auto Comparable")

@dataclass(order=True)
class RankedTask:
    priority: int      # compared first (field declaration order)
    name: str = ""

tasks = [RankedTask(2, "email"), RankedTask(1, "deploy"), RankedTask(1, "backup")]
print(f"sorted(tasks): {sorted(tasks)}")           # uses generated __lt__
print(f"min(tasks): {min(tasks)}")                 # RankedTask(priority=1, name='backup')

# order=True generates __lt__, __le__, __gt__, __ge__ from fields — NOT __eq__/__hash__
# (eq=True is still default — separate concern; see lesson 07 for hash)


section("6. Manual __lt__ + @total_ordering")

@total_ordering
class Version:
    """Compare major.minor — only __eq__ and __lt__ required; decorator fills the rest."""

    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other: "Version") -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self) -> str:
        return f"Version({self.major}.{self.minor})"


versions = [Version(2, 1), Version(1, 9), Version(2, 0)]
print(f"sorted(versions): {sorted(versions)}")
print(f"Version(1, 9) < Version(2, 0): {Version(1, 9) < Version(2, 0)}")

# Java: class Version implements Comparable<Version> { public int compareTo(...) }


section("7. min / max — same ordering rules as sorted")

print(f"max(points, key=lambda p: p.x): {max(points, key=lambda p: p.x)}")
print(f"max(versions): {max(versions)}")  # uses __lt__


section("8. Java TreeSet? — no stdlib sorted set")

# Java TreeSet keeps elements sorted by compareTo/Comparator at insert time.
# Python set is always hash-based (like HashSet). No built-in TreeSet.
#
# Options:
#   sorted(list, key=...)     — sort when you need a view (most common)
#   bisect on a sorted list   — binary search insert (stdlib bisect module)
#   sortedcontainers.SortedSet — third party
#
# For custom objects: either keep a list sorted with key= / __lt__,
# or sort on demand — don't expect set to maintain order.

nums_set = {3, 1, 2}
print(f"set iteration order (hash-based, not sorted): {nums_set}")
print(f"sorted(nums_set): {sorted(nums_set)}")


section("9. Cheat sheet — Java Collections ↔ Python hooks")

print("""
| Java                         | Python                         | Hooks used        |
|------------------------------|--------------------------------|-------------------|
| HashSet.contains             | x in set                       | __hash__ + __eq__ |
| HashMap.get(key)             | d[key] / key in d              | __hash__ + __eq__ |
| LinkedHashMap iteration      | for k in d / list(d.keys())    | insertion order (3.7+); reassign key ≠ move |
| ArrayList.contains           | x in list                      | __eq__ only (O(n))|
| HashMap value (any type)     | d[key] = mutable_obj           | none on value     |
| TreeSet / Comparable sort    | sorted(xs) with __lt__         | __lt__ (ordering) |
| Comparator.sort              | sorted(xs, key=lambda ...)     | key return values |
| equals + hashCode contract   | __eq__ + __hash__              | set / dict keys   |
| compareTo contract           | __lt__ (+ order=True)          | sort / min / max  |
""")

print("Lesson 2: collections → lesson_02/01_collections.py")
print("Equality deep dive → lesson_08/07_eq_and_hash.py")
