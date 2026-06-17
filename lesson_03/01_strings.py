"""Lesson 3 — strings: operations & formatting (Java String → Python str).

Indexing, split/strip/count, f-strings, join, escaping, regex (re).
OOP hooks → lesson_08/03_str_repr_and_formatting.py

Run:
    uv run python lesson_03/01_strings.py

Practice:
    uv run python lesson_03/practice/01_strings.py
    uv run python lesson_03/practice/02_string_ops.py
"""


def section(title: str) -> None:
    # '=' * 60  →  60 equals signs (Java 11+: "=".repeat(60))
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Quick intro — f-string hello")

name = "Alex"
print(f"Hello, {name}!")
print(r"C:\new\folder")
word = "eat"
print(sorted(word))                # ['a', 'e', 't']  — sorted() ALWAYS returns a list
print("".join(sorted(word)))      # aet              — join list[str] back into one str
# print(sorted(word)) alone does NOT print "aet" — see section 8


section("0b. Single vs double quotes — both are str")

print("hello")                       # str
print('hello')                       # same str — Java: only " for String
print('a')                           # one-char str — Java: 'a' is char, not String
print("it's fine")                   # apostrophe inside double quotes — no escape
print('say "hi"')                    # double quotes inside single quotes
print('it\'s also fine')             # or backslash escape — same as Java \'
# Output like ['a', 'e', 't'] uses single quotes in *display* (repr of list elements)


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


section("4. f-string conversions — !s !r !a · str() vs repr()")

word = "hi"
items = ["a", "b"]
print(f"!s → {word!s}")           # !s → hi       — str(word); default if flag omitted
print(f"!r → {word!r}")           # !r → 'hi'     — repr(word); quotes in output
print(f"plain → {word}")          # plain → hi    — same as !s
print(f"list !r → {items!r}")     # repr(whole list) — ['a', 'b']

print("--- str() vs repr() ---")
print(str(word), repr(word))      # hi  'hi'
print(str(items), repr(items))    # ['a', 'b']  ['a', 'b']  — lists often look alike
s = "line1\nline2"
print(f"str: {s}")                # real newline
print(f"repr: {s!r}")             # 'line1\nline2'  — escapes visible

# repr(x) calls x.__repr__() on any object (Lesson 8: __str__ vs __repr__)
# !s is optional — only !r and !a change behavior

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

print("--- sorted(string) trap ---")
print(sorted("cba"))                 # ['a', 'b', 'c']  — list of one-char strings
print("".join(sorted("cba")))        # abc              — str again
# Java: sort char[] then new String(chars) / String.join("", parts)
# sorted() never returns str — always list; use "".join(...) when you need a string


section("9. Escaping quotes & backslashes — Java vs Python")

# Quotes — same \" as Java, OR alternate quote style (Java has no '...' strings):
print("He said \"hello\"")           # He said "hello"
print('He said "hello"')             # same — inner " needs no \
print("it's fine")                   # apostrophe in double-quoted str
print('it\'s fine')                  # apostrophe escaped in single-quoted str

# Control chars — same as Java inside "..." : \n \t \r \\
print("line1\nline2")                # line1  + newline  + line2
print("tab\there")                   # tab    + here

# Backslashes — TWO equivalent ways (raw is optional sugar; \\ is the standard escape):
print("C:\\new\\folder")             # Way 1: \\ — same as Java "C:\\new\\folder"
print(r"C:\new\folder")              # Way 2: r"..." — same result, less typing
print(r"\n\t\\")                      # raw: \n \t \\ stay literal (not newline/tab)
print("unicode: \u0041")             # unicode: A  — Java: "\u0041"

print("""line1
line2""")                            # triple quotes — multiline (Java 15+ text blocks)


section("10. When to use \\ vs raw r\"...\"")

print("C:\\new" == r"C:\new")        # True — same string, two ways to write it
# Use "..." with \\ when you WANT \n \t as control characters:
print("line1\nline2")                # real newline
# Use r"..." for paths, regex — backslashes stay literal (\n is NOT newline):
print(r"line1\nline2")               # prints line1\nline2 literally
# Raw is optional — not a separate string type; fr"..." = raw f-string for paths

print(b"ascii bytes")                # b'ascii bytes'  — bytes literal, not str


section("11. Objects in f-strings → str path")

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(3, 4)
print(f"point={p}")                  # point=Point(x=3, y=4)  — uses __repr__ via str path
print(f"point={p!r}")                # same here for dataclass — explicit repr
print(repr(p))                       # 'Point(x=3, y=4)'  — repr on any object


section("12. Indexing & slicing — str is a sequence (like list)")

text = "Python"
print(text[0])                       # P          Java: text.charAt(0)
print(text[-1])                      # n          Java: text.charAt(text.length() - 1)
print(text[1:4])                     # yth        Java: text.substring(1, 4)
print(text[::2])                     # Pto        every 2nd char
print(len(text))                     # 6          Java: text.length() — len() is a function, not .length()


section("13. Membership & equality")

s = "hello world"
print("world" in s)                  # True       Java: s.contains("world")
print("World" in s)                  # False      case-sensitive
print(s == "hello world")            # True       Java: s.equals("hello world")
print(s != "hi")                     # True


section("14. split — opposite of join; returns a list")

line = "alice:95,bob:87"
print(line.split(","))               # ['alice:95', 'bob:87']     Java: split(",")
print(line.split(":", 1))            # ['alice', '95,bob:87']     maxsplit=1 — rest stays
print("a\nb\nc".splitlines())        # ['a', 'b', 'c']            Java: split("\\R")

# Rejoin after split — common parse/transform pattern
parts = "  one   two  three  ".split()   # default: whitespace, runs collapsed
print(parts)                         # ['one', 'two', 'three']
print(" ".join(parts))               # 'one two three'


section("15. strip — trim leading/trailing whitespace")

raw = "  hello  \n"
print(raw.strip())                   # 'hello'    Java: trim() — no separate method name
print("***hi***".strip("*"))         # 'hi'       optional chars to strip
print("  left".lstrip())             # 'left'
print("right  ".rstrip())            # 'right'


section("16. replace & count")

msg = "foo bar foo"
print(msg.replace("foo", "baz"))     # 'baz bar baz'   Java: replace("foo", "baz") — all occurrences
print(msg.replace("foo", "baz", 1))  # 'baz bar foo'   max 1 replacement
print("hello".count("l"))            # 2               Java: no one-liner — loop indexOf
print("mississippi".count("iss"))    # 2               overlapping counts non-overlapping matches


section("17. find, index, startswith, endswith")

hay = "hello world"
print(hay.find("world"))             # 6          Java: indexOf — returns -1 if missing
print(hay.find("xyz"))               # -1
# hay.index("xyz")                   # ValueError — like indexOf that throws
print(hay.startswith("hello"))       # True       Java: startsWith
print(hay.endswith("world"))         # True       Java: endsWith
print("report.csv".endswith((".csv", ".tsv")))  # True — tuple = any suffix


section("18. Case — upper, lower, title")

label = "Hello World"
print(label.upper())                 # HELLO WORLD   Java: toUpperCase()
print(label.lower())                 # hello world   Java: toLowerCase()
print(label.title())                 # Hello World   Java: no direct equivalent
print("café".casefold())             # café — better than lower() for case-insensitive compare


section("19. Char counts — .count() in a dict comprehension")

# Pattern from lesson_02/practice/02_collections.py (char_counts exercise)
sample = "hello"
counts = {c: sample.count(c) for c in sample if c != " "}
print(counts)                        # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# For large text, a single loop with a dict is O(n); .count per char is fine for learning.


section("20. Regular expressions — re module (≈ java.util.regex)")

import re

# Java:
#   Pattern p = Pattern.compile("\\d+");
#   Matcher m = p.matcher(text);
#   if (m.find()) { String hit = m.group(); }
#   String all = p.matcher(text).replaceAll("-");
# Python: use raw strings for patterns — r"\d+" not "\\d+"

text = "Order 42: ship 7-10 days"
print(re.search(r"\d+", text))           # <re.Match ...>  — first match object or None
m = re.search(r"\d+", text)
print(m.group() if m else None)         # 42              — Java: m.group()
print(re.findall(r"\d+", text))        # ['42', '7', '10'] — all matches as strings
print(re.sub(r"\d+", "#", text))       # Order #: ship #-# days  — replaceAll

# Anchors — match whole string?
print(bool(re.fullmatch(r"\d+", "42")))    # True   — Java: matches() on whole input
print(bool(re.fullmatch(r"\d+", "x42")))  # False
print(bool(re.match(r"\d+", "42 days")))   # True   — Java: lookingAt() / starts with

email = "Contact: alice@example.com or bob@test.org"
print(re.findall(r"[\w.]+@[\w.]+", email))  # quick demo — not production email regex

# Compile once, reuse — Java: Pattern.compile cached
digits = re.compile(r"\d+")
print(digits.findall("a1 b22"))        # ['1', '22']

# When str methods are enough, prefer them (faster, clearer):
#   "abc".startswith("a")  beats  re.match(r"a", "abc")
#   split / replace / in   before reaching for regex
