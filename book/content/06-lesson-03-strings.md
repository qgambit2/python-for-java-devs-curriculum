# Lesson 3 — Strings: operations and formatting

Python `str` is a **sequence** of characters — indexing and slicing work like lists (see Lesson 2). For **building** and **printing** text, Python defaults to **f-strings** instead of Java's `String.format` / `printf`.

**Run:**

```bash
uv run python lesson_03/01_strings.py
```

---

## Java String map

Scan this as a lookup table — each row is explained in the sections below; you don't need to memorize it now.

| Java | Python `str` |
|------|----------------|
| `String.format("%s! You are %d.", name, age)` | `f"{name}! You are {age}."` |
| `String.format("%.2f", price)` | `f"{price:.2f}"` |
| `String.format("%8s", "id")` / `%-8s` | `f"{label:>8}"` / `f"{label:<8}"` |
| manual pad / `StringUtils.center(s, 8)` | `f"{label:^8}"` (center — no `%` flag) |
| `f"{c:*>8}"` fill char | no `printf` fill-char flag — pad/replace manually |
| `String.format("%-10s%4d", name, score)` | `f"{name:<10}{score:>4}"` |
| `String.format("%#x", 255)` / `"%05d"` | `f"{255:#x}"` / `f"{7:05d}"` |
| `String.format("0x%02X", 255)` | `f"0x{255:02X}"` (uppercase byte — practice `hex_byte`) |
| `"Dear %s, $%.2f".formatted(name, bal)` (15+) | `"Dear {name}, ${balance:.2f}".format(...)` |
| `System.out.printf("%s %d", n, s)` | `"%s %d" % (name, score)` |
| `String.join(", ", parts)` | `", ".join(parts)` |
| `"=".repeat(5)` | `"=" * 5` |
| `s.length()` / `charAt` / `substring` | `len(s)` / `s[0]` / `s[1:4]` |
| `s.contains("x")` / `s.equals("hi")` | `"x" in s` / `s == "hi"` |
| `s.trim()` / `split` / `replace` | `strip()` / `split()` / `replace()` |
| `s.indexOf("x")` (-1 if missing) | `s.find("x")` |
| `s.toUpperCase()` / `toLowerCase()` | `s.upper()` / `s.lower()` |
| `obj.toString()` in concat | `f"{obj}"` |
| `Pattern.compile` + `Matcher` | `re.compile` / `re.search` |
| only `"..."` for String; `'a'` is `char` | `'a'` and `"a"` are both `str` |

The demo file prints this table when you run `lesson_03/01_strings.py` (section 0).

---

## Indexing, length, membership

```python
text = "Python"
text[0]          # 'P'     — Java: charAt(0)
text[-1]         # 'n'
text[1:4]        # 'yth'   — Java: substring(1, 4)
len(text)        # 6       — Java: length()  (function, not a method)
"yth" in text    # True    — Java: contains("yth")
```

Strings are **immutable** — slices and methods return new strings; the original is unchanged.

---

## Quote literals — `'` and `"` (both are `str`)

```python
"hello"
'hello'     # identical — pick either; Java: only "..." for String
'a'         # one-character str — Java: 'a' is char, not String
"it's fine" # apostrophe inside double quotes — no escape needed
'say "hi"'  # or alternate quoting style
'it\'s'     # or backslash escape — like Java \" inside "..."
```

When you `print(sorted("eat"))` you see `['a', 'e', 't']` — the **single quotes in output** are how Python **displays** strings in a list (`repr` of each element), not a special “single inside double” literal rule.

---

## split, strip, replace, count

**`split`** breaks a string into a list (opposite of **`join`**):

```python
"a,b,c".split(",")              # ['a', 'b', 'c']
"  one   two   three ".split()  # ['one', 'two', 'three']  — whitespace runs collapsed
" ".join(["one", "two"])        # 'one two'  — parse → transform → rejoin
```

**`strip`** trims ends — Java's `trim()`:

```python
"  hello  \n".strip()           # 'hello'
```

**`replace`** substitutes all occurrences (optional max count):

```python
"foo bar foo".replace("foo", "baz")     # 'baz bar baz'
```

**`count`** counts non-overlapping substrings:

```python
"hello".count("l")              # 2
```

> **Java:** `split`, `trim`, `replace`, `contains`, `startsWith`, `endsWith` map closely. There is no `String.count` — you'd loop `indexOf`.

**Search helpers:**

```python
hay.find("xyz")                 # -1 if missing  — indexOf
hay.startswith("hello")
hay.endswith((".csv", ".tsv"))  # tuple = any suffix
```

**Char-frequency dict** (also used in Lesson 2 practice):

```python
{c: text.count(c) for c in text if c != " "}
```

For large inputs, a single loop over characters is O(n); `.count` per unique char is fine while learning.

---

## Building strings

```python
"=" * 5              # '====='
"ab" * 3             # 'ababab'
"hi" + " " + "there" # concatenation
```

> **Java:** `"=".repeat(5)`, `"ab".repeat(3)`, `"hi" + " " + "there"`.

A few `+` or `+=` on short literals is fine. The **antipattern** is growing a string **inside a loop** — each step allocates a new `str` and copies everything built so far. Because `str` is **immutable** (like Java `String`), nothing is updated in place.

### Antipattern: `+=` in a loop (O(n²))

**Why it hurts:** after `n` appends of similar-sized pieces, you copy roughly `1 + 2 + … + n` characters → **O(n²)**. Same trap as `result += p` in a Java loop without a buffer.

**Python — avoid:**

```python
result = ""
for part in parts:
    result += part          # new str every iteration — copies the whole prefix again
```

**Python — prefer when you already have a list:**

```python
", ".join(parts)
```

**Python — prefer when you build incrementally (no `StringBuilder` in idiomatic code):**

```python
chunks: list[str] = []
for word in words:
    if ok(word):
        chunks.append(transform(word))
return "\n".join(chunks)    # one final str — O(total length)
```

**Java — same antipattern:**

```java
String result = "";
for (String p : parts) {
    result += p;            // BAD at scale — new String each time, O(n²)
}
```

**Java — fix when you have a collection:**

```java
String.join(", ", parts);
```

**Java — fix when you build in a loop:**

```java
StringBuilder sb = new StringBuilder();
for (String p : parts) {
    sb.append(p);
}
String result = sb.toString();   // materialize once
```

| Situation | Python | Java |
|-----------|--------|------|
| List of strings ready | `", ".join(parts)` | `String.join(", ", parts)` |
| Filtering / mapping in a loop | `list` + `join` | `StringBuilder.append` |
| Antipattern at scale | `s += piece` in loop | `s += piece` in loop |

> **Rule:** immutable strings → **collect pieces, join once** (Python) or **one `StringBuilder`** (Java). A handful of `+=` in a tiny loop is readable and fine; avoid the pattern for large `n` or hot paths.

**Examples:**

```python
", ".join(["Python", "Java", "Go"])   # Python, Java, Go
"".join(sorted("cba"))                # abc
```

```java
String.join(", ", List.of("Python", "Java", "Go"));
```

### `sorted(string)` returns a **list** — not a `str`

`sorted()` **always** returns a new `list`, never a string. On a `str`, each element is a **one-character string**:

```python
sorted("eat")           # ['a', 'e', 't']  — not "aet"
print(sorted("eat"))    # prints ['a', 'e', 't']
"".join(sorted("eat"))  # 'aet'            — join back to str
```

> **Java:** sorting characters gives you `char[]` or a collection — you still build `new String(chars)` or `String.join("", parts)`. Python splits the steps: `sorted()` → list, `"".join(...)` → string.

Common pattern (anagram key from Lesson 2 practice):

```python
"".join(sorted(word))
```

**Rule:** need a sorted **string** → `"".join(sorted(s))`. A bare `sorted(s)` is a **list** — fine if you keep processing it, wrong type for APIs that expect `str`.

---

## f-strings — default choice

**Java:**

```java
String name = "Alex";
int age = 30;
String msg = String.format("Hello, %s! You are %d.", name, age);
// Java 15+: "Hello, %s! You are %d.".formatted(name, age);
```

**Python:**

```python
name, age = "Alex", 30
print(f"Hello, {name}! You are {age}.")
print(f"Next year: {age + 1}")   # any expression inside {…}
```

Any expression works inside `{...}`.

### Format specifiers — `{value:spec}`

**Java** (`String.format` / `printf` flags):

```java
String.format("%.2f", 12.5);       // 12.50
String.format("%,d", 1_000_000);   // 1,000,000
String.format("%05d", 7);          // 00007

// Hex — watch digit count on 255 vs 15:
String.format("%#x", 255);         // 0xff   — minimal digits, lowercase
String.format("%#x", 15);          // 0xf    — no leading zero on the digit
String.format("0x%02X", 255);      // 0xFF   — always ≥2 hex digits (byte style)
String.format("0x%02X", 15);       // 0x0F   — pads with 0 when needed
String.format("0x%02X", 0);        // 0x00
```

**Python** (same ideas after the colon):

```python
print(f"{price:.2f}")      # 12.50
print(f"{1_000_000:,}")    # 1,000,000
print(f"{7:05d}")          # 00007

print(f"{255:#x}")         # 0xff
print(f"{15:#x}")          # 0xf
print(f"0x{255:02X}")      # 0xFF
print(f"0x{15:02X}")       # 0x0F
print(f"0x{0:02X}")        # 0x00
```

**Hex digit count — same value, different formats:**

| `n` | `%#x` / `{n:#x}` | `0x%02X` / `f"0x{n:02X}"` | Why |
|-----|------------------|---------------------------|-----|
| 255 | `0xff` | `0xFF` | 255 needs 2 hex digits either way |
| **15** | **`0xf`** | **`0x0F`** | `%#x` = minimal; `%02X` pads to 2 digits |
| 0 | `0x0` | `0x00` | same padding difference |

`#` adds the `0x` prefix but does **not** zero-pad the digits. For fixed-width bytes (`0x00`–`0xFF`), use **`0x%02X`** / **`f"0x{n:02X}"`** (practice `hex_byte`).

| Goal | Java | Python |
|------|------|--------|
| Lowercase, minimal digits + `0x` | `String.format("%#x", n)` | `f"{n:#x}"` |
| Uppercase byte `0x00`–`0xFF` | `String.format("0x%02X", n)` | `f"0x{n:02X}"` |
| Digits only, no prefix | `Integer.toHexString(n)` | `f"{n:x}"` / `hex(n)` |

### Width and alignment

**Java:**

```java
String.format("|%8s|", "id");    // |      id|  right-align (default for %s)
String.format("|%-8s|", "id");   // |id      |  left-align
// Center — no %^ flag in String.format; pad manually:
int w = 8, pad = w - "id".length(), left = pad / 2;
String centered = " ".repeat(left) + "id" + " ".repeat(pad - left);
// Or: org.apache.commons.lang3.StringUtils.center("id", 8);
```

**Python:**

```python
label = "id"
print(f"|{label:>8}|")    # right-align  — Java: %8s
print(f"|{label:<8}|")    # left-align   — Java: %-8s
print(f"|{label:^8}|")    # center       — Java: manual / StringUtils.center
print(f"|{'9':*>8}|")     # fill char *  — Java: no printf fill-char flag
```

### Debug suffix `{var=}` (3.8+)

```python
score = 42
print(f"{score=}")         # score=42
```

Variable name must be a literal in the expression — for dynamic labels, build the string manually.

### `str` vs `repr` — and `!s` `!r` `!a` in f-strings

Java has one conversion path in templates: `obj.toString()` / `String.valueOf(obj)`. Python splits **human** (`str`) vs **debug** (`repr`); f-strings expose both via `!s` / `!r` / `!a`.

Two ways to turn a value into text:

| Call | Audience | String `"hi"` prints as |
|------|----------|-------------------------|
| `str(x)` / `{x}` / `{x!s}` | human-readable | `hi` |
| `repr(x)` / `{x!r}` | developer / debug | `'hi'` (quotes included) |

```python
word = "hi"
f"{word}"      # hi      — str(word); default
f"{word!s}"    # hi      — same as default (!s changes nothing)
f"{word!r}"    # 'hi'    — repr(word); single quotes in output

items = ["a", "b"]
f"{items!r}"   # repr(whole list) → ['a', 'b']
```

`repr(x)` works on **any object** — it calls `x.__repr__()` (Lesson 8). For strings, `repr` shows escapes:

```python
s = "a\nb"
f"{s}"         # real newline in output
f"{s!r}"       # 'a\nb'  — backslash visible
```

| Flag | Calls | Notes |
|------|-------|-------|
| (none) / `!s` | `str()` | default |
| `!r` | `repr()` | quoted, escape-visible |
| `!a` | `ascii()` | non-ASCII escaped for logs |

---

## Escaping quotes and backslashes

**Quotes** — same `\"` as Java, plus alternate delimiters:

```python
"it's fine"
'it\'s fine'
"she said \"hi\""
```

**Backslashes** — two **equivalent** ways to get a literal `\` (raw is optional; `\\` is the standard escape):

```python
"C:\\new\\folder"    # standard — same as Java
r"C:\new\folder"     # raw shortcut — same resulting string
"C:\\new" == r"C:\new"   # True
```

| Need | Use |
|------|-----|
| Real `\n` newline, `\t` tab | normal `"a\nb"` |
| Windows path, regex (literal `\`) | `r"..."` **or** `"C:\\path"` |
| Path + f-string variable | `fr"C:\users\{name}\file.txt"` |

Use **normal** `"..."` when you want escape sequences. Use **`r"..."`** when you want backslashes to stay literal (`\n` is two characters, not a newline).

---

## Other formatting styles

**`str.format()`** — reusable template. Java's `String.format` is **positional only**; Python's `.format()` adds **named** placeholders (`{name}`), which Java lacks:

```java
String template = "Dear %s, balance $%.2f";
String.format(template, "Alice", 1234.5);
```

```python
"Dear {name}, balance ${balance:.2f}".format(name="Alice", balance=1234.5)
```

**Forwarding placeholders** — a function can take caller values and spread them into `.format()` with `**`:

```python
def format_template(template: str, **kwargs: object) -> str:
    return template.format(**kwargs)   # ** = unpack the dict back into keyword args

format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5)
# "Dear Ann, total=$9.50"
```

The `**` in the `def` *collects* keyword args into a dict; the `**` in `.format(**kwargs)` *unpacks* that dict back into keyword args — same punctuation, opposite directions. **Lesson 4 covers the full `*args` / `**kwargs` mechanics** (including the `format(kwargs)`-without-`**` mistake); here you just need that `.format(**kwargs)` forwards placeholders.

> **Java:** no `**kwargs` and no keyword unpack. Closest: build `Map<String, Object>` and pass fields explicitly. Java **varargs** (`int... args`) ≈ Python `*args` only (positional) — see **Lesson 4**.

**Legacy `%`** — still seen in older code (≈ `printf` / `String.format` with `%s`):

```java
String.format("%s scored %d", "Bob", 95);
```

```python
"%s scored %d" % ("Bob", 95)
```

> **Key idea:** New code uses **f-strings**. Know `.format()` and `%` for reading legacy code.

---

## Literal braces

Double braces escape `{` and `}` in f-strings (same idea as `{{` / `}}` in Java `String.format`):

```python
print(f"set literal: {{1, 2, 3}}")
```

---

## Objects in f-strings

**Java:** `"point=" + p` calls `p.toString()`.

**Python:** `f"{p}"` uses the str path (`__str__` / `__repr__` — see Lesson 8). `@dataclass` generates a repr like a Java `record` `toString()`.

```python
@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
f"point={p}"      # point=Point(x=3, y=4)
f"point={p!r}"    # explicit repr
```

---

## Case conversion

```python
"Hello".upper()       # HELLO         — toUpperCase()
"Hello".lower()       # hello         — toLowerCase()
"hello world".title() # Hello World
```

---

## Regular expressions — `re` module

When `in`, `split`, `replace`, and `startswith` are not enough, use the stdlib **`re`** module (≈ Java `java.util.regex`).

**Always use raw strings for patterns** — `r"\d+"` not `"\\d+"`:

```python
import re

text = "Order 42: ship 7-10 days"

m = re.search(r"\d+", text)    # first Match or None     — find()
m.group()                      # "42"                    — group()

re.findall(r"\d+", text)       # ['42', '7', '10']       — all matches
re.sub(r"\d+", "#", text)      # replaceAll
re.fullmatch(r"\d+", "42")     # Match (whole string)    — matches() -> boolean
re.match(r"\d+", "42 days")    # Match (at start)         — lookingAt() -> boolean
```

| Java | Python `re` |
|------|-------------|
| `Pattern.compile(p)` | `re.compile(p)` |
| `matcher.find()` | `re.search(p, s)` / `pattern.search(s)` |
| `matcher.matches()` | `re.fullmatch(p, s)` |
| `matcher.group()` | `match.group()` |
| `matcher.replaceAll(rep)` | `re.sub(p, rep, s)` |
| `String.split(p)` | `re.split(p, s)` |

Compile once when you reuse the same pattern:

```python
digits = re.compile(r"\d+")
digits.findall("a1 b22")   # ['1', '22']
```

> **Rule:** try plain string methods first; regex when the pattern is real pattern matching (digits, emails, log parsing). This lesson introduces `re` — not a full regex tutorial.

---

## Pause and practice

```bash
uv run python lesson_03/practice/01_strings.py
uv run python lesson_03/practice/02_string_ops.py
```

OOP string methods (`__str__`, `__repr__`, `__format__`) come in **Lesson 8**.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_03/01_strings.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_03/01_strings.py)
- **Practice (formatting):** [lesson_03/practice/01_strings.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_03/practice/01_strings.py)
- **Practice (operations):** [lesson_03/practice/02_string_ops.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_03/practice/02_string_ops.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
