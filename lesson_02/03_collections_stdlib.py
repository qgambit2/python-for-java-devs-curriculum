"""Lesson 2c — collections module (stdlib extras beyond list/dict/set).

Java: java.util has ArrayDeque, LinkedHashMap; Guava adds Multiset, Multimap patterns.
Python keeps the common ones in collections — no pip install.

Topics:
  - defaultdict — computeIfAbsent without the boilerplate
  - Counter — frequency map / Multiset
  - deque — double-ended queue (O(1) both ends; beats list.pop(0))
  - OrderedDict — move_to_end / popitem(last=False) (LRU → lesson_08/09_ordered_dict_lru.py)

Prerequisites: lesson_02/01_collections.py

Run:
    uv run python lesson_02/03_collections_stdlib.py
"""

from __future__ import annotations

from collections import Counter, OrderedDict, defaultdict, deque


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. defaultdict — computeIfAbsent in one line")

# Java:
#   map.computeIfAbsent(key, k -> new ArrayList<>()).add(item);
#
# defaultdict(factory) calls factory() when a missing key is first accessed.

groups: defaultdict[str, list[str]] = defaultdict(list)
for word in ["eat", "tea", "tan"]:
    key = "".join(sorted(word))
    groups[key].append(word)          # no if key not in groups / setdefault dance
print(dict(groups))

# int factory — missing keys start at 0 (handy for counting)
hits: defaultdict[str, int] = defaultdict(int)
for page in ("home", "home", "about"):
    hits[page] += 1                   # hits[page] is 0 first time
print(dict(hits))


section("2. Counter — frequency map (≈ Guava Multiset / Stream.collect grouping)")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = Counter(words)
print(freq)                           # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(freq["apple"])                  # 3 — missing key → 0 (not KeyError)
print(freq.most_common(2))            # [('apple', 3), ('banana', 2)]

# Counter supports + and - on counts (union / subtract multisets)
print(Counter("aab") + Counter("abb"))


section("3. deque — ArrayDeque (O(1) both ends)")

# list.pop(0) is O(n) — whole array shifts. deque is O(1) at front and back.
dq: deque[int] = deque([10, 20, 30])
dq.append(40)                         # add right — append
dq.appendleft(5)                      # add left — addFirst
print(dq.popleft())                   # 5 — removeFirst
print(dq.pop())                       # 40 — removeLast
print(dq)

# Bounded deque — auto-evicts from opposite end (simple sliding window)
window: deque[int] = deque(maxlen=3)
for n in range(5):
    window.append(n)
print(window)                         # deque([2, 3, 4], maxlen=3)


section("4. OrderedDict — access-order hooks (preview)")

# Plain dict: insertion order only — get does not promote key (see 01_collections.py §2b).
# OrderedDict adds move_to_end and popitem(last=False).

od: OrderedDict[str, int] = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")                   # promote to MRU tail — LinkedHashMap(accessOrder=true)
print(list(od.keys()))                # ['b', 'c', 'a']
k, v = od.popitem(last=False)         # evict LRU front — plain dict has no last=False
print(f"evicted {k}={v}")

print("\nLRU with plain dict (pop+reinsert) OR OrderedDict → lesson_08/09_ordered_dict_lru.py")
