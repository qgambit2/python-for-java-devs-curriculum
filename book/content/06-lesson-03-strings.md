# Lesson 3 — Strings and formatting

Java leans on `String.format`, `MessageFormat`, and concatenation. Python's default is **f-strings** — expressions inside `{...}` in a string literal prefixed with `f`.

**Run:**

```bash
uv run python lesson_03/01_strings.py
```

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

---

## Raw strings and combined prefixes

Backslashes are literal in raw strings — paths and regex:

```python
print(r"C:\new\folder")
print(fr"C:\users\{name}\file.txt")   # raw + formatted
```

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

## Pause and practice

```bash
uv run python lesson_03/practice/01_strings.py
```

OOP string hooks (`__str__`, `__repr__`, `__format__`) come in **Lesson 8**.
