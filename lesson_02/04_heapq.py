"""Lesson 2d — heapq (min-heap priority queue).

Python has no separate Heap class — the heapq module operates on a list IN-PLACE.
Always a MIN-heap: index 0 is the smallest element.

Java: PriorityQueue (natural order / min-heap by default).
  poll()  ≈ heapq.heappop
  offer() ≈ heapq.heappush
  O(log n) push/pop; heapify is O(n)

NOT in collections — import heapq (stdlib, no pip).

Prerequisites: lesson_02/01_collections.py

Run:
    uv run python lesson_02/04_heapq.py
"""

from __future__ import annotations

import heapq


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Mental model — binary min-heap in a list")

# heapq stores a complete binary tree in an array (like ArrayDeque backing array):
#
#   index:  0   1   2   3   4   5
#   heap:  [1,  3,  2,  7,  5,  4]
#
#   parent(i)     = (i - 1) // 2
#   left child    = 2*i + 1
#   right child   = 2*i + 2
#
# Invariant: parent <= both children  →  h[0] is always MINIMUM.

nums = [5, 1, 9, 2, 7]
heapq.heapify(nums)                   # in-place — O(n); nums is now a heap
print(nums)                           # [1, 2, 9, 5, 7] — NOT fully sorted!

print(nums[0])                        # 1 — peek min (Java PriorityQueue.peek)
print(heapq.heappop(nums))            # 1 — pop min — O(log n)
print(nums)                           # heap restored after pop


section("2. Push / pop — mutable priority queue")

h: list[int] = []
heapq.heappush(h, 30)
heapq.heappush(h, 10)
heapq.heappush(h, 20)
print(h)                              # heap order, not sorted list
print(heapq.heappop(h))               # 10
print(heapq.heappop(h))               # 20


section("3. Top-k without sorting the whole list")

data = [5, 1, 9, 2, 7, 1, 3]
print(heapq.nsmallest(3, data))       # [1, 1, 2] — k smallest
print(heapq.nlargest(2, data))       # [9, 7] — k largest

# With key= (like Comparator) — tie-break alphabetically:
words = ["cc", "bb", "aa", "bb", "aa"]
freq = {"aa": 2, "bb": 2, "cc": 1}
print(
    heapq.nsmallest(
        2, words, key=lambda w: (freq[w], w)
    )
)                                     # ['cc', 'aa'] — lowest freq, then alpha


section("4. Max-heap trick — negate values")

# heapq is MIN-only. For MAX-heap priorities, store negative numbers:
scores = [45, 90, 72, 88]
max_heap = [-s for s in scores]
heapq.heapify(max_heap)
best = -heapq.heappop(max_heap)
print(best)                           # 90

# Or use nlargest(1, scores)[0] for a one-off peek at max.


section("5. Tuple ordering — priority + payload")

# heap compares elements with < . Tuples compare left-to-right:
#   (priority, tie_breaker, item)  — lower priority int wins first.
#
# Java: PriorityQueue with Comparator.comparing(Task::getPriority)
#       .thenComparing(Task::getName)

tasks: list[tuple[int, str]] = []
heapq.heappush(tasks, (3, "low"))
heapq.heappush(tasks, (1, "urgent"))
heapq.heappush(tasks, (2, "medium"))
print(heapq.heappop(tasks))           # (1, 'urgent')
print(heapq.heappop(tasks))           # (2, 'medium')


section("6. heapq.merge — lazy k-way merge (sorted streams)")

# Merge already-sorted iterables without materializing one giant list first.
a = [1, 4, 7]
b = [2, 3, 8]
print(list(heapq.merge(a, b)))         # [1, 2, 3, 4, 7, 8]

# Java: merge step in merge-sort, or PriorityQueue over iterator heads.


section("7. When to use heap vs sorted vs deque")

print("""
| Need                         | Use                          |
|------------------------------|------------------------------|
| k smallest / largest         | heapq.nsmallest / nlargest   |
| repeated pop-min / push      | heapq heapify + heappush/pop |
| fully sorted output          | sorted() or list.sort()      |
| both-end queue, not priority | collections.deque            |
| Java PriorityQueue           | list + heapq                   |
""")

print("Practice → lesson_02/practice/04_heapq.py")
print("collections tour → lesson_02/03_collections_stdlib.py")
