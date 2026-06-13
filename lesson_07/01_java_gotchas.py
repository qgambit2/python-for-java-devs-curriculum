"""Lesson 1n — Java habits that bite in Python."""

# 1. No i++ or i--
count = 0
count += 1   # use this, not count++

# 2. elif not else if
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:   # one word!
    grade = "B"
else:
    grade = "C"

# 3. Boolean literals are capitalized
is_active = True    # not true

# 4. Default args are evaluated ONCE at definition time (gotcha!)
def add_item(item, bucket=[]):  # DON'T do this
    bucket.append(item)
    return bucket

# Safe pattern:
def add_item_safe(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item_safe("a"))
print(add_item_safe("b"))   # ['b'] — fresh list each call

# 5. No method or constructor overloading — last definition wins
# def greet(name): ...
# def greet(name, age): ...  # replaces the first!
# def __init__(self, name): ...
# def __init__(self, name, age): ...  # same for constructors — only ONE __init__

# Use default args or different names instead:
def greet(name: str, times: int = 1) -> str:
    return f"Hi {name}! " * times

# class Person:
#     def __init__(self, name: str, age: int = 0) -> None:  # ≈ Person(String) + Person(String, int)
#         self.name = name
#         self.age = age

# 6. Indentation is syntax — mixing tabs/spaces breaks things

# 7. list.sort() returns None (mutates in place)
nums = [3, 1, 2]
result = nums.sort()   # result is None!
print(nums)            # [1, 2, 3] — nums was sorted

# 8. Save before running tests — editor buffer != disk file
