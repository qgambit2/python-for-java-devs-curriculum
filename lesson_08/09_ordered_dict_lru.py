"""Lesson 8j — OrderedDict & LRU pattern (LinkedHashMap access-order).

Lesson 2 covered dict insertion order and removal (del, pop, popitem, next(iter)).
This lesson shows when a plain dict is not enough — access-order LRU caches.

Topics:
  - Plain dict: insert order only; get does not promote to MRU
  - OrderedDict.move_to_end — like LinkedHashMap access-order
  - LRUCache with OrderedDict and with plain dict (pop + reinsert)

Prerequisites: lesson_02/01_collections.py §2b, lesson_08/01_class_basics.py

Run:
    uv run python lesson_08/09_ordered_dict_lru.py
"""

from __future__ import annotations

from collections import OrderedDict


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Plain dict — insertion order, not access order")

cache: dict[str, int] = {}
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3
_ = cache["a"]              # read — key "a" stays at front, not promoted to end
print(list(cache.keys()))   # ['a', 'b', 'c']

# Evict oldest by insertion: next(iter(cache)) or popitem(last=False)
oldest = next(iter(cache))
del cache[oldest]
print(f"evicted {oldest!r} → keys {list(cache.keys())}")


section("2. OrderedDict — move_to_end on access")

# Java: LinkedHashMap(accessOrder=true) — get/put moves entry to tail (MRU)
od: OrderedDict[str, int] = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od.move_to_end("a")         # promote "a" to most-recently-used (end)
print(list(od.keys()))      # ['b', 'c', 'a']

od.move_to_end("c", last=False)  # push "c" to front (LRU side)
print(list(od.keys()))      # ['c', 'b', 'a']

# Evict LRU (front): popitem(last=False)
k, v = od.popitem(last=False)
print(f"evicted {k}={v} → {list(od.keys())}")


section("3. LRUCache — OrderedDict (readable intent)")

class LRUCache:
    """Capacity-bounded cache — OrderedDict for O(1) get/put + eviction."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._store: OrderedDict[str, int] = OrderedDict()

    def get(self, key: str) -> int:
        if key not in self._store:
            return -1
        self._store.move_to_end(key)
        return self._store[key]

    def put(self, key: str, value: int) -> None:
        if key in self._store:
            self._store.move_to_end(key)
        self._store[key] = value
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)

    def __repr__(self) -> str:
        return f"LRUCache({dict(self._store)}, cap={self.capacity})"


lru = LRUCache(2)
lru.put("a", 1)
lru.put("b", 2)
print(lru.get("a"))         # 1 — promotes "a"
lru.put("c", 3)             # evicts "b" (LRU)
print(lru)                  # a=1, c=3


section("4. LRUCache — plain dict (pop + reinsert, equally common)")

# Same O(1) average behavior — no collections import. On get/put:
#   pop(key) then store[key] = val  →  key lands at the end (MRU).
# Evict LRU: pop(next(iter(store)))  →  removes oldest key.


class LRUCacheDict:
    """LRU with a regular dict — LeetCode-style alternative to OrderedDict."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._store: dict[str, int] = {}

    def get(self, key: str) -> int:
        if key not in self._store:
            return -1
        val = self._store.pop(key)
        self._store[key] = val          # reinsert at tail → MRU
        return val

    def put(self, key: str, value: int) -> None:
        if key in self._store:
            self._store.pop(key)
        self._store[key] = value
        if len(self._store) > self.capacity:
            self._store.pop(next(iter(self._store)))  # evict LRU (front)

    def __repr__(self) -> str:
        return f"LRUCacheDict({self._store}, cap={self.capacity})"


lru2 = LRUCacheDict(2)
lru2.put("a", 1)
lru2.put("b", 2)
print(lru2.get("a"))
lru2.put("c", 3)
print(lru2)                 # same outcome as OrderedDict version


print("\ncollections module overview → lesson_02/03_collections_stdlib.py")
print("Removal recap → lesson_02/01_collections.py §2b")
print("Equality/hash in dict keys → lesson_08/07_eq_and_hash.py")
