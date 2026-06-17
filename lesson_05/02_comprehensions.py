"""Lesson 1k — comprehensions (idiomatic filter/map in one expression)."""

nums = [1, 2, 3, 4, 5, 6]

# List comprehension — like stream().map().filter().collect()
evens = [n for n in nums if n % 2 == 0]
squares = [n * n for n in nums]
print(evens, squares)

# Java equivalent of evens:
# nums.stream().filter(n -> n % 2 == 0).collect(toList())

# Dict comprehension
word_lengths = {word: len(word) for word in ["hi", "hey", "hello"]}
print(word_lengths)

# Invert a map — keys become values (duplicate values: last key wins)
scores = {"alice": 95, "bob": 87}
by_score = {score: name for name, score in scores.items()}
# same: {scores[n]: n for n in scores}
print(by_score)

# Transform values — new dict, sorted lists (anagram_groups pattern)
# NEED .items() — {k: sorted(v) for k, v in groups} is WRONG (loops keys only)
groups = {"aet": ["eat", "tea", "ate"]}
print({k: sorted(v) for k, v in groups.items()})
# same: {k: sorted(groups[k]) for k in groups}

# Merge dicts — comprehension over all keys (| unions keys — see 12_sets.py)
left = {"alice": 10, "bob": 5}
right = {"bob": 3, "carol": 7}
merged = {name: left.get(name, 0) + right.get(name, 0) for name in left.keys() | right.keys()}
print(merged)   # {'bob': 8, 'carol': 7, 'alice': 10}

# Set comprehension — unique values
unique_lengths = {len(word) for word in ["hi", "hey", "yo", "hello"]}
print(unique_lengths)

# Generator expression — lazy (like Stream), use with sum/any/max/sorted
total = sum(n * n for n in nums if n % 2 == 1)  # sum of odd squares
print(total)

# sorted + generator — both work; omit [] when sorted is the only consumer
before = {"alice": 50, "bob": 70}
after = {"alice": 50, "bob": 65, "carol": 40}
changed = sorted(name for name, score in after.items() if before.get(name, 0) != score)
print(changed)   # ['bob', 'carol']
# sorted([name for ...])  # same result — extra list allocation

# Nested — flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)

# When NOT to use — keep regular loops for complex logic or side effects
# Bad: [print(x) for x in nums]   # works but weird — use a for loop
