# Lesson 1 — Control flow (Java if / for / while / switch)

**Read early** — right after syntax and variables, before collections.

```bash
uv run python lesson_01/03_control_flow.py
uv run python lesson_01/practice/02_control_flow.py
```

Lesson 4 (`lesson_04/`) adds **truthiness**, `is` vs `==`, and **functions** on top of this.

---

## Java ↔ Python map

| Java | Python |
|------|--------|
| `if (x > 0) { }` | `if x > 0:` |
| `else if` | `elif` |
| `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| `for (T x : list)` | `for x in list:` ← **default** |
| `while (cond)` | `while cond:` |
| `do { } while (cond);` | no direct form — see below |
| `switch (x) { case A: }` | `match x: case A:` (3.10+) |
| `break` / `continue` | same keywords |

Blocks use **indentation**, not `{ }`.

---

## if / elif / else

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

Parentheses around the condition are optional. Combine with `and`, `or`, `not` (Java `&&`, `||`, `!`).

---

## for loops

**Iterate values** (Java enhanced `for`):

```python
for fruit in fruits:
    print(fruit)
```

**Index loop** when you need `i`:

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

`range(stop)` → `0 .. stop-1` (stop **exclusive**, like Java `i < n`).

| Python | Java |
|--------|------|
| `range(5)` | `for (int i = 0; i < 5; i++)` or `IntStream.range(0, 5)` |
| `range(2, 5)` | `for (int i = 2; i < 5; i++)` or `IntStream.range(2, 5)` |
| `range(0, 10, 2)` | `for (int i = 0; i < 10; i += 2)` |
| `range(1, 6)` (1..5) | `IntStream.rangeClosed(1, 5)` — **inclusive** end in Java |

`IntStream.range` (Java 8+) is the closest named “range” — end **exclusive**, lazy until you `.toArray()` / `collect`. Python `range` is also lazy; `list(range(...))` materializes.

```python
range(5)        # 0,1,2,3,4
range(2, 5)     # 2,3,4
range(0, 10, 2) # 0,2,4,6,8
```

---

## while

```python
while n > 0:
    print(n)
    n -= 1
```

Same idea as Java `while`.

---

## do/while — no direct equivalent

Java `do/while` always runs the body once. Python patterns:

```python
# while True + break
while True:
    body()
    if done:
        break

# or: first value before loop
data = read()
while data is not None:
    process(data)
    data = read()
```

---

## switch → match (Python 3.10+)

**Yes — Python has a direct equivalent:** `match` / `case` (requires Python 3.10+; this curriculum uses 3.12).

**Java (modern switch, no fall-through with `->`):**

```java
switch (status) {
    case 200 -> label = "ok";
    case 404 -> label = "missing";
    case 500, 502, 503 -> label = "server error";
    default -> label = "other";
}
```

**Python:**

```python
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
```

| Java switch | Python `match` |
|-------------|----------------|
| `case 200:` / `case 200 ->` | `case 200:` |
| `case 500, 502, 503` | `case 500 \| 502 \| 503` |
| `default` | `case _:` |
| fall-through with `:` (old style) | **no fall-through** — one case runs, then done |
| `break` after each case (old style) | not needed |
| switch on `String` | `match` on `str` works the same way |
| guarded patterns (Java 21+) | `case x if x > 0:` |

**`match` is a statement** (not a switch *expression* like Java's `switch (x) { case 1 -> "a"; }` as a value). Assign inside each `case`, or use `if/elif` / a dict when you need a value inline:

```python
def label_for(code: int) -> str:
    match code:
        case 200:
            return "ok"
        case 404:
            return "missing"
        case _:
            return "other"
```

**Guard on a case:**

```python
match n:
    case 0:
        "zero"
    case x if x > 0:
        "positive"
    case _:
        "negative"
```

### Alternatives (when `match` is overkill)

**`if` / `elif` chain** — always works:

```python
if code == 200:
    label = "ok"
elif code == 404:
    label = "missing"
else:
    label = "other"
```

**Dict dispatch** — compact for simple mappings:

```python
HTTP = {200: "ok", 404: "missing"}
label = HTTP.get(code, "other")
```

> **Rule:** use **`match`** for real multi-way branching (especially strings and enums); use **`if/elif`** or a **dict** for two–three simple cases.

---

## break, continue, for-else

`break` and `continue` work like Java.

**for-else** — no Java equivalent:

```python
for fruit in fruits:
    if fruit == target:
        break
else:
    print("not found")   # runs only if loop did NOT break
```

> **Java:** use a `boolean found` flag.

---

## On GitHub

- **Example:** [lesson_01/03_control_flow.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_01/03_control_flow.py)
- **Practice:** [lesson_01/practice/02_control_flow.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_01/practice/02_control_flow.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
