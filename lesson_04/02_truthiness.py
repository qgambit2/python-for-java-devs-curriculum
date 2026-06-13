"""Lesson 1m — truthiness, is vs == (critical for Java devs)."""

# Falsy values — empty or zero-ish
falsy = [None, False, 0, 0.0, "", [], {}, set()]
for value in falsy:
    print(repr(value), "->", bool(value))

# Truthy — everything else
print(bool("hello"), bool([1]), bool({"a": 1}))

# == compares VALUES
# is compares IDENTITY (same object in memory) — like Java ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)   # True  — same contents
print(a is b)   # False — different list objects
print(a is c)   # True  — same object

# NEVER use `is` for numbers/strings content checks
# WRONG: if index is None  — only True for the one None singleton
x = None
print(x is None)    # correct way to check for None
print(x == None)    # works but style guides prefer `is None`

# Practical patterns
name = ""
if name:                    # False for empty string
    print("has name")
else:
    print("no name")

scores = [90, 85]
if scores:                  # False only for empty list
    print("has scores")
