"""Lesson 1c — control flow (Java if / for / while / switch → Python).

Read after 01_syntax.py and 02_variables.py — before collections (Lesson 2).
Lesson 4 adds truthiness, is vs ==, and functions on top of this.

Run:
    uv run python lesson_01/03_control_flow.py

Practice:
    uv run python lesson_01/practice/02_control_flow.py
"""


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java control flow map")

print("""
| Java                         | Python                          |
|------------------------------|---------------------------------|
| if (x > 0) { }               | if x > 0:                       |
| else if (x < 0) { }          | elif x < 0:                     |
| else { }                     | else:                           |
| for (int i=0; i<n; i++)      | for i in range(n):              |
| for (T x : list)             | for x in list:   ← primary      |
| while (cond) { }             | while cond:                     |
| do { } while (cond);         | no direct form — see §5         |
| switch (x) { case A: ... }   | match x: case A: ...  (3.10+)  |
| break / continue             | break / continue  (same)        |
""")


section("1. if / elif / else — no parentheses required")

score = 85

# Java:
#   if (score >= 90) {
#       grade = "A";
#   } else if (score >= 80) {
#       grade = "B";
#   } else {
#       grade = "C";
#   }

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"score={score} grade={grade}")

# Combined conditions — and / or / not (Java: && || !)
age, has_ticket = 20, True
if age >= 18 and has_ticket:
    print("admit")
else:
    print("deny")


section("2. for — iterate collections (Java enhanced for)")

fruits = ["apple", "banana", "cherry"]

# Java: for (String fruit : fruits) { ... }
for fruit in fruits:
    print(f"  fruit: {fruit}")

# Java: for (int i = 0; i < fruits.size(); i++)
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# Prefer direct iteration when you only need values:
#   for fruit in fruits:   not for i in range(len(fruits)):

# range(stop) — 0 .. stop-1 (stop exclusive)
# Java equivalents:
#
#   C-style for (classic):
#     for (int i = 0; i < 5; i++) { }        // 0..4
#     for (int i = 2; i < 5; i++) { }        // 2..4
#     for (int i = 0; i < 10; i += 2) { }    // 0,2,4,6,8
#
#   IntStream.range (Java 8+) — lazy sequence, end exclusive (like Python):
#     IntStream.range(0, 5)                  // 0..4  ≈ range(5)
#     IntStream.range(2, 5)                  // 2..4  ≈ range(2, 5)
#     // no 3-arg range — step: for (i=0; i<10; i+=2) or IntStream.iterate(0, i -> i+2).limit(5)
#
#   IntStream.rangeClosed(1, 5)              // 1..5 INCLUSIVE — use range(1, 6) in Python
#
# list(...) materializes — range itself is lazy (like IntStream until .toArray() / collect)
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 5)))        # [2, 3, 4]
print(list(range(0, 10, 2)))     # [0, 2, 4, 6, 8]


section("3. while — same keyword as Java")

# Java: while (n > 0) { n--; }
n = 3
while n > 0:
    print(f"  countdown: {n}")
    n -= 1


section("4. break / continue — same as Java")

for word in ["skip", "stop", "gone"]:
    if word == "stop":
        break
    print(f"  word: {word}")

for num in range(5):
    if num % 2 == 0:
        continue
    print(f"  odd: {num}")


section("5. do/while — no direct form in Python")

print("""
Java:
    do {
        line = readLine();
    } while (line != null);

Python — run body at least once, then test at bottom:
""")

# Pattern A: while True + break
attempts = 0
while True:
    attempts += 1
    print(f"  try {attempts}")
    if attempts >= 2:
        break

# Pattern B: run once before while (when you already have the first value)
# data = read()
# while data is not None:
#     process(data)
#     data = read()


section("6. switch / case → match / case (Python 3.10+)")

print("""
Java switch (modern, no fall-through with ->):
    switch (status) {
        case 200 -> result = "ok";
        case 404 -> result = "missing";
        case 500, 502, 503 -> result = "server error";
        default -> result = "other";
    }

Python match (3.10+) — direct equivalent:
    match status:
        case 200: ...
        case 404: ...
        case 500 | 502 | 503: ...
        case _: ...          # default

Key differences from OLD Java switch:
  - Python cases do NOT fall through — no 'break' needed (like Java switch ->)
  - '_' is default (like default:)
  - Multiple values: case 500 | 502 | 503  (like case 500, 502, 503 in Java)
""")

status = 404


def http_label(code: int) -> str:
    match code:
        case 200:
            return "ok"
        case 404:
            return "missing"
        case 500 | 502 | 503:
            return "server error"
        case _:
            return "other"


print(f"status {status} -> {http_label(status)}")

# match on strings — like switch on String:
def command_label(cmd: str) -> str:
    match cmd:
        case "start":
            return "starting"
        case "stop":
            return "stopping"
        case _:
            return "unknown"


print(command_label("start"))

# match is a statement, not an expression — assign inside each case (or use a helper):
def http_label_assign(code: int) -> str:
    result = "other"
    match code:
        case 200:
            result = "ok"
        case 404:
            result = "missing"
    return result


print(f"assign inside cases: {http_label_assign(404)}")

# case with guard — like case x when x > 0 (Java 21+ guarded patterns):
def sign_word(n: int) -> str:
    match n:
        case 0:
            return "zero"
        case x if x > 0:
            return "positive"
        case _:
            return "negative"


print(f"sign_word(5)={sign_word(5)} sign_word(-3)={sign_word(-3)}")

# Before match (or simple switches): if/elif chain — still valid
def http_label_elif(code: int) -> str:
    if code == 200:
        return "ok"
    elif code == 404:
        return "missing"
    else:
        return "other"


# Or dict dispatch — like Map.of(200, "ok", 404, "missing"):
HTTP = {200: "ok", 404: "missing", 500: "server error"}
print(HTTP.get(404, "other"))


section("7. for-else — Python only (no Java equivalent)")

target = "cherry"
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == target:
        print(f"  found {target}")
        break
else:
    print(f"  {target} not in list")
# else runs only if loop did NOT break — Java: use a boolean found flag


section("8. What comes next")

print("""
Lesson 2 — collections (list, dict, for key, value in d.items())
Lesson 4 — truthiness (if name:), is vs ==, def functions
""")
