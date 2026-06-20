"""Lesson 2c — collections module (all public container types).

Built-in list/dict/tuple/set are always available. The stdlib collections
package adds specialized containers — ships with Python (no pip install).

Public types in collections (this lesson):
  - defaultdict   — dict + auto-create missing keys
  - Counter       — dict subclass for counting (Multiset)
  - deque         — double-ended queue (ArrayDeque)
  - OrderedDict   — dict + move_to_end / popitem(last=False)
  - namedtuple    — lightweight immutable record (pre-dataclass)
  - ChainMap      — layered dict lookup (stack of maps)
  - UserDict      — dict wrapper for safer subclassing
  - UserList      — list wrapper for safer subclassing
  - UserString    — str wrapper for safer subclassing

See also (later lessons): collections.abc — Mapping, Sequence, Iterable ABCs.

Prerequisites: lesson_02/01_collections.py

Run:
    uv run python lesson_02/03_collections_stdlib.py
"""

from __future__ import annotations

from collections import (
    ChainMap,
    Counter,
    OrderedDict,
    UserDict,
    UserList,
    UserString,
    defaultdict,
    deque,
    namedtuple,
)


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Overview — stdlib collections vs built-in types")

# Java parallel:
#   list/dict/set     ≈ ArrayList, HashMap, HashSet  — language + JDK core
#   collections.*     ≈ java.util extras (Deque, LinkedHashMap patterns)
#                       + Guava-style Multiset / multimaps
#
# Import explicitly — not built into the language like dict:
#   from collections import deque, Counter, ...

print("import from collections — no pip install")
print(
    "types:",
    "defaultdict Counter deque OrderedDict namedtuple",
    "ChainMap UserDict UserList UserString",
)


section("1. defaultdict — dict + default factory (computeIfAbsent)")

# defaultdict(default_factory) calls default_factory() on __missing__(key).
# Subclasses dict — all normal dict methods work.
#
# Java:
#   map.computeIfAbsent(key, k -> new ArrayList<>()).add(item);
#   NOT the same as getOrDefault — defaultdict WRITES the default into the map.

# --- list values (grouping) ---
groups: defaultdict[str, list[str]] = defaultdict(list)
for word in ["eat", "tea", "tan", "ate"]:
    key = "".join(sorted(word))
    groups[key].append(word)
print(dict(groups))

# Compare manual setdefault (mutates only if missing — same outcome here):
manual: dict[str, list[str]] = {}
for word in ["eat", "tea"]:
    key = "".join(sorted(word))
    manual.setdefault(key, []).append(word)
print(manual)

# --- int factory (counting) ---
hits: defaultdict[str, int] = defaultdict(int)
for page in ("home", "home", "about"):
    hits[page] += 1                    # __missing__ created 0 first
print(dict(hits))

# --- set factory (unique buckets) ---
tags: defaultdict[str, set[str]] = defaultdict(set)
for user, tag in [("alice", "py"), ("alice", "java"), ("bob", "py")]:
    tags[user].add(tag)
print({k: sorted(v) for k, v in tags.items()})

# --- custom factory ---
def fresh_list() -> list[int]:
    return []

nums: defaultdict[str, list[int]] = defaultdict(fresh_list)
nums["a"].append(1)
print(nums["a"] is nums["a"])          # True — same list object per key

# Missing key WITHOUT triggering factory — use .get() like a normal dict:
print(nums.get("missing", []))         # [] — key not inserted
print("missing" in nums)               # False

# Convert to plain dict when done building:
plain = dict(groups)
print(type(plain))


section("2. Counter — frequency map (Multiset)")

# Counter is a dict subclass — keys are elements, values are int counts.
# Missing key → 0 (returns 0, does not insert).

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = Counter(words)
print(freq)
print(freq["apple"], freq["missing"])  # 3, 0

# Construct from mapping, iterable, or keyword args:
print(Counter({"a": 3, "b": 1}))
print(Counter(a=2, b=4))

# --- update counts ---
freq.update(["apple", "date"])
freq["cherry"] += 2
print(freq)

# --- query ---
print(freq.most_common(2))             # top-N [(elem, count), ...]
print(list(freq.elements()))           # 'apple','apple',... — repeats by count
print(sum(freq.values()), freq.total())  # total() — 3.10+

# --- multiset arithmetic ---
a, b = Counter("aab"), Counter("abb")
print(a + b)                           # union — add counts
print(a - b)                           # subtract — drop zero/negative
print(a & b)                           # intersection — min counts
print(a | b)                           # union — max counts

# Counter only keeps positive counts after - :
c = Counter(a=5, b=3) - Counter(a=2, b=4)
print(c)                               # Counter({'a': 3}) — b dropped

# Convert: dict(freq), list(freq) — keys only for list()


section("3. deque — double-ended queue (ArrayDeque)")

# deque — doubly-linked blocks — O(1) append/pop at BOTH ends.
# list.pop(0) is O(n) because elements shift.
#
# Java: ArrayDeque — addFirst/addLast, removeFirst/removeLast

dq: deque[int] = deque([10, 20, 30])
dq.append(40)                          # right — addLast
dq.appendleft(5)                         # left  — addFirst
print(dq)

print(dq.popleft())                    # 5
print(dq.pop())                        # 40
print(dq)

# Bulk ops
dq.extend([50, 60])                    # extend right
dq.extendleft([1, 2])                  # extend left — note: 2,1 end up first
print(dq)

# rotate — circular shift (positive = right, negative = left)
dq.rotate(1)
print(dq)
dq.rotate(-2)
print(dq)

# Index access O(n) — deques are not for random access like lists:
print(dq[0], dq[-1])

# maxlen — bounded deque evicts from opposite side (sliding window):
window: deque[int] = deque(maxlen=3)
for n in range(6):
    window.append(n)
print(window)                          # deque([3, 4, 5], maxlen=3)

# Thread-safe: append/pop are atomic in CPython — useful for queues.
# For heavy concurrency prefer queue.Queue (lesson later).


section("4. OrderedDict — ordered dict + access-order hooks")

# Since Python 3.7 plain dict keeps insertion order. OrderedDict still useful for:
#   move_to_end(key, last=True|False)
#   popitem(last=True|False)  — FIFO evict on last=False (plain dict popitem has no last=)
#   order-sensitive equality: od1 == od2 compares order (dict == does not)

od: OrderedDict[str, int] = OrderedDict()
od["c"] = 3
od["a"] = 1
od["b"] = 2
print(list(od.keys()))                 # insertion order

od.move_to_end("a")                    # promote to MRU tail
print(list(od.keys()))

od.move_to_end("b", last=False)        # push to LRU front
print(list(od.keys()))

k, v = od.popitem(last=False)          # FIFO evict
print(f"evicted {k}={v}, remaining {list(od.keys())}")

# Reassigning existing key does NOT move it (same as plain dict):
od2: OrderedDict[str, int] = OrderedDict(a=1, b=2)
od2["a"] = 99
print(list(od2.keys()))                # still a, b

# Order-aware equality:
x = OrderedDict([("a", 1), ("b", 2)])
y = OrderedDict([("b", 2), ("a", 1)])
print(x == y)                          # False — different key order

# LRU full walkthrough → lesson_08/09_ordered_dict_lru.py


section("5. namedtuple — immutable record (lightweight Pair / record)")

# namedtuple(typename, field_names) builds a tuple subclass with named attributes.
# Immutable — like a Java record without boilerplate (pre-@dataclass era).
#
# Java: record Point(int x, int y) { }  or  AbstractMap.SimpleEntry

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y, p[0])                  # attribute + index access
print(p)                               # Point(x=3, y=4)

# _replace — "with" for namedtuples (returns NEW tuple):
p2 = p._replace(x=10)
print(p, p2)

# _asdict() — OrderedDict of fields:
print(p._asdict())

# Unpack like any tuple:
x, y = p
print(x, y)

# Field names fixed at class creation — typo → AttributeError:
# p.z = 1  # AttributeError — immutable

# For mutable classes with methods → lesson_08 @dataclass. namedtuple = frozen data bag.


section("6. ChainMap — layered lookup (stack of dicts)")

# ChainMap(m1, m2, ...) searches maps left-to-right; first hit wins.
# Writes/deletes only touch the FIRST map.
#
# Java: no direct JDK equivalent — imagine stacked Maps or
#   Properties with defaults parent, or Spring Environment with property sources.

defaults = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark"}
env = {"debug": True}

settings = ChainMap(env, user_prefs, defaults)
print(settings["theme"])               # dark  — user_prefs
print(settings["lang"])                # en    — defaults
print(settings["debug"])               # True  — env (leftmost wins)

# Mutation hits leftmost map only:
settings["lang"] = "fr"
print(user_prefs)                      # {'theme': 'dark', 'lang': 'fr'}
print(defaults["lang"])                # still 'en'

# new_child() — push a fresh map on the left (scope chain):
child = settings.new_child({"theme": "solarized"})
print(child["theme"], child.maps[0])   # solarized — child layer only

# parents property — tuple of backing dicts (excluding top):
print(len(settings.maps))

# Flatten to one dict (rightmost loses on duplicate keys... actually last wins in merge):
print(dict(settings))


section("7. UserDict / UserList / UserString — safe subclassing")

# Subclassing built-in list/dict directly can break — methods are implemented in C
# and may bypass your overrides. User* wrappers delegate to .data (or .data for str).
#
# Java analogy: extend AbstractMap / AbstractList instead of implementing Map raw.

class LowerDict(UserDict):
    """Dict wrapper — keys stored lowercased."""

    def __setitem__(self, key: str, value: str) -> None:
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> str:
        return super().__getitem__(key.lower())


ld = LowerDict({"Name": "Alice"})
print(ld["name"], ld.data)

class AppendList(UserList):
    def append_twice(self, item: int) -> None:
        self.data.append(item)
        self.data.append(item)


al = AppendList([1])
al.append_twice(2)
print(al.data)

class Shout(UserString):
    def shout(self) -> str:
        return self.data.upper() + "!"


print(Shout("hi").shout())

# For most code: use plain dict/list or @dataclass. User* when you need
# inheritance hooks without fighting C builtins.


section("8. Cheat sheet — when to reach for which")

print("""
| Type          | Use when                          | Java-ish parallel        |
|---------------|-----------------------------------|--------------------------|
| defaultdict   | auto-create missing keys          | computeIfAbsent          |
| Counter       | count frequencies                 | Multiset / groupingBy    |
| deque         | fast both-end queue/window        | ArrayDeque               |
| OrderedDict   | move_to_end, FIFO popitem         | LinkedHashMap access     |
| namedtuple    | small immutable record            | record / Pair            |
| ChainMap      | layered config / scoped defaults  | stacked property sources |
| UserDict/List | subclass dict/list safely         | AbstractMap / AbstractList |

collections.abc (Mapping, Sequence, …) — type-checking & protocols; later lessons.
LRU cache (dict vs OrderedDict) → lesson_08/09_ordered_dict_lru.py
""")
