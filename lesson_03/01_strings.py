"""Lesson 1e — strings & formatting (Java String.format / printf → Python).

Basics + f-strings, specifiers, join, escaping. OOP hooks → lesson_08/03_str_repr_and_formatting.py

Run:
    uv run python lesson_03/01_strings.py

Practice:
    uv run python lesson_03/practice/01_strings.py
"""


def section(title: str) -> None:
    # '=' * 60  →  60 equals signs (Java 11+: "=".repeat(60))
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Quick intro — f-string hello")

name = "Alex"
print(f"Hello, {name}!")
print(r"C:\new\folder")
word = "eat"
print("".join(sorted(word)))   # anagram key pattern


section("1. Repeat & concat — building strings without a loop")

print("=" * 5)              # '====='     Java: "=".repeat(5)
print("ab" * 3)               # 'ababab'    Java: "ab".repeat(3)
print("hi" + " " + "there")   # 'hi there'  Java: "hi" + " " + "there"
print("-" * 0)                # ''          zero repeat → empty


section("2. f-strings — prefix `f` (or `F`); default choice")

name = "Alex"
age = 30
# Java: String.format("Hello, %s! You are %d.", name, age)
print(f"Hello, {name}! You are {age}.")       # Hello, Alex! You are 30.
print(f"Next year: {age + 1}")                # Next year: 31


section("2. Format specifiers — {value:spec} with example output")

price = 12.5
count = 42
ratio = 0.875
print(f"price={price:.2f}")       # price=12.50      Java: %.2f
print(f"count={count:d}")         # count=42         Java: %d
print(f"ratio={ratio:.1%}")       # ratio=87.5%      percent style
print(f"big={1_000_000:,}")       # big=1,000,000    thousands comma
print(f"hex={255:#x}")            # hex=0xff         Java: %#x
print(f"pad={7:05d}")             # pad=00007        zero-fill width 5


section("3. Width & alignment")

label = "id"
print(f"|{label:>8}|")           # |      id|
print(f"|{label:<8}|")           # |id      |
print(f"|{label:^8}|")           # |   id   |
print(f"|{'9':*>8}|")            # |******9|  * is fill char


section("4. f-string conversions — !s !r !a (after expression, before :)")

word = "hi"
print(f"!s → {word!s}")           # !s → hi
print(f"!r → {word!r}")           # !r → 'hi'
print(f"!a → {'café'!a}")         # !a → 'caf\xe9'  (ascii-safe repr)

score = 42
print(f"{score=}")               # score=42  (= suffix — Python 3.8+; variable name must be literal)
label, value = "score", 42
print(f"{label}={value}")        # score=42  (dynamic label — build manually)


section("5. Literal braces & combined prefixes")

# Literal { } in output — double them
print(f"set literal: {{1, 2, 3}}")   # set literal: {1, 2, 3}
print(f"{{name}} placeholder")       # {name} placeholder

# fr / rf = raw + formatted (order doesn't matter)
print(fr"C:\users\{name}\file.txt")  # backslashes preserved + interpolated


section("6. str.format() — reusable template")

template = "Dear {name}, your balance is ${balance:.2f}."
print(template.format(name="Alice", balance=1234.5))
# Dear Alice, your balance is $1234.50.

print("({}, {})".format(10, 20))     # (10, 20)


section("7. Legacy % formatting")

name, score = "Bob", 95
print("%s scored %d" % (name, score))  # Bob scored 95
print("literal %% sign")               # literal % sign


section("8. join — preferred over += in loops")

parts = ["Python", "Java", "Go"]
print(", ".join(parts))              # Python, Java, Go
print("".join(sorted("cba")))        # abc


section("9. Escaping — Java vs Python (with output)")

# SAME as Java inside "..." : \" \\ \n \t \r
print("He said \"hello\"")           # He said "hello"
print("line1\nline2")                # line1  + newline  + line2
print("tab\there")                   # tab    + here

# Backslashes — Python has TWO ways (Java: escaped "..." only):
print("C:\\new\\folder")             # Way 1: escaped — same as Java "C:\\new\\folder"
print(r"C:\new\folder")              # Way 2: raw r"..." — same output, no \\ doubling
print(r"\n\t\\")                      # raw: \n\t\\ literal (escaped would be "\\n\\t\\\\")

# Other Python options:
print('He said "hello"')             # single quotes — inner " needs no \
print("unicode: \u0041")             # unicode: A  — Java: "\u0041" (same idea)

# Triple-quoted multiline (Java 15+ text blocks are similar)
print("""line1
line2""")                            # two lines


section("10. When to use which backslash style")

# Escaped "..." — use when you WANT \n \t etc. as control characters
print("line1\nline2")                # real newline

# Raw r"..." — use for paths, regex; backslashes stay literal (\n is NOT newline)
print(r"line1\nline2")               # prints line1\nline2 literally

print(b"ascii bytes")                # b'ascii bytes'  — bytes literal, not str


section("11. Objects in f-strings → str path")

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(3, 4)
print(f"point={p}")                  # point=Point(x=3, y=4)
