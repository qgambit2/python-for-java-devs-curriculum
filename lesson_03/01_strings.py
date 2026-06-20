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


section("0. Java String → Python str map")

print("""
| Java                                    | Python str                               |
|-----------------------------------------|------------------------------------------|
| String.format("%s! You are %d.", n, a)  | f"{name}! You are {age}."                |
| String.format("%.2f", price)            | f"{price:.2f}"                           |
| String.format("%8s", "id")              | f"{label:>8}"   (right-align in field)   |
| String.format("%-8s", "id")             | f"{label:<8}"   (left-align)             |
| manual pad / StringUtils.center(s, 8)   | f"{label:^8}"   (center — no % flag)     |
| String.format("%-10s%4d", name, score)  | f"{name:<10}{score:>4}"                 |
| String.format("%#x", 255)               | f"{255:#x}"  (0x prefix, lowercase)      |
| String.format("0x%02X", 255)            | f"0x{255:02X}"  (uppercase, zero-pad)    |
| String.format("%05d", 7)                | f"{7:05d}"                               |
| template.formatted(name, bal)  (15+)    | template.format(name=..., balance=...)   |
| System.out.printf("%s %d", n, s)        | print("%s %d" % (name, score))           |
| String.join(", ", parts)                | ", ".join(parts)                         |
| "=".repeat(5)                           | "=" * 5                                  |
| "ab".repeat(3)                          | "ab" * 3                                 |
| s.length()                              | len(s)                                   |
| s.charAt(0)                             | s[0]                                     |
| s.charAt(s.length() - 1)                | s[-1]                                    |
| s.substring(1, 4)                       | s[1:4]                                   |
| s.contains("world")                       | "world" in s                             |
| s.equals("hello")                       | s == "hello"                             |
| s.equalsIgnoreCase("HI")                | s.lower() == "hi".lower()  (or casefold) |
| s.trim()                                | s.strip()                                |
| s.split(",")                            | s.split(",")  → list[str]                |
| s.replace("foo", "baz")                 | s.replace("foo", "baz")                  |
| s.indexOf("x")  (-1 if missing)         | s.find("x")                              |
| s.startsWith("pre") / endsWith(".csv")  | s.startswith / s.endswith                |
| s.toUpperCase() / toLowerCase()         | s.upper() / s.lower()                    |
| obj.toString() in concat                | f"{obj}"  → __str__ / __repr__ path      |
| Pattern.compile("\\\\d+") + Matcher     | re.compile(r"\\d+") / re.search          |
| only "..." for String; 'a' is char      | 'a' and "a" are both str                 |
| "C:\\\\new"  or  Java 15 text blocks   | "C:\\\\new"  or  r"C:\\new"  or  \"\"\"  |
""")


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
# Java:
#   String msg = String.format("Hello, %s! You are %d.", name, age);
#   // Java 15+: "Hello, %s! You are %d.".formatted(name, age);
print(f"Hello, {name}! You are {age}.")       # Hello, Alex! You are 30.
print(f"Next year: {age + 1}")                # Next year: 31 — expression inside {}


section("2. Format specifiers — {value:spec} with example output")

price = 12.5
count = 42
ratio = 0.875
# Java one-liners (String.format):
#   String.format("%.2f", price)        → 12.50
#   String.format("%d", count)          → 42
#   String.format("%,d", 1_000_000)     → 1,000,000
#   Hex digit count — %#x uses minimal digits; %02X pads to at least 2 (byte style):
#     n=255:  %#x → 0xff     0x%02X → 0xFF
#     n=15:   %#x → 0xf      0x%02X → 0x0F   ← padding shows on small values
#     n=0:    %#x → 0x0      0x%02X → 0x00
#   Integer.toHexString(n) → ff / f / 0  (no 0x prefix, no width pad)
#   String.format("%05d", 7)            → 00007
# Python f-string {value:spec} mirrors printf-style flags after the colon:
print(f"price={price:.2f}")       # price=12.50      Java: %.2f
print(f"count={count:d}")         # count=42         Java: %d
print(f"ratio={ratio:.1%}")       # ratio=87.5%      Java: no direct % — use NumberFormat
print(f"big={1_000_000:,}")       # big=1,000,000    Java: %,d
print(f"hex={255:#x}")            # hex=0xff         Java: %#x — 255 → minimal digits
print(f"hex={15:#x}")             # hex=0xf          Java: %#x — 15 → one digit (no pad)
print(f"0x{255:02X}")             # 0xFF             Java: 0x%02X — 255 → two digits
print(f"0x{15:02X}")              # 0x0F             Java: 0x%02X — 15 → padded to 2
print(f"0x{0:02X}")               # 0x00             Java: 0x%02X — 0 → padded to 2
print(f"pad={7:05d}")             # pad=00007        Java: %05d


section("3. Width & alignment")

label = "id"
# Java:
#   String.format("|%8s|", "id")    → |      id|   (right-align — default for %s)
#   String.format("|%-8s|", "id")   → |id      |   (left-align)
#   Center — no printf flag; pad manually or use Apache Commons StringUtils.center("id", 8)
#   int pad = 8 - "id".length(); int left = pad / 2;
#   " ".repeat(left) + "id" + " ".repeat(pad - left)   → |   id   |
print(f"|{label:>8}|")           # |      id|       Java: %8s
print(f"|{label:<8}|")           # |id      |       Java: %-8s
print(f"|{label:^8}|")           # |   id   |       Java: manual / StringUtils.center
print(f"|{'9':*>8}|")            # |******9|  * fill — Java: no printf fill-char flag


section("4. f-string conversions — !s !r !a · str() vs repr()")

# Java has one path: obj.toString() in concat / String.valueOf(obj).
# Python splits human (str) vs debug (repr) — f-strings expose both via !s / !r / !a.

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
# Java: no f"{score=}" — use "score=" + score or debugger / IDE evaluates
print(f"{score=}")               # score=42  (= suffix — Python 3.8+; variable name must be literal)
label, value = "score", 42
print(f"{label}={value}")        # score=42  (dynamic label — build manually)


section("5. Literal braces & combined prefixes")

# Literal { } in output — double them (Java String.format also uses {{ and }}):
#   String.format("set literal: {{1, 2, 3}}")  → set literal: {1, 2, 3}
print(f"set literal: {{1, 2, 3}}")   # set literal: {1, 2, 3}
print(f"{{name}} placeholder")       # {name} placeholder

# fr / rf = raw + formatted (order doesn't matter)
# Java: no raw f-string — escape backslashes: "C:\\users\\" + name + "\\file.txt"
print(fr"C:\users\{name}\file.txt")  # backslashes preserved + interpolated


section("6. str.format() — reusable template")

# Java:
#   String template = "Dear %s, your balance is $%.2f.";
#   String.format(template, "Alice", 1234.5);
#   // Java 15+: "Dear %s, balance $%.2f".formatted("Alice", 1234.5);
# Python named placeholders read like a small DSL:
template = "Dear {name}, your balance is ${balance:.2f}."
print(template.format(name="Alice", balance=1234.5))
# Dear Alice, your balance is $1234.50.

print("({}, {})".format(10, 20))     # (10, 20)   Java: String.format("(%d, %d)", 10, 20)

# **kwargs — COLLECT in def, UNPACK in .format() (see book Lesson 3 § format_template)
#   def f(**kwargs):     → kwargs is a dict
#   g(**kwargs)          → spread dict into keyword args (NOT g(kwargs))
def format_template(template: str, **kwargs: object) -> str:
    return template.format(**kwargs)

print(format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5))


section("7. Legacy % formatting")

name, score = "Bob", 95
# Java: System.out.printf("%s scored %d%n", name, score);
#       String.format("%s scored %d", name, score);
print("%s scored %d" % (name, score))  # Bob scored 95
print("literal %% sign")               # literal % sign   Java: "literal %% sign"


section("8. join — preferred over += in loops")

parts = ["Python", "Java", "Go"]
# str is IMMUTABLE — s += x allocates a new string; += in a loop is O(n²) (see book § antipattern).
#
# Java antipattern (same immutability):
#   String result = "";
#   for (String p : parts) result += p;     // BAD — new String each iteration
#
# Java fixes:
#   String.join(", ", parts);               // when you have a list
#   StringBuilder sb = new StringBuilder();
#   for (String p : parts) sb.append(p);
#   String result = sb.toString();        // when building in a loop
#
# Python fixes:
#   ", ".join(parts)                        // when you have a list
#   chunks = []; ... chunks.append(x); "".join(chunks)  // when building in a loop
print(", ".join(parts))              # Python, Java, Go
print("".join(sorted("cba")))        # abc

print("--- sorted(string) trap ---")
print(sorted("cba"))                 # ['a', 'b', 'c']  — list of one-char strings
print("".join(sorted("cba")))        # abc              — str again
# Java: char[] chars = "cba".toCharArray(); Arrays.sort(chars); new String(chars);
#       String.join("", Arrays.stream(chars).map(String::valueOf).toList());
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
# Java:
#   Point p = new Point(3, 4);
#   System.out.println("point=" + p);   // calls p.toString()
#   // @dataclass / record generates toString() like Python's generated __repr__
print(f"point={p}")                  # point=Point(x=3, y=4)  — uses __repr__ via str path
print(f"point={p!r}")                # same here for dataclass — explicit repr
print(repr(p))                       # 'Point(x=3, y=4)'  — repr on any object


section("12. Indexing & slicing — str is a sequence (like list)")

text = "Python"
# Java: charAt / substring — Python also allows negative indices (from the end)
print(text[0])                       # P          Java: text.charAt(0)
print(text[-1])                      # n          Java: text.charAt(text.length() - 1)
print(text[1:4])                     # yth        Java: text.substring(1, 4)  — end exclusive
print(text[::2])                     # Pto        every 2nd char — Java: manual loop or chars
print(len(text))                     # 6          Java: text.length() — len() is a function, not .length()


section("13. Membership & equality")

s = "hello world"
# Java: contains / equals — use == not .equals on literals (Python has no .equals method)
print("world" in s)                  # True       Java: s.contains("world")
print("World" in s)                  # False      case-sensitive
print(s == "hello world")            # True       Java: s.equals("hello world")
print(s != "hi")                     # True
# Java equalsIgnoreCase: s.equalsIgnoreCase("WORLD")  →  s.lower() == "world".lower()


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
# Java: replace replaces ALL occurrences; no built-in count — loop indexOf
print(msg.replace("foo", "baz"))     # 'baz bar baz'   Java: replace("foo", "baz")
print(msg.replace("foo", "baz", 1))  # 'baz bar foo'   max 1 — Java: replaceFirst via regex
print("hello".count("l"))            # 2               Java: manual indexOf loop
print("mississippi".count("iss"))    # 2               overlapping counts non-overlapping matches


section("17. find, index, startswith, endswith")

hay = "hello world"
# Java indexOf returns -1; Python find returns -1; index() raises ValueError
print(hay.find("world"))             # 6          Java: indexOf("world")
print(hay.find("xyz"))               # -1         Java: indexOf("xyz") when missing
# hay.index("xyz")                   # ValueError — stricter read (no -1 sentinel)
print(hay.startswith("hello"))       # True       Java: startsWith("hello")
print(hay.endswith("world"))         # True       Java: endsWith("world")
print("report.csv".endswith((".csv", ".tsv")))  # True — tuple = any suffix (Java: endsWith one at a time)


section("18. Case — upper, lower, title")

label = "Hello World"
print(label.upper())                 # HELLO WORLD   Java: toUpperCase()
print(label.lower())                 # hello world   Java: toLowerCase()
print(label.title())                 # Hello World   Java: no direct equivalent (WordUtils etc.)
print("café".casefold())             # café — better than lower() for case-insensitive compare (Java: toLowerCase(Locale.ROOT) + normalize)


section("19. Char counts — .count() in a dict comprehension")

# Pattern from lesson_02/practice/02_collections.py (char_counts exercise)
# Java: Map<Character,Integer> counts = new HashMap<>();
#       for (char c : sample.toCharArray()) counts.merge(c, 1, Integer::sum);
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
