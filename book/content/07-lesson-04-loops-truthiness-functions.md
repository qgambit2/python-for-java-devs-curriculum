# Lesson 4 — Loops, truthiness, and functions

Builds on **Lesson 1 control flow** (`lesson_01/03_control_flow.py`). Here: truthiness in `if`, `is` vs `==`, and `def` functions.

Three things in this lesson behave unlike their Java counterparts, and each is a silent-bug source rather than a compile error. Python's `if` accepts *any* object and decides truth by emptiness, so `if items:` replaces `if (!list.isEmpty())` — but `if count:` quietly treats `0` as false. `==` compares values while `is` compares identity, and confusing them passes tests until it suddenly doesn't. And `def` has no overloading and evaluates default arguments **once** at definition time — the classic mutable-default trap. Knowing these up front saves you the debugging session each one otherwise costs.

**Run:**

```bash
uv run python lesson_04/01_loops.py
uv run python lesson_04/02_truthiness.py
uv run python lesson_04/03_functions.py
```

---

## for and while

```python
for fruit in fruits:
    print(fruit)

for key, value in scores.items():   # need both? use .items()
    print(key, value)

for i in range(3):                  # 0, 1, 2 — stop exclusive
    print(fruits[i])
```

`range(start, stop, step)` matches slice semantics — **stop is exclusive**.

`break` and `continue` work like Java.

### for-else — no Java equivalent

```python
for fruit in fruits:
    if fruit == target:
        print("found")
        break
else:
    print("not found")    # runs only if loop did NOT break
```

> **Java:** simulate with a `found` flag.

---

## Truthiness — empty means false

These are **falsy:** `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`. Everything else is truthy.

```python
if name:           # False for ""
    ...
if scores:       # False for []
    ...
```

> **Key idea:** Empty collections and empty strings are **falsy**, so `if items:` means "if non-empty." In Java you'd write `if (!items.isEmpty())`; in Python the bare object is enough — and never test `if items == True`.

### `is` vs `==`

- `==` compares **values**
- `is` compares **identity** (same object in memory)

```python
x is None          # correct None check
x == None          # works but avoid — style guides prefer `is None`
```

Never use `is` for string or int content checks — only for singletons like `None`.

> **Java:** `==` on objects is identity; `.equals()` is value. Python splits this explicitly.

---

## Functions

```python
def greet(person: str, times: int = 1) -> str:
    return (f"Hi, {person}! ") * times

greet("Java dev")
greet("Java dev", times=3)
```

- No overloading — one `def` per name; use default args
- Type hints are optional at runtime
- Keyword args at call site: `times=3`

> **Java:** No method overloading. Java picks an overload by signature at compile time; Python has **one** `def` per name and leans on default values and keyword args instead.

### `*args` and `**kwargs` — same symbols, opposite jobs

Python reuses `*` and `**` in two places. **Direction** tells you which job:

| Location | `*…` | `**…` |
|----------|------|-------|
| **In `def`** (parameter list) | **Collect** extra positional args → `tuple` | **Collect** extra keyword args → `dict` |
| **In a call** (argument list) | **Unpack** a sequence into positional args | **Unpack** a dict into keyword args |

```text
def f(**kwargs):     ← COLLECT at the door
    g(**kwargs)      ← UNPACK when forwarding

Caller keyword args  →  dict  →  callee keyword args
```

**Rule:** `def` = pack extras in; call = spread them out. Same punctuation, opposite flow.

#### Java varargs (positional only)

Java **`int... values`** collects **extra positional** arguments into an **array** — always the **last** parameter, no keyword bucket:

```java
static int sum(int first, int... rest) {
    int total = first;
    for (int v : rest) total += v;
    return total;
}
sum(1, 2, 3, 4);   // rest is int[] {2, 3, 4}
```

| Python in `def` | Becomes inside function | Java parallel |
|-----------------|-------------------------|---------------|
| `*args` | `tuple` of extra positionals | `int... values` |
| `**kwargs` | `dict` of extra keywords | **no equivalent** — `Map<String, Object>` by hand |

```python
def demo(a, *args, **kwargs):
    print(a, args, kwargs)

demo(1, 2, 3, name="Ann", total=9.5)
# 1 (2, 3) {'name': 'Ann', 'total': 9.5}
```

#### Unpacking at a call site (Lesson 3 `format_template`)

```python
def format_template(template: str, **kwargs) -> str:
    #        COLLECT ↑ in def          UNPACK ↑ in call
    return template.format(**kwargs)

format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5)
```

Inside the function, `kwargs` is `{"name": "Ann", "total": 9.5}`.  
`template.format(**kwargs)` is **required** — not `template.format(kwargs)`:

```python
template.format(**kwargs)   # ✓ .format(name="Ann", total=9.5)
template.format(kwargs)     # ✗ one positional arg; {name} / {total} break
```

Positional unpack works the same way:

```python
values = (10, 20)
"{} + {}".format(*values)   # ✓ same as .format(10, 20)
"{} + {}".format(values)    # ✗ prints "(10, 20)" as one value, not two fields
```

| You want | Write |
|----------|-------|
| Collect extras in `def` | `def f(a, *args, **kwargs):` |
| Spread sequence at call | `f(*[1, 2, 3])` |
| Spread dict at call | `g(**{"x": 1})` or `template.format(**kwargs)` |

> **Java:** varargs ≈ `*args` collect only. No `**kwargs`, no `f(*list)` spread at call — pass elements explicitly or loop.

### Do not mutate caller's collections

```python
def merge_scores(left, right):
    result = right.copy()    # new dict
    for name, score in left.items():
        result[name] = result.get(name, 0) + score
    return result
```

Mutating `right` in place surprises callers — same as modifying a passed-in `HashMap`.

### Mutable default args — classic gotcha

```python
def add_item(item, bucket=None):   # NOT bucket=[]
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Default `[]` is created **once** at function definition time and shared across calls.

> **Key idea:** Copy before mutate; `None` for optional mutable defaults.

---

## Pause and practice

```bash
uv run python lesson_04/01_loops.py
uv run python lesson_04/02_truthiness.py
uv run python lesson_04/03_functions.py
```

Run each demo, then edit it to make a change stick: rewrite an indexed loop with `enumerate`, swap an `== None` for `is None`, and convert a function with a mutable default argument to the `None` idiom — confirm the output shifts the way you expect.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_04/01_loops.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/01_loops.py)
- **Example:** [lesson_04/02_truthiness.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/02_truthiness.py)
- **Example:** [lesson_04/03_functions.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_04/03_functions.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
