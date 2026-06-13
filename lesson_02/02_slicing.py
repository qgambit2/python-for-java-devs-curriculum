"""Lesson 1i — list slicing (subList in Java)."""

nums = [10, 20, 30, 40, 50]

# Basic slices — stop is EXCLUSIVE (like range)
print(nums[:3])     # [10, 20, 30]   first 3
print(nums[2:])     # [30, 40, 50]   from index 2 to end
print(nums[1:4])    # [20, 30, 40]   index 1 up to (not including) 4
print(nums[:])      # [10, 20, 30, 40, 50]  shallow copy — Java: new ArrayList<>(nums)
# Other list shallow copies: nums.copy()  list(nums)  — same idea as nums[:]
# Dict has NO [:] — use {**d} or d.copy() instead (see 04_collections.py)

# Negative indexes — count from the end (-1 = last, -5 = first when len=5)
# Rule: index k  ==  len(items) + k  when k is negative
print(nums[-1])     # 50           last ELEMENT (not a list)
print(nums[-1:])     # [50]          last element as a one-item LIST
print(nums[-3:])     # [30, 40, 50]  last 3  (same as [k:] with negative k)
print(nums[:-1])     # [10, 20, 30, 40]  all but last  ([:k] with k=-1)
print(nums[:-2])     # [10, 20, 30]  all but last 2
print(nums[-5:])      # [10, 20, 30, 40, 50]  whole list (k at start)

# Step — third argument
print(nums[::2])    # [10, 30, 50]   every 2nd item
print(nums[::-1])   # [50, 40, 30, 20, 10]  reversed COPY

# [::-1] trick — Java lastIndexOf (no built-in in Python)
# Reverse copy → .index finds first in reversed (= last in original) → flip index
fruits = ["apple", "banana", "cherry", "banana"]
#          0        1         2         3
print(fruits[::-1])                                    # reversed view
print(fruits[::-1].index("banana"))                    # 0 (position in reversed)
print(len(fruits) - 1 - fruits[::-1].index("banana"))  # 3 — ≈ lastIndexOf
# Mirror rule: original index i  ↔  reversed index (len - 1 - i)
# Also in lesson_02/01_collections.py (§1 list)

# Slicing never mutates the original
copy = nums[:]
copy[0] = 999
print(nums[0])      # 10 — original unchanged

# Common patterns in practice
words = ["a", "b", "c", "d", "e"]
print(words[::2])           # every other — used in every_other()
print(sorted(nums, reverse=True)[:2])  # top 2 — used in top_n()

# chunk pattern
size = 2
items = ["a", "b", "c", "d", "e"]
for i in range(0, len(items), size):
    print(items[i : i + size])
