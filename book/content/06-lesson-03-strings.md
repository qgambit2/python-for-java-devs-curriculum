# Lesson 3 — Strings: operations and formatting

Python `str` is a **sequence** of characters — indexing and slicing work like lists (see Lesson 2). For **building** and **printing** text, Python defaults to **f-strings** instead of Java's `String.format` / `printf`.

**Run:**

```bash
uv run python lesson_03/01_strings.py
```

---

## Indexing, length, membership

```python
text = "Python"
text[0]          # 'P'     — Java: charAt(0)
text[-1]         # 'n'
text[1:4]        # 'yth'   — Java: substring(1, 4)
len(text)        # 6       — Java: length()  (function, not a method)
"world" in s     # True    — Java: contains("world")
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
"  one   two  ".split()         # ['one', 'two', 'three']  — whitespace runs collapsed
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

Prefer **`join`** over `+=` in loops — each `+=` can allocate a new string.

```python
", ".join(["Python", "Java", "Go"])   # Python, Java, Go
"".join(sorted("cba"))                # abc
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

```python
name, age = "Alex", 30
print(f"Hello, {name}! You are {age}.")
print(f"Next year: {age + 1}")
```

Any expression works inside `{...}`.

### Format specifiers — `{value:spec}`

```python
price = 12.5
print(f"{price:.2f}")      # 12.50
print(f"{1_000_000:,}")    # 1,000,000
print(f"{255:#x}")         # 0xff
print(f"{7:05d}")          # 00007
```

> **Java:** `%.2f`, `%,d`, `%#x` in `String.format`.

### Width and alignment

```python
label = "id"
print(f"|{label:>8}|")    # right-align
print(f"|{label:<8}|")    # left-align
print(f"|{label:^8}|")    # center
```

### Debug suffix `{var=}` (3.8+)

```python
score = 42
print(f"{score=}")         # score=42
```

Variable name must be a literal in the expression — for dynamic labels, build the string manually.

### `str` vs `repr` — and `!s` `!r` `!a` in f-strings

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

**`str.format()`** — reusable template:

```python
"Dear {name}, balance ${balance:.2f}".format(name="Alice", balance=1234.5)
```

**Legacy `%`** — still seen in older code:

```python
"%s scored %d" % ("Bob", 95)
```

> **Key idea:** New code uses **f-strings**. Know `.format()` and `%` for reading legacy code.

---

## Literal braces

Double braces escape `{` and `}` in f-strings:

```python
print(f"set literal: {{1, 2, 3}}")
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

re.search(r"\d+", text)        # first Match or None     — find()
m.group()                      # "42"                    — group()

re.findall(r"\d+", text)       # ['42', '7', '10']       — all matches
re.sub(r"\d+", "#", text)      # replaceAll
re.fullmatch(r"\d+", "42")     # True — whole string      — matches()
re.match(r"\d+", "42 days")    # True — at start          — lookingAt()
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
