"""Lesson 1e — loops (for, while, break, continue).

Deeper loop patterns: 08_builtins.py (enumerate), 11_comprehensions.py (replace many loops).

Run:
    uv run python lesson_04/01_loops.py
"""

fruits = ["apple", "banana", "cherry", "date"]
scores = {"alice": 95, "bob": 87}

# --- for loops ---
for fruit in fruits:
    print(f"  fruit: {fruit}")

# for k in scores  → keys only (like keySet). Use .items() when you need both:
for key, value in scores.items():
    print(f"  {key} -> {value}")

for i in range(3):
    print(f"  index {i}: {fruits[i]}")

# --- while (Java: while (cond) { ... }) ---
n = 3
while n > 0:
    print(f"  countdown: {n}")
    n -= 1

# --- break / continue (same keywords as Java) ---
for word in ["skip", "stop", "gone"]:
    if word == "stop":
        break
    print(f"  word: {word}")

for num in range(5):
    if num % 2 == 0:
        continue
    print(f"  odd: {num}")

# --- for-else: else runs only if loop did NOT break (no Java equivalent) ---
target = "cherry"
for fruit in fruits:
    if fruit == target:
        print(f"  found {target}")
        break
else:
    print(f"  {target} not in list")
