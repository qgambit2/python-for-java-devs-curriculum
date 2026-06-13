"""Lesson 2g — __eq__ / __hash__ (≈ Java equals() / hashCode()).

Topics:
  - == vs is
  - __eq__ + __hash__ contract: a == b ⇒ hash(a) == hash(b) (same as Java equals/hashCode)
  - When each is called: == → __eq__ only; hash() → __hash__ only;
    set/dict → BOTH (__hash__ bucket, then __eq__ verify)  §3a-bis
  - hash((x, y)) tuple combinator  §3a
  - NotImplemented / reverse __eq__  §3b
  - unhashable when __eq__ without __hash__

Run:
    uv run python lesson_08/07_eq_and_hash.py

Practice:
    uv run python lesson_08_eq_hash_practice.py
"""

from dataclasses import dataclass


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. == vs is  (value equality vs identity)")

a = [1, 2]
b = [1, 2]
c = a
print(f"a == b: {a == b}")   # True  — same contents
print(f"a is b: {a is b}")   # False — different list objects
print(f"a is c: {a is c}")   # True  — same object (Java == on references)

x = None
print(f"x is None: {x is None}")  # idiomatic — never x == None


section("2. Default object — identity ==, id-based hash")

class DefaultBox:
    pass


box1 = DefaultBox()
box2 = DefaultBox()
print(f"box1 == box2: {box1 == box2}")  # False — object.__eq__ is identity
print(f"hash equal: {hash(box1) == hash(box2)}")  # usually False


section("3. Value object — __eq__ + __hash__ (Java equals/hashCode contract)")

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:  # -> bool is a HINT — not enforced at runtime
        if not isinstance(other, Point):
            # NotImplemented is a singleton object, not a bool — tells == to try other.__eq__(self)
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))  # hash every field used in __eq__

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


# Contract (same as Java equals/hashCode): if a == b then hash(a) == hash(b)
# NOT the reverse — unequal objects MAY share a hash (collision); __eq__ resolves it.
p1 = Point(1, 2)
p2 = Point(1, 2)
print(f"p1 == p2: {p1 == p2}")
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")  # contract satisfied
print(f"set: { {p1, p2} }")  # one element — set used BOTH __hash__ and __eq__ (see §3a-bis)


section("3a-bis. When Python uses __eq__ alone vs __hash__ alone vs BOTH")

# ==  print  f"{a == b}"  →  __eq__ only (never __hash__)
print(f"p1 == p2 uses __eq__ only: {p1 == p2}")

# hash()  →  __hash__ only
print(f"hash(p1) uses __hash__ only: {hash(p1)}")

# set / dict  →  __hash__ first (find bucket), then __eq__ (confirm match — collisions exist)
# Java HashSet: hashCode() → bucket, equals() → verify
s = {p1}
print(f"p2 in s: {p2 in s}")   # True — hash(p2)==hash(p1), then __eq__(p2, p1)

# list  →  __eq__ only (linear scan, no hashing)
print(f"p2 in [p1]: {p2 in [p1]}")  # True — scans with ==


section("3a. hash((self.x, self.y)) — how tuple hashing works")

# hash(obj) → int (like hashCode()). For a tuple, Python:
#   1. hash each element (must be hashable — int/str/float/tuple, not list/dict)
#   2. mix those ints with a built-in combinator (order and length matter)
#   3. return one int — big negative numbers are normal

print(f"hash(1): {hash(1)}")                    # 1 — small ints often hash to themselves
print(f"hash(2): {hash(2)}")                    # 2
print(f"hash((1, 2)): {hash((1, 2))}")          # mixed int — NOT hash(1)+hash(2)
print(f"hash((2, 1)): {hash((2, 1))}")          # different order → different hash
print(f"equal tuples: {hash((1, 2)) == hash((1, 2))}")  # True

# Elements need not be int — any hashable type:
print(f"hash(('A', 'spades')): {hash(('A', 'spades'))}")

# Nested tuples OK:
print(f"hash((1, (2, 3))): {hash((1, (2, 3)))}")

# Mutable / unhashable inside tuple → TypeError:
try:
    hash(([1, 2], 3))
except TypeError as e:
    print(f"list in tuple: {e}")

# Java parallel: Objects.hash(x, y) — mixes hashCode of each field
# Python idiom: hash((x, y)) — hash every field used in __eq__, fixed order


section("3b. NotImplemented → reverse __eq__ (no Java equivalent)")

# a == b protocol (compare to idiomatic Java equals — identity is developer-written, not Java magic):
#
#   Java equals() (what devs often write)     Python a == b (language protocol)
#   ------------------------------------      -------------------------
#   1. if (this == o) return true  (habit)    step 3: (a is b) if __eq__ failed both ways
#   2. if (!(o instanceof T)) false            your __eq__: False or NotImplemented
#   3. compare fields                         your __eq__: field comparison
#
#
#   1. a.__eq__(b)
#   2. if NotImplemented → b.__eq__(a)   ← reverse equals
#   3. if still NotImplemented → (a is b)  ← like Java's first line, but automatic

# Contrived on purpose: Point and PointAsTuple are not a design you'd ship —
# they exist to show the == protocol (forward __eq__, NotImplemented, reverse __eq__).
class PointAsTuple:
    """Knows how to compare itself to Point — Point alone does not know this type."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented


pt = Point(1, 2)
wrapper = PointAsTuple(1, 2)
print(f"Point == PointAsTuple: {pt == wrapper}")  # True — reverse __eq__ on PointAsTuple
print(f"Point == tuple: {pt == (1, 2)}")        # False — both sides NotImplemented → not is


section("4. __eq__ without __hash__ → unhashable (Python default)")

# To use set/dict keys you MUST define __hash__ matching __eq__ (same as Java).
# If you only define __eq__: Python sets __hash__ = None (unhashable, TypeError).
# Java instead keeps Object.hashCode() — HashSet accepts it but contract is broken.

class MutablePoint:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MutablePoint):
            return NotImplemented
        return self.x == other.x and self.y == other.y


mp = MutablePoint(1, 2)
print(f"mp == MutablePoint(1, 2): {mp == MutablePoint(1, 2)}")
try:
    {mp}
except TypeError as e:
    print(f"set fails: {e}")


section("5. Dict keys — hashable; values — anything")

ledger: dict[Point, str] = {Point(0, 0): "origin", Point(1, 2): "corner"}
print(f"lookup Point(1, 2): {ledger[Point(1, 2)]}")  # key needs __hash__ + __eq__

# Values are NOT hashed — lists, mutable objects, unhashable types are fine:
by_name: dict[str, MutablePoint] = {"home": MutablePoint(0, 0)}
by_name["home"].x = 99   # mutate value — OK
print(f"dict value mutated: {by_name['home'].x}")

try:
    {MutablePoint(0, 0): "bad"}  # type: ignore[misc]
except TypeError as e:
    print(f"unhashable KEY fails: {e}")  # same rule as set — keys only, not values


section("6. NotImplemented — comparing to other types")

print(f"Point(1,2) == (1,2): {Point(1, 2) == (1, 2)}")  # False — not a Point
print(f"(1,2) == Point(1,2): {(1, 2) == Point(1, 2)}")  # False — tuple doesn't know Point


section("7. Broken contract — value __eq__ + id __hash__ (DON'T do this)")

class BrokenEq:
    """Explicitly keeps object.__hash__ (id) while comparing by value — violates contract."""

    __hash__ = object.__hash__  # rare foot-gun; default __eq__-only classes are just unhashable

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BrokenEq):
            return NotImplemented
        return self.value == other.value


b1 = BrokenEq(42)
b2 = BrokenEq(42)
print(f"b1 == b2: {b1 == b2}")
print(f"hash equal: {hash(b1) == hash(b2)}")  # False — id-based hash
print(f"set length: {len({b1, b2})}")  # 2 — duplicates in set despite ==
print("Violated contract → set bug. Safe fixes: __eq__ only → unhashable; or __eq__ + __hash__ on same fields")


section("8. Tuples — built-in immutable value objects (always hashable if contents are)")

t1 = (1, 2)
t2 = (1, 2)
print(f"t1 == t2: {t1 == t2}")
print(f"{{t1, t2}}: { {t1, t2} }")

bad = ([1, 2], 3)  # list inside tuple
try:
    hash(bad)
except TypeError as e:
    print(f"tuple with list inside unhashable: {e}")


section("9. @dataclass — auto __eq__; __hash__ only when frozen")

@dataclass
class Person:
    name: str
    age: int


@dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int


@dataclass(eq=False)
class NoCompare:
    value: int


print(f"Person equal: {Person('A', 1) == Person('A', 1)}")
print(f"frozen set: { {FrozenPoint(1, 2), FrozenPoint(1, 2)} }")
print(f"NoCompare uses identity: {NoCompare(1) == NoCompare(1)}")

try:
    {Person("A", 1)}
except TypeError as e:
    print(f"mutable Person unhashable: {e}")


section("10. Practical pattern — dedupe with set (needs __hash__)")

points = [Point(1, 2), Point(3, 4), Point(1, 2), Point(0, 0)]
unique = set(points)
print(f"{len(points)} points → {len(unique)} unique: {sorted(unique, key=lambda p: (p.x, p.y))}")
# Sorting vs equality → lesson_08/08_collections_and_sorting.py
