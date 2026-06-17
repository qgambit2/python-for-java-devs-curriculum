"""Lesson 1h — built-in functions (always available, no import)."""

# ---------------------------------------------------------------------------
# range() — like a lazy number sequence for loops
# ---------------------------------------------------------------------------
# Java:  for (int i = 0; i < 5; i++)
# Python: for i in range(5):

print("range(5):", list(range(5)))           # [0, 1, 2, 3, 4]
print("range(2, 5):", list(range(2, 5)))     # [2, 3, 4]  — start inclusive, stop exclusive
print("range(0, 10, 2):", list(range(0, 10, 2)))  # [0, 2, 4, 6, 8] — step

# range() does NOT build a list in memory until you ask (via list() or a loop)
# Good for large ranges: range(1_000_000) is cheap

# ---------------------------------------------------------------------------
# len, min, max, sum — work on lists and other collections
# ---------------------------------------------------------------------------
nums = [3, 1, 4, 1, 5]
print(len(nums))    # 5   — like .length / .size()
print(min(nums))    # 1
print(max(nums))    # 5
print(sum(nums))    # 14

# ---------------------------------------------------------------------------
# sorted — ALWAYS returns a new list (any iterable in, list out)
# ---------------------------------------------------------------------------
print(sorted(nums))              # [1, 1, 3, 4, 5]
print(nums)                      # [3, 1, 4, 1, 5]  still original

# Works on any iterable — return type is always list, not the input type
print(sorted((3, 1, 2)))         # [1, 2, 3]  tuple in → list out
print(sorted({3, 1, 2}))         # [1, 2, 3]  set in → list out
print(sorted("cba"))             # ['a', 'b', 'c']  string in → list of chars
# Java: Arrays.sort(word.toCharArray()); new String(arr)  OR  String.join("", sortedChars)
print("".join(sorted("cba")))    # 'abc'

# Dict: sorted(d) sorts KEYS (not values); original dict unchanged
scores = {"bob": 87, "alice": 95, "carol": 72}
print(sorted(scores))            # ['alice', 'bob', 'carol']
print(sorted(scores.keys()))     # same — .keys() is a dict_keys view, sorted() still returns list
print(sorted(scores.items()))    # [('alice', 95), ('bob', 87), ('carol', 72)] — (key, value) pairs

# Sort keys by value — key= lambda (like Comparator.comparing)
print(sorted(scores, key=lambda name: scores[name]))           # names by score asc
print(sorted(scores, key=lambda name: scores[name], reverse=True))  # top scorer first

# list.sort() is different: mutates list in place, returns None — only lists have .sort()
copy = [3, 1, 2]
result = copy.sort()             # result is None! copy is now [1, 2, 3]
print(result, copy)

print(list(reversed(nums)))      # [5, 1, 4, 1, 3]

# ---------------------------------------------------------------------------
# heapq — top-k smallest/largest (min-heap; like PriorityQueue)
# ---------------------------------------------------------------------------
import heapq

nums = [5, 1, 9, 2, 7, 1]
print(heapq.nsmallest(3, nums))   # [1, 1, 2]
print(heapq.nlargest(2, nums))    # [9, 7]

word_counts = {"aa": 1, "bb": 2, "cc": 2}
print(heapq.nsmallest(2, word_counts.keys(), key=lambda w: (word_counts[w], w)))
# ['aa', 'bb'] — same key idea as sorted(...)[:k] in rare_words practice

h = [5, 1, 9]
heapq.heapify(h)
heapq.heappush(h, 0)
print(heapq.heappop(h))           # 0 — smallest (poll on min-heap)

# ---------------------------------------------------------------------------
# any, all — like stream().anyMatch() / allMatch()
# ---------------------------------------------------------------------------
scores = [40, 55, 90]
print(any(s >= 60 for s in scores))   # True  — at least one passes
print(all(s >= 60 for s in scores))   # False — not all pass

# ---------------------------------------------------------------------------
# enumerate — loop with index (cleaner than range(len(...)))
# ---------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# ---------------------------------------------------------------------------
# zip — pair elements from parallel iterables (returns tuples)
# ---------------------------------------------------------------------------
names = ["alice", "bob"]
values = [95, 87]
for name, score in zip(names, values):
    print(f"  {name} -> {score}")

print(list(zip([1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9])))
# [(1, 3, 5, 7), (2, 4, 6, 8), (3, 5, 7, 9)] — one tuple per index

# * unpacks a list into separate zip arguments — Java: method(row0, row1, ...) varargs
matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))        # same as zip([1,2,3], [4,5,6]) → columns as tuples
# Java transpose (no zip): for (int c = 0; c < cols; c++) out[c][r] = matrix[r][c]
print([list(col) for col in zip(*matrix)])  # transpose → [[1, 4], [2, 5], [3, 6]]
# * works with any number of rows — not just 2

# Without * use index loop (most like Java nested for-loops)
# strict=False (3.10+): ragged rows OK — zip stops at shortest (Java: check row lengths yourself)
print(list(zip(*[[1, 2], [3, 4, 5]], strict=False)))  # [(1, 3), (2, 4)]

# ---------------------------------------------------------------------------
# type, isinstance — check types (isinstance is preferred)
# ---------------------------------------------------------------------------
x = 42
print(type(x))                  # <class 'int'>
print(isinstance(x, int))       # True

# ---------------------------------------------------------------------------
# int, str, float, bool — casting (like Integer.parseInt, String.valueOf)
# ---------------------------------------------------------------------------
print(int("42"))                # 42
print(str(42))                  # "42"
print(float("3.14"))            # 3.14
print(bool(0), bool(1), bool(""))  # False True False
