# Java ↔ Python Equivalents

Reference for teaching. Expand as curriculum grows.

## Syntax

| Java | Python |
|------|--------|
| `{ }` blocks | indentation (4 spaces) |
| `;` end statements | optional |
| `else if` | `elif` |
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `for (String s : list)` | `for s in list:` |
| `while (cond)` | `while cond:` |
| `i++` / `i--` | `i += 1` / `i -= 1` |
| `//` comment | `#` comment |
| `/* */` | `"""` multiline or `#` per line |
| `System.out.println(x)` — one expression | `print(a, b, c)` — any count; `sep`, `end` |
| `System.out.print(x)` — no newline | `print(x, end="")` |

Lesson: `lesson_01/01_syntax.py`

## Types & literals

| Java | Python |
|------|--------|
| `int x = 5` | `x = 5` |
| `String s = "hi"` | `s = "hi"` |
| `null` | `None` |
| `true` / `false` | `True` / `False` |
| `instanceof` | `isinstance(x, int)` |
| `Integer.parseInt("42")` | `int("42")` |
| `String.valueOf(42)` | `str(42)` |
| `byte[]` | `bytes` |
| `char` / `Character` | one-character `str` |
| `List`, `Map` interfaces | `list`, `dict` concrete types (no separate interfaces in daily use) |

Lesson: `lesson_06/01_types_and_datatypes.py`

## Loops & control flow

| Java | Python |
|------|--------|
| `if (cond) { }` | `if cond:` |
| `else if` | `elif` |
| `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| `IntStream.range(0, n)` (Java 8+) | `range(n)` — end exclusive, lazy |
| `IntStream.rangeClosed(a, b)` | `range(a, b + 1)` — Java end is **inclusive** |
| `for (int i = 0; i < 10; i += 2)` | `range(0, 10, 2)` |
| `for (String s : list)` | `for s in list:` |
| `while (cond)` | `while cond:` |
| `do { } while (cond);` | `while True:` + `break`, or body once then `while` |
| `switch (x) { case A: }` | `match x: case A:` (3.10+); `_` = default |
| `case 500, 502` (Java) | `case 500 | 502 | 503:` |
| switch expression | assign inside `case` blocks, or use `if/elif` / dict |
| guarded case (Java 21+) | `case x if x > 0:` |
| simple switch | `if/elif` or `{code: label}.get(x, default)` |
| `break` / `continue` | `break` / `continue` |
| labeled break | no labels — refactor or flag |
| `for (...) { } else` (rare) | `for ... else:` — runs if no `break` |

Lesson: `lesson_01/03_control_flow.py` §6 · reinforcement: `lesson_04/01_loops.py`

## Math & numbers

| Java | Python |
|------|--------|
| `Math.sqrt(x)` | `math.sqrt(x)` |
| `Math.pow(a, b)` | `a ** b` |
| `7 / 2` (ints → int) | `7 // 2` → `3`; `7 / 2` → `3.5` |
| `7 % 2` | `7 % 2` |
| `Math.abs` | `abs(x)` |
| `BigDecimal` | `decimal.Decimal` |
| `new Random()` | `import random` |

Lesson: `lesson_06/02_math_and_numbers.py`

## Dates & time (`java.time`)

| Java | Python |
|------|--------|
| `LocalDate.now()` | `date.today()` |
| `LocalDate.of(y, m, d)` | `date(y, m, d)` |
| `LocalDateTime.now()` | `datetime.now()` |
| `date.plusDays(n)` | `date + timedelta(days=n)` |
| `ChronoUnit.DAYS.between(a, b)` | `(b - a).days` |
| `DateTimeFormatter` | `strftime` / `strptime` |
| `ZonedDateTime` + `ZoneId` | `datetime` + `zoneinfo.ZoneInfo` |

Lesson: `lesson_06/03_datetime.py`

## Recursion

| Java | Python |
|------|--------|
| `StackOverflowError` | `RecursionError` |
| no TCO on JVM either (usually) | **no TCO** in CPython — assume stack grows |
| iterative alternative | `for`/`while` or explicit stack |

Lesson: `lesson_06/04_recursion.py`

## Mutate in place vs return new (read this first)

| Mutates original | Returns new object |
|------------------|-------------------|
| `list.append(x)` | `list + other` |
| `list.extend(other)` | `sorted(list)` |
| `list.sort()` → `None` | slicing `list[:]` |
| `list.reverse()` → `None` | `[expr for x in list]` |
| `dict[k] = v` | `dict(zip(keys, vals))` |
| `new HashMap<>(defaults); putAll(user)` | `{**defaults, **user}` — new dict; right overwrites left |
| shallow copy of map | `{**d}` · `d.copy()` · `dict(d)` |
| `lambda d: {**d}` | anonymous shallow-copy function |
| overlay only known keys | `{**defaults, **{k: user[k] for k in user if k in defaults}}` |
| `set.add(x)` | `{x for x in xs}` |

**Rule:** if assignment looks like `x = x.method()`, check whether `method()` returns `None` (`sort`, `reverse`, `extend`, `append`).

## Collections

| Java | Python |
|------|--------|
| `ArrayList<T>` | `list` |
| `HashMap<K,V>` | `dict` (hash lookup; also keeps insertion order since 3.7) |
| `LinkedHashMap<K,V>` | `dict` — iteration order = insertion order; reassigning a key does not move it |
| `HashSet<T>` | `set` |
| `Sets.union(a, b)` / `addAll` | `a \| b` (set union) |
| `retainAll` | `a & b` (intersection) |
| `removeAll` on copy | `a - b` (difference — left minus right) |
| `Sets.symmetricDifference(a, b)` | `a ^ b` (symmetric difference) |
| `(union) - (intersection)` | `a ^ b` — identity: `(a \| b) - (a & b) == a ^ b` |
| list concat (not set union) | `[1,2] + [2,3]` — use `\|` only on sets |
| `d.keySet()` union both maps | `left.keys() \| right.keys()` (3.9+) |
| shallow copy of map | `d.copy()` or `dict(d)` or `{**d}` |
| merge maps (sum values, new dict) | `{k: a.get(k,0)+b.get(k,0) for k in a.keys()\|b.keys()}` |
| `TreeMap` | no stdlib — `sorted(d.items())` |
| `ConcurrentHashMap` | no stdlib — `Lock` + `dict` |
| `Map.entry(k,v)` / Guava `Pair` | tuple `(k, v)` |
| `list.add(x)` | `list.append(x)` |
| `list.addAll(other)` | `list.extend(other)` (mutates) |
| concat two lists (new list) | `a + b` (neither mutated) |
| `stream().flatMap(List::stream)` | `[x for sub in nested for x in sub]` |
| lazy Stream pipeline | `(x for x in xs if p(x))` generator — consume once |
| `.parallelStream()` | no stdlib — `multiprocessing` / `ProcessPoolExecutor` |
| `Stream.reduce` | `functools.reduce` (rarely idiomatic) |
| method reference `Foo::bar` | `lambda x: x.bar` or `operator.attrgetter("bar")` |
| `Function<T,R>` / lambda value | function object — `def` or `lambda`, first-class |
| `Iterator` + manual `hasNext` | `yield` generator functions (Lesson 1 §17 — planned) |
| partial application | `functools.partial` |
| `sum` of list concat trick | `sum(nested, [])` — fold with `+`, needs `start=[]` |
| `list.size()` | `len(list)` |
| `list.indexOf(x)` | `lst.index(x)` — missing → **`ValueError`** (not `-1`) |
| `list.indexOf(x, fromIndex)` | `lst.index(x, start)` |
| `list.lastIndexOf(x)` | no built-in — `len(lst) - 1 - lst[::-1].index(x)` |
| test element in list | `x in lst` — like `indexOf != -1` |
| `map.get(k)` | `d.get(k)` → `None` if missing |
| `map.get(k)` on missing (no default) | `d[k]` → **`KeyError`** — stricter than Java `null` |
| `map.getOrDefault(k, d)` | `d.get(k, d)` |
| `computeIfAbsent(k, k -> new ArrayList<>())` | `d.setdefault(k, []).append(x)` |
| `getOrDefault(k, emptyList())` read-only | `d.get(k, [])` — don't `.append` on result |
| transform all map values | `{k: f(v) for k, v in d.items()}` — needs `.items()` |
| `map.put(k, v)` | `d[k] = v` |
| `map.containsKey(k)` | `k in d` |
| `map.remove(k)` | `del d[k]` or `d.pop(k)` — **no** `dict.remove()` |
| `map.remove(k)` return value | `d.pop(k)` returns value; `del d[k]` returns nothing |
| `dict.popitem()` | LIFO pair — last inserted; no `last=` kwarg on plain `dict` |
| evict oldest plain dict entry | `k = next(iter(d)); del d[k]` |
| `OrderedDict.popitem(last=False)` | FIFO eldest — access-order LRU → `lesson_08/09_ordered_dict_lru.py` |
| `list.removeLast()` / `removeFirst()` | `lst.pop()` / `lst.pop(0)` |
| `list.remove(Object)` | `lst.remove(value)` — `ValueError` if missing |
| `computeIfAbsent(k, k -> new ArrayList<>())` | `defaultdict(list)` then `d[k].append(x)` |
| `Collections.frequency` / Multiset | `Counter(iterable)` — `+` `-` `&` `\|` on counts |
| `ArrayDeque` | `collections.deque` — `appendleft`, `popleft`, `rotate`, `maxlen` |
| `list.removeFirst()` on `ArrayDeque` | `deque.popleft()` — **not** `list.pop(0)` (O(n)) |
| `LinkedHashMap(accessOrder=true)` | `OrderedDict.move_to_end` or plain `dict` pop+reinsert |
| Java `record` / `Pair` (immutable) | `namedtuple("Name", ["x", "y"])` — `_replace`, `_asdict` |
| stacked config / override chain | `ChainMap(child, parent, defaults)` |
| subclass `AbstractMap` safely | `UserDict` / `UserList` — override hooks, `.data` inside |
| `map.keySet()` | `d.keys()` |
| `map.values()` | `d.values()` |
| `map.entrySet()` | `d.items()` |
| `for (K k : map.keySet())` | `for k in d` |
| flip / invert map | `{v: k for k, v in d.items()}` — duplicate values: last wins |
| `Collections.sort(list)` | `sorted(list)` or `list.sort()` |
| `list.subList(0, n)` | `list[:n]` |
| `list.subList(k, list.size())` | `list[k:]` |
| `new ArrayList<>(list)` | `list[:]` · `list.copy()` · `list(list)` |
| `new HashMap<>(map)` | `{**d}` · `d.copy()` · `dict(d)` — **not** `d[:]` |
| `list.get(list.size() - 1)` | `list[-1]` (element, not list) |
| `list.subList(size-2, size)` | `list[-2:]` |
| `list.subList(0, size-1)` | `list[:-1]` |
| negative index `k` | real index = `len(list) + k` |

## Tuples (values & type hints)

| Java | Python |
|------|--------|
| `Map.entry(k, v)` / Guava `Pair` | `(k, v)` tuple |
| `(42)` grouping | `int` — **not** a tuple |
| **1-tuple** | `(42,)` or `42,` — **trailing comma required** |
| empty tuple | `()` — len 0 |
| 2-tuple | `(1, 2)` — comma between values |
| 1-tuple from iterable | `tuple([42])` — when you have a list |
| `return 42` vs `return 42,` | `int` vs `tuple (42,)` |
| unpack 1-tuple | `x, = (42,)` — one target; fails if `len > 1` |
| starred unpack (rest) | `first, *rest = seq` — `rest` is always a `list` |
| ignore rest | `first, *_ = seq` — `*` + throwaway `_` |
| first + last only | `*_, last = seq` or `a, *_, z = t` |
| middle slice | `a, *mid, z = (1, 2, 3, 4)` → `mid=[2, 3]` |
| `arr[i]` / `list.get(i)` | `t[i]` — zero-based; `t[1]` = **second** value |
| `int[2]` fixed array | `tuple[int, int]` value `(x, y)` |
| `List<Integer>` variable | `tuple[int, ...]` |
| Scala `Tuple22` max (stdlib) | **no arity cap** — runtime or hints |
| multi-return via holder class | `return a, b` → one `tuple` |
| unpack Pair / array into locals | `x, y = pair` · `low, high = min_max(xs)` |
| `for (var e : map.entrySet())` body | `for k, v in d.items():` — unpack each entry |
| ignore one field | `name, _, email = person` — `_` is throwaway name |
| immutable list | `tuple` (not `frozenlist`) |

### Fixed-length vs variable-length type hints

```python
pair: tuple[int, int] = (1, 2)
triple: tuple[int, int, int] = (1, 2, 3)
mixed: tuple[str, int, bool] = ("Alice", 30, True)
many: tuple[int, ...] = (1, 2, 3, 4, 5)   # any count, homogeneous
```

| Annotation | Arity | Positions |
|------------|-------|-----------|
| `tuple[int, int]` | exactly 2 | both `int` |
| `tuple[int, int, int]` | exactly 3 | RGB, x/y/z |
| `tuple[str, int]` | exactly 2 | different types per slot |
| `tuple[int, ...]` | 0+ | all `int` |

**No Scala Tuple22-style limit** in Python stdlib. For many named fields, use `@dataclass` instead of a 10+ element tuple.

**Runtime:** hints are not enforced — `coords: tuple[int, int] = (1, 2, 3)` runs fine. Use `__post_init__` or explicit checks if length matters.

### Unpacking (destructuring)

```python
person = ("Alice", 30, "alice@example.com")
person[1]                            # 30 — one slot by index (second = index 1)
x, y = (3, 4)                        # unpack whole tuple
name, age, email = person
_, age, _ = person                   # second slot only — ignore others
low, high = min_max([3, 1, 4])       # function return
for k, v in d.items(): ...           # loop entry pairs
first, *rest = [1, 2, 3, 4]          # *rest → [2, 3, 4] (list)
first, *_ = (42, 33, 5)              # first=42; ignore rest
*_, last = (42, 33, 5)               # last=5
a, *mid, z = (1, 2, 3, 4)            # mid=[2, 3]
```

**`x, = (42,)`** requires exactly one value; **`x, = (42, 33, 5)`** → `ValueError`. Use `first, *rest = ...` for longer sequences.

Left-hand **count must match** unless `*` soaks the rest. FAQ: § Tuple unpacking · § Starred unpack · § one-element tuple.

### One-element tuple (1-tuple)

```python
type((42))        # int — NOT a tuple
type((42,))       # tuple, len 1
type(42,)          # tuple, len 1 — comma outside () works too

x, = (42,)         # unpack → x is int
return 42,         # return 1-tuple, not int
tuple([42])        # build 1-tuple from list
```

**Rule:** parentheses group; **commas** build tuples. `(42)` = int; `(42,)` = 1-tuple.

Lesson: `lesson_02/01_collections.py` · FAQ: § `(42)` vs `(42,)`

## Strings

Lesson: `lesson_03/01_strings.py` · Practice: `lesson_03/practice/01_strings.py` · FAQ: § String formatting

### Repeat & build

| Java | Python | Example output |
|------|--------|----------------|
| `"=".repeat(60)` (Java 11+) | `"=" * 60` | `============================================================` |
| `"ab".repeat(3)` | `"ab" * 3` | `ababab` |
| `"a" + "b"` | `"a" + "b"` | `ab` |
| `String.join(", ", parts)` | `", ".join(parts)` | `a, b, c` |

### Formatting map (with example output)

| Java | Python | Input | Output |
|------|--------|-------|--------|
| `String.format("%s %d", "Alex", 30)` | `f"{name} {age}"` | name=`Alex`, age=`30` | `Alex 30` |
| `String.format("%.2f", 12.5)` | `f"{x:.2f}"` | `12.5` | `12.50` |
| `String.format("%d", 42)` | `f"{n:d}"` | `42` | `42` |
| `String.format("%,d", 1_000_000)` | `f"{n:,}"` | `1000000` | `1,000,000` |
| `String.format("%#x", 255)` | `f"{n:#x}"` | `255` | `0xff` |
| `String.format("%#x", 15)` | `f"{n:#x}"` | `15` | `0xf` |
| `String.format("0x%02X", 255)` | `f"0x{n:02X}"` | `255` | `0xFF` |
| `String.format("0x%02X", 15)` | `f"0x{n:02X}"` | `15` | `0x0F` |
| `String.format("0x%02X", 0)` | `f"0x{n:02X}"` | `0` | `0x00` |
| `Integer.toHexString(255)` | `f"{n:x}"` / `hex(n)` | `255` | `ff` |
| `String.format("%8s", "id")` | `f"{s:>8}"` | `"id"` | `      id` |
| `String.format("%-8s", "id")` | `f"{s:<8}"` | `"id"` | `id      ` |
| manual pad / `StringUtils.center("id", 8)` | `f"{s:^8}"` | `"id"` | `   id   ` |
| `String.format("%05d", 7)` | `f"{n:05d}"` | `7` | `00007` |
| `template.formatted(...)` (Java 15+) | `template.format(name="Alice", b=99.5)` | — | `Dear Alice, $99.50` |
| `"%s scored %d" % (name, score)` | same | Bob, 95 | `Bob scored 95` |

### f-string prefixes & `{…}` options

| Feature | Example | Output |
|---------|---------|--------|
| `f` prefix | `f"{2+2}"` | `4` |
| `r` raw | `r"\n"` | `\n` (two chars) |
| `fr` combined | `fr"C:\{x}"` | path + value, backslashes kept |
| `{var=}` debug | `score=42` → `f"{score=}"` | `score=42` (literal var name only) |
| `{v!r}` repr | `f"{'hi'!r}"` | `'hi'` |
| `{{` literal | `f"{{x}}"` | `{x}` |

### Escaping — mostly same; backslashes: two Python ways

Python **can** escape backslashes like Java (`\\`) **or** use raw strings (`r"..."`) — both valid, same output for paths.

| Goal | Java | Python way 1 (escaped, like Java) | Python way 2 (raw shortcut) | Output |
|------|------|-----------------------------------|-----------------------------|--------|
| Path | `"C:\\new"` | `"C:\\new"` | `r"C:\new"` | `C:\new` |
| Quote in string | `"say \"hi\""` | `"say \"hi\""` or `'say "hi"'` | — | `say "hi"` |
| Newline | `"a\nb"` | `"a\nb"` | `r"a\nb"` gives literal `\n`, not newline | line break |
| Literal `\n` chars | `"\\n"` | `"\\n"` | `r"\n"` | `\n` |
| Unicode 16-bit | `\u0041` | `\u0041` | — | `A` |
| Multiline | `"""..."""` (Java 15+) | `"""..."""` | — | multiple lines |
| 32-bit Unicode | surrogate pairs | `\U0001F600` | — | 😀 |

| Java | Python |
|------|--------|
| `String.valueOf(n)` in concat | `f"{n}"` — auto `str()` |
| `"a".equals("b")` | `a == b` |
| `s.length()` | `len(s)` |
| `s.substring(1, 4)` | `s[1:4]` |
| `s.contains("x")` | `"x" in s` |
| `s.startsWith("pre")` | `s.startswith("pre")` |
| `s.endsWith(".csv")` | `s.endswith(".csv")` |
| `s.indexOf("x")` | `s.find("x")` — `-1` if missing; `s.index("x")` raises |
| `s.trim()` | `s.strip()` — also `lstrip` / `rstrip` |
| `s.split(",")` | `s.split(",")` — returns `list[str]` |
| `s.replace("a", "b")` | `s.replace("a", "b")` — all occurrences |
| loop `indexOf` for count | `s.count("x")` — non-overlapping |
| `s.toUpperCase()` | `s.upper()` |
| `s.toLowerCase()` | `s.lower()` |
| `Pattern.compile(p)` / `Matcher` | `re.compile(p)` / `re.search`, `re.findall`, `re.sub` |
| `matcher.matches()` | `re.fullmatch(p, s)` |
| `matcher.replaceAll(rep)` | `re.sub(p, rep, s)` |
| sort chars of string | `sorted(s)` → list; `"".join(sorted(s))` → str |
| anagram signature key | `"".join(sorted(word))` |

**Default choice:** f-strings. Use `!r` for debug output; `f"{var=}"` when the variable name in source is the label you want.

### Lesson 8 — formatting with classes

| Java | Python | Example output |
|------|--------|----------------|
| `toString()` used in concat | `f"{obj}"` → `__str__` | `(3, 4)` |
| debugger string in template | `f"{obj!r}"` → `__repr__` | `Point(x=3, y=4)` |
| `String.format` in method | `return f"{self.name}: ${self.balance:.2f}"` | `Alice: $1234.50` |
| (no direct equivalent) | `__format__(self, spec)` for `f"{m:.2f}"` | custom per-type formatting |

Lesson: `lesson_08/03_str_repr_and_formatting.py` · Practice: `lesson_08/practice/03_string_formatting.py` · Basics: `lesson_03/01_strings.py`

## Methods & functions

| Java | Python |
|------|--------|
| `public static void f()` | `def f():` |
| `public int f()` | `def f() -> int:` |
| `void` no return | `pass` or omit return |
| method overloading | defaults: `def f(a, b=1):` |
| `int... values` (varargs, positional) | `def f(a, *args):` → `args` is `tuple` |
| no varargs for keyword names | `def f(**kwargs):` → `kwargs` is `dict` |
| `sum(1, 2, 3)` spread at call | `f(*[1, 2, 3])` unpacks sequence into positional args |
| pass `Map` to custom helper | `g(**{"name": "Ann"})` unpacks dict into keyword args |
| `this.field` | `self.field` |
| `return a, b` (not idiomatic) | `return a, b` → tuple |

## OOP (Lesson 8)

| Java | Python |
|------|--------|
| `class Foo { }` | `class Foo:` |
| `new Foo()` | `Foo()` |
| constructor `Foo()` | `def __init__(self, ...):` |
| `@PostConstruct void init()` (auto-called hook) | `def __post_init__(self):` — **dataclass only** |
| `toString()` (one method) | two hooks + **two conversion paths** — str path (`str`/`print`/f-strings) vs repr path (`repr`/debugger); see § `__str__` vs `__repr__` |
| `@Override` | redefine method (no annotation) |
| `private` / `protected` | convention: `_name` (still accessible) |
| `static` field | class attribute (`Foo.bar = 1` in class body) |
| instance field `private int balance` | `self.balance = ...` in `__init__` |
| `record Person(String name, int age)` | `@dataclass` + fields |
| missing field reference | compile error | `AttributeError` at runtime |
| Scala `case class Person(name: String, age: Int)` | `@dataclass` (no pattern matching) |
| Lombok `@Data` / `@Value` | `@dataclass` / `@dataclass(frozen=True)` |
| `extends` | `class Child(Parent):` |
| `super()` | `super().__init__(...)` |
| `import java.util.*` | `from dataclasses import dataclass` (stdlib) |

### Class attributes vs instance attributes (`self`)

```java
class BankAccount {
    static String bankName = "Java Federal";
    String owner;
    double balance;
}
```

```python
class BankAccount:
    bank_name = "Python Federal"   # class attribute — shared (≈ static)

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner         # instance attribute — per object
        self.balance = balance
```

| Access | Result |
|--------|--------|
| `BankAccount.bank_name` | class attribute |
| `alice.bank_name` | same — **fallback** to class if not on instance |
| `alice.balance` | instance attribute |
| `alice.age` | `AttributeError` — not on instance or class |

**Inside methods:** `balance += amount` creates a **local** variable — wrong. Use `self.balance += amount`.

```python
def bad_deposit(self, amount: float) -> None:
    balance += amount
# UnboundLocalError — local 'balance' read before assignment (forgot self)

def good_deposit(self, amount: float) -> None:
    self.balance += amount
```

| Error | When | Java |
|-------|------|------|
| `AttributeError` | `obj.missing_attr` | compile error (unknown field) |
| `UnboundLocalError` | bare name assigned in function before bind — e.g. forgot `self` | field access usually compiles |
| `NameError` | name not defined at all | cannot find symbol |

**Never** use mutable defaults at class level (`items = []`) — shared across instances. Use `self.items = []` in `__init__`.

**`@dataclass`:** `name: str` in class body is a type hint; generated `__init__` sets `self.name` per instance (≈ `record` components).

Lesson: `lesson_08/05_class_vs_instance.py` · FAQ: § `self` required

### Missing `__init__` — Java default fields vs Python (Counter pattern)

```java
class Counter {
    private int count;          // default 0 — field exists on every instance

    void increment() { count++; }
}
```

```python
class Counter:
    def __init__(self) -> None:
        self.count = 0          # REQUIRED — Python does not auto-create attributes

    def increment(self) -> None:
        self.count += 1
```

| | Java | Python |
|--|------|--------|
| Instance field exists after `new` | yes — declared in class body | **no** — until `self.field = ...` in `__init__` |
| Default `int` / `null` | `0` / `null` | attribute **does not exist** → `AttributeError` |
| `count = 0` at class level + `self.count += 1` | misleading | shadows class with per-instance attrs — still use `__init__` |
| `Counter.count += 1` in method | `static` counter — truly shared | mutates class attribute |

Without `__init__` and no class attr: `self.count += 1` → `AttributeError`. Bare `count += 1` → `UnboundLocalError`.

### Attribute lookup — read (fallback) vs write (instance only)

**Read** `self.attr`: instance → class → parent classes → `AttributeError`.

**Write** `self.attr = v` or `self.attr += 1`: always on **instance** (creates attr if missing; does not mutate class).

```python
class ReallyBad:
    call_count = 0
    def ping(self) -> None:
        self.call_count += 1   # read class 0 → instance call_count = 1

a = ReallyBad()
a.ping()
# a.call_count == 1, ReallyBad.call_count == 0  (class orphaned)
```

| | Java | Python |
|--|------|--------|
| Read missing field | compile error | `AttributeError` at runtime |
| `this.x += 1` with only static `x` | must use `Class.x` | `self.x += 1` writes **instance** x (shadow) |
| Parent field | `super` / inherited | read falls through to parent class |

Inheritance lesson: `lesson_08/04_inheritance.py`

Lesson: `lesson_08/02_self_explained.py` · FAQ: § missing `__init__`

### `__str__` vs `__repr__` (Java `toString()` split in two)

**Do not teach** `print → __str__` and `repr → __repr__` as parallel 1:1 rules. Python has **two conversion paths**:

```
str path:   str(obj), print(obj), f"{obj}"   →  __str__ if defined, else __repr__
repr path:  repr(obj), debugger, REPL        →  __repr__ only (never __str__)
```

`print(obj)` always goes through `str(obj)` — **not** a third path.

| | Java | Python |
|--|------|--------|
| User/log output | `toString()` | **str path:** `str(obj)`, `print(obj)`, f-strings |
| Debugger / REPL | often same `toString()` | **repr path:** `repr(obj)` only |
| `print` vs `str` | N/A | **identical** — `print(obj)` calls `str(obj)` first |
| Both hooks defined | N/A | str path → `__str__`; repr path → `__repr__` |
| Only `__repr__` defined | N/A | both paths → `__repr__` (`str(obj) == repr(obj)`) |
| Only `__str__` defined | N/A | str path → `__str__`; repr path → `<Class at 0x...>` (**not** `__str__`) |
| `@dataclass` / record | `toString()` generated | `__repr__` generated |

**Builtins vs hooks — mapping Java doesn't have:** Python separates **call-site API** (`print`, `str`, `repr`, f-strings) from **class hooks** (`__str__`, `__repr__`). Builtins invoke the hooks for you — like `println` calling `toString()`, but with named builtins instead of one method. You *can* call `obj.__str__()` directly; idiomatic code uses `str(obj)` / `print(obj)` at call sites and defines hooks on the class only.

| Call site | Conversion path | Direct call (legal, not idiomatic) |
|-----------|-----------------|-------------------------------------|
| `str(obj)`, `print(obj)`, `f"{obj}"` | str path → `__str__`, else `__repr__` | `obj.__str__()` |
| `repr(obj)` | repr path → `__repr__` only | `obj.__repr__()` |

```python
def __repr__(self) -> str:
    return self.__str__()   # OK inside class — method calls use self. (≈ this.toString())
# return __str__(self)      # NameError — must be self.__str__()
# At call sites: str(self) / repr(self), not bare __str__(self)
```

Lesson: `lesson_08/03_str_repr_and_formatting.py` · FAQ: § `__str__` vs `__repr__`

### `equals()` / `hashCode()` → `__eq__` / `__hash__`

**Same contract as Java** (`Object` javadoc):

| Rule | Java | Python |
|------|------|--------|
| Equal → same hash | `a.equals(b)` ⇒ `a.hashCode() == b.hashCode()` | `a == b` ⇒ `hash(a) == hash(b)` |
| Same hash → equal | **not** required (collisions OK) | **not** required |
| Violation symptom | duplicate entries in `HashSet`, `get` misses in `HashMap` | same — or Python blocks with `__hash__ = None` |
| Hash same fields as equals | `Objects.hash(x, y)` | `hash((x, y))` |

Required for `set` / `dict` **keys**. Dict **values** are not hashed.

### When `__eq__` vs `__hash__` vs **both** (FAQ § full table)

| Operation | `__eq__` | `__hash__` | Java |
|-----------|----------|------------|------|
| `a == b` | yes | **no** | `equals()` only |
| `hash(a)` | no | yes | `hashCode()` only |
| `a in set` / `dict` **key** lookup | yes (verify) | yes (bucket) | `HashSet` / `HashMap` key — `hashCode` + `equals` |
| `dict` **value** | no | no | `HashMap` value — any type, mutable OK |
| `a in list` | yes (scan) | no | `List.contains` → `equals` |

Hash-based lookup: **`__hash__` first** (find bucket), then **`__eq__`** (confirm — collisions exist). `==` never calls `__hash__`. Lesson: `lesson_08/07_eq_and_hash.py` §3a-bis.

| | Java | Python |
|--|------|--------|
| Value equality | `a.equals(b)` | `a == b` → `a.__eq__(b)` |
| Identity | `a == b` (references) | `a is b` |
| Hash | `a.hashCode()` | `hash(a)` → `a.__hash__()` |
| Want `set` / `dict` key? | **must** define `hashCode()` matching `equals()` | **must** define `__hash__` matching `__eq__` |
| Override equality only | **still has** `Object.hashCode()` — can enter `HashSet` but broken | **`__hash__ = None`** — blocked from `set`/`dict` (`TypeError`) |
| Override both for collections | required by contract; IDE warns | define `__eq__` + `__hash__` together — only way to be hashable after custom `__eq__` |
| Mutable value object in `HashMap` | discouraged but compiles | `TypeError` if unhashable — Python blocks it |
| `@dataclass` / record | auto `equals`/`hashCode` | auto `__eq__`; `__hash__` only if `frozen=True` |
| `Comparable.compareTo()` | `__lt__` (+ `order=True` generates rich comparisons) | `sorted(xs)`, `min`/`max` without `key=` |
| `Comparator` | `sorted(xs, key=lambda x: ...)` | compares key results, not element `<` |
| `TreeSet` | no stdlib — `sorted(list)` or `sortedcontainers` | Python `set` is always hash-based |

```python
# Java: @Override equals AND hashCode together
# Python: if you customize __eq__ without __hash__, instances cannot be set/dict keys

@dataclass
class Person:
    name: str
    age: int

{Person("A", 1)}   # TypeError: unhashable type: 'Person'

@dataclass(frozen=True)
class Point:
    x: int
    y: int

{Point(1, 2), Point(1, 2)}   # {Point(1, 2)} — one element, __eq__ + __hash__ agree
```

**Return type hints** (`-> bool`) are not enforced at runtime — unlike Java `boolean`. Returning non-bool values is legal but bad practice except for protocol values like `NotImplemented`.

**`return NotImplemented`** — singleton object (not `NotImplementedError`, not `False`). When `a == b`: if `a.__eq__(b)` returns `NotImplemented`, Python tries **`b.__eq__(a)`** (reverse equals); if still `NotImplemented`, falls back to `a is b`. Java has no equivalent — use `return false` for wrong types.

**Identity check placement:** Java does **not** auto-check identity in `equals()` — developers who override `equals` **often** write `if (this == o) return true` first (idiom, not language rule). Python's **`==` operator** applies `a is b` **automatically** as the final step — you rarely write it inside `__eq__` (optional optimization only).

**`hash((x, y))` in `__hash__`** — ≈ `Objects.hash(x, y)`:

| | Java | Python |
|--|------|--------|
| Combine field hashes | `Objects.hash(x, y)` | `hash((x, y))` |
| Element types | any object with `hashCode()` | any **hashable** (`int`, `str`, `tuple`, …) |
| Result | `int` | `int` |
| Equal objects | same `hashCode` | same `hash()` |
| Order matters | field order in `Objects.hash` | `(x, y)` ≠ `(y, x)` |

`hash((1, 2))` hashes each element, mixes with a built-in combinator — not `hash(1) + hash(2)`. Lists/dicts inside tuples fail (`TypeError`).

FAQ: § `__eq__` and `__hash__` · Lesson: `lesson_08/07_eq_and_hash.py` · Practice: `lesson_08/practice/02_eq_hash.py`

### `__init__` — initializer (≈ constructor)

Fixed name — Python calls it when you write `Foo(...)`. You never call `__init__` yourself in normal code (same *idea* as Spring calling `@PostConstruct` for you, but at **construction** time).

```java
// Java
public class Dog {
    private final String name;
    public Dog(String name) { this.name = name; }
}
Dog rex = new Dog("Rex");
```

```python
# Python
class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

rex = Dog("Rex")   # __init__ called automatically — no `new`
```

**Nuance:** object is allocated first, then `__init__` runs (rarely you touch `__new__`).

### No constructor overloading

| Java | Python |
|------|--------|
| `Foo()`, `Foo(int)`, `Foo(String, int)` | **one** `def __init__(self, ...)` only |
| Second constructor overload | second `def __init__` **replaces** the first |
| Optional ctor args via overloads | **default args:** `def __init__(self, name, age=0):` |
| `this(name, 0)` delegation | `age=0` in signature |

```java
public Person(String name) { this(name, 0); }
public Person(String name, int age) { ... }
```

```python
class Person:
    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age
```

Applies to **all** methods — see `lesson_07/01_java_gotchas.py`. FAQ: § no constructor overloading.

### `__post_init__` — dataclass hook (≈ `@PostConstruct` timing)

Only on `@dataclass` classes. The **generated** `__init__` assigns fields, then calls `__post_init__` if defined. Use for validation or derived fields **after** assignment.

```java
// Java — fields injected / set, then hook
@PostConstruct
void validate() {
    if (age < 0) throw new IllegalArgumentException();
}
```

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValueError("age must be non-negative")
```

On a **plain** class (no `@dataclass`), `__post_init__` is **not** called automatically.

### `@dataclass` — data carrier (≈ `record` / Scala `case class`)

Stdlib **decorator** (not a Java annotation) — runs at class definition time and generates `__init__`, `__repr__`, `__eq__`.

```java
// Java 16+ record
public record Person(String name, int age) {}
```

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
print(alice)   # Person(name='Alice', age=30)
```

| | Java `record` | Python `@dataclass` (default) | `@dataclass(frozen=True)` |
|--|---------------|----------------------------------|---------------------------|
| Mutability | immutable | mutable | immutable (≈ record) |
| Inheritance | very limited | `class Employee(Person)` OK | same |
| `copy` with one field changed | record compact ctor | `dataclasses.replace(p, age=31)` | same |
| Auto `equals` / `hashCode` | yes | `__eq__` yes; `__hash__` if `frozen` | yes |
| Keyword args at call site | no (use builder) | `Person(age=18, name="Bob")` | same |
| Missing required field | compile error | `TypeError` at runtime | same |

### Dataclass construction — required, defaults, keyword args

```python
@dataclass
class Person:
    name: str
    age: int
    email: str = ""   # default — must come after non-default fields
```

| Call | Result |
|------|--------|
| `Person("Bob", 18)` | OK — positional, order = field order |
| `Person(age=18, name="Bob")` | OK — keyword order free |
| `Person("Bob", 25)` | OK — `email` defaults to `""` |
| `Person()` | `TypeError` — missing `name`, `age` |
| `Person(18, "Bob")` | Runs but **wrong** — no runtime type check |

```java
// Java — positional only; compile-time errors for missing args
public record Person(String name, int age) {}
var bob = new Person("Bob", 18);
// new Person();                    // compile error
// new Person(18, "Bob");           // compile error (wrong types)
// No: new Person(age=18, name="Bob")
```

**Field order in class:** required fields first, then fields with defaults (same rule as `def f(a, b=1):`).

Lesson: `lesson_08/06_dataclass.py` · FAQ: § dataclass construction

### `frozen=True` — shallow immutability & immutable collections

`@dataclass(frozen=True)` ≈ Java `record`: **field reassignment** blocked, `replace()` for copies.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 5  # FrozenInstanceError
```

**Shallow only** — mutable objects inside fields can still be mutated (same as `record` with `List` field):

```java
public record Wrapper(List<Integer> items) {}
// w.items() = List.of(9);  // compile error
w.items().add(3);            // OK at runtime
```

| Mutable field type | Immutable substitute for `frozen=True` fields |
|--------------------|-----------------------------------------------|
| `list` | `tuple` (no stdlib `frozenlist`) |
| `set` | `frozenset` |
| `dict` | no stdlib `frozendict`; `tuple(d.items())` or `types.MappingProxyType(d)` |

```python
@dataclass(frozen=True)
class Config:
    tags: frozenset[str]
    coords: tuple[int, int]
```

| Python | Mutable | Immutable | Java |
|--------|---------|-----------|------|
| sequence | `list` | `tuple` | `ArrayList` / `List.of()` |
| unique set | `set` | `frozenset` | `HashSet` / `Set.of()` |
| mapping | `dict` | (no built-in `frozendict`) | `HashMap` / `Map.of()` |

FAQ: § `frozen=True`, `frozenset`, shallow immutability · Lesson: `lesson_08/06_dataclass.py`

### Exception handling — dataclass / frozen (runtime vs Java compile-time)

```python
from dataclasses import FrozenInstanceError, dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)

try:
    p.x = 5
except FrozenInstanceError:
    ...   # Java: would not compile for record component

try:
    Person()  # missing required fields
except TypeError:
    ...

try:
    Person("Bad", -1)  # __post_init__ raises ValueError
except ValueError:
    ...
```

| Error | Python exception | Java analog |
|-------|------------------|-------------|
| Missing ctor args | `TypeError` | compile error |
| Validation in hook | `ValueError` (typical) | `IllegalArgumentException` in ctor |
| Reassign frozen field | `FrozenInstanceError` | compile error on `record` |
| `frozenset.add` | `AttributeError` | N/A |
| `tuple[i] = x` | `TypeError` | N/A |
| Mutate nested `list` in frozen dataclass | **no error** (shallow) | `items().add(...)` on record |

Runnable demos: `lesson_08/06_dataclass.py` § Exception handling.

## Functional / streams

| Java | Python |
|------|--------|
| `stream().map(f)` | `(f(x) for x in xs)` or `[f(x) for x in xs]` |
| `stream().filter(p)` | `(x for x in xs if p(x))` |
| `stream().anyMatch(p)` | `any(p(x) for x in xs)` |
| `stream().allMatch(p)` | `all(p(x) for x in xs)` |
| `stream().count()` | `len(xs)` or `sum(1 for ...)` |
| `stream().sum()` | `sum(xs)` |
| `stream().sorted()` | `sorted(xs)` |
| `stream().max(Comparator)` | `max(xs, key=...)` |
| `Comparator.comparing(Foo::getX)` | `key=lambda x: x.x` |
| `.thenComparing(Foo::getY)` | `key=lambda x: (x.x, x.y)` |
| `collect(toList())` | `[...]` comprehension |
| filter + sort (one pass) | `sorted(x for x in xs if p(x))` — **no `[]`** unless you need the list twice |
| `collect(toMap())` | `{...}` comprehension or `dict(zip(...))` |

## Built-ins (no import)

| Java-ish need | Python |
|---------------|--------|
| `.size()` | `len(x)` |
| sort copy | `sorted(x)` — **always returns new `list`** |
| filter then sort (no extra list) | `sorted(x for x in xs if p(x))` — prefer over `sorted([...])` |
| sort in place | `x.sort()` — lists only; returns `None` |
| sort `keySet()` | `sorted(d)` or `sorted(d.keys())` — list of keys |
| sort map entries | `sorted(d.items())` — list of `(key, value)` tuples |
| sort string chars | `sorted("cba")` → `['a','b','c']` |
| `map.keySet()` view | `d.keys()` — `dict_keys` view, iterable not list |
| `new ArrayList<>(map.keySet())` | `list(d)` or `list(d.keys())` — **keys only**, insertion order (3.7+) |
| ordered unique keys from sequence | `list(dict.fromkeys(items))` — dedupe, first-seen order; no Java one-liner |
| `dict.fromkeys(keys, default)` | map each key → same value (default `None`); values often discarded |
| reverse copy | `x[::-1]` or `reversed(x)` |
| top-k smallest / largest (full sort OK) | `sorted(xs, key=...)[:k]` or `sorted(xs, reverse=True)[:k]` |
| top-k on huge n, small k | `import heapq` → `heapq.nsmallest(k, xs, key=...)` / `nlargest` |
| `PriorityQueue` / `poll` / `offer` | `heapq.heapify(list)` + `heappush` / `heappop` on that list |
| enumerate index | `enumerate(x)` |
| zip parallel lists | `zip(a, b)` → iterator of tuples |
| `list(zip(a,b))` | list of tuples — `[("a", 1), ("b", 2)]` |
| `dict(zip(a,b))` / `dict(pairs)` | map from parallel keys+values or pair list |
| list of rows → columns | `zip(*matrix)` — `*` unpacks rows as separate args |
| **transpose matrix** | `[list(col) for col in zip(*matrix)]` — **not** 90° rotation |
| transpose without `*` | `[[row[i] for row in matrix] for i in range(len(matrix[0]))]` — ≈ nested `for (c) for (r)` |
| `zip(matrix)` wrong | zips one iterable (rows as elements) — use `zip(*matrix)` |
| `zip` unequal lengths | `strict=False` truncates; `strict=True` raises — Java: check sizes manually |
| varargs spread | `zip(*rows)` — Java: `method(rows.get(0), rows.get(1), ...)` or loop |
| min / max | `min(x)` / `max(x)` |
| total | `sum(x)` |

## Errors & null checks

| Java | Python |
|------|--------|
| `if (x == null)` | `if x is None:` |
| `if (list != null && !list.isEmpty())` | `if list:` |
| `IndexOutOfBoundsException` | `IndexError` |
| `NullPointerException` | often `AttributeError` or `TypeError` |
| `.indexOf` returns -1 | `.index()` raises `ValueError` |

## Modules & tooling (Lesson 3+)

| Java | Python |
|------|--------|
| `package` / `import` | `import module` / `from x import y` |
| Maven `pom.xml` | `pyproject.toml` + `uv` |
| `mvn run` | `uv run python script.py` |
| `.env` + properties | `python-dotenv` + `os.environ` |
| `mvn test` | `uv run pytest` |

## Unit testing (Lesson 16) — JUnit 5 primary

**Default:** pytest ≈ JUnit 5. Legacy: unittest ≈ JUnit 4 (`04_unittest_legacy.py`).

| Java (JUnit 5) | Python (pytest) |
|----------------|-----------------|
| `@Test void add()` | `def test_add():` |
| `assertEquals(5, add(2,3))` | `assert add(2, 3) == 5` |
| `assertThrows(Ex.class, () -> f())` | `with pytest.raises(Ex): f()` |
| `assertAll(() -> …, () -> …)` | multiple `assert` in one test |
| `@BeforeEach void setUp()` | `@pytest.fixture` |
| `@BeforeAll` | `@pytest.fixture(scope="module")` |
| `@ParameterizedTest` + `@CsvSource` | `@pytest.mark.parametrize(...)` |
| `@Disabled` | `@pytest.mark.skip` |
| `@ExtendWith(MockitoExtension.class)` | `MagicMock()` passed into constructor |

| Java (Mockito) | Python (`unittest.mock`) |
|----------------|--------------------------|
| `mock(Foo.class)` | `MagicMock()` |
| `when(m.f()).thenReturn(x)` | `m.f.return_value = x` |
| `when(m.f()).thenThrow(ex)` | `m.f.side_effect = ex` |
| `verify(m).f()` | `m.f.assert_called_once()` |
| `@Mock` / `@InjectMocks` | manual `Greeter(mock)` or `@patch` |

Run: `uv sync --group dev` then `uv run pytest lesson_16/ -v`

### Flask REST — Spring Boot Test / MockMvc?

**Lesson 16:** `05_flask_testing.py` · **Lesson 11:** Flask routes · Practice: `02_flask_api.py`

| Spring Boot Test | Flask + pytest |
|------------------|----------------|
| `@WebMvcTest` + `MockMvc` | `app.test_client()` |
| `mockMvc.perform(get("/books"))` | `client.get("/books")` |
| `.andExpect(status().isOk())` | `assert response.status_code == 200` |
| `.andExpect(jsonPath("$.title").value("x"))` | `assert response.get_json()["title"] == "x"` |
| `@SpringBootTest` + `create_app` | `@pytest.fixture def app(): return create_app(testing=True)` |
| `@MockBean` | `@patch("myapp.module.service_fn")` — not Flask's `request` proxy |

```python
@pytest.fixture
def client(app):
    return app.test_client()

def test_create_book(client):
    r = client.post("/books", json={"title": "Dune"})
    assert r.status_code == 201
```

## JSON (Lesson 10)
|---------|---------------|
| `readValue(s, Map.class)` | `json.loads(s)` |
| `writeValueAsString(obj)` | `json.dumps(obj)` |

## File I/O (Lesson 6 — planned)

| Java | Python |
|------|--------|
| `java.nio.file.Paths` | `pathlib.Path` |
| `Files.readString` / `readAllLines` | `Path.read_text()` / `readlines()` or `for line in f` |
| `Files.writeString` | `Path.write_text()` |
| try-with-resources | `with open(...) as f:` |
| `BufferedReader.readLine()` | `for line in f:` (text mode) |
| `InputStream` / `OutputStream` | `open(path, "rb")` / `"wb"` |
| `Files.walk` | `Path.rglob("*")` |

## Concurrency & async I/O (Lesson 7 — planned)

| Java | Python |
|------|--------|
| `ExecutorService` | `concurrent.futures.ThreadPoolExecutor` |
| `CompletableFuture` | `asyncio` + `async`/`await` (different model) |
| blocking HTTP client | `requests` / sync `httpx` (Lesson 4) |
| async / reactive HTTP | `httpx.AsyncClient`, `aiohttp` (Lesson 7) |
| true multi-core CPU threads | GIL limits CPU parallelism — `multiprocessing` |
| `ConcurrentHashMap` | `threading.Lock` + `dict` |

## Database (Lesson 17)

Python has **no JPA in the stdlib**. Learn in layers: **DB-API 2.0** (JDBC-like) → **SQLAlchemy** (Hibernate/JPA-like).

| Java | Python | Notes |
|------|--------|-------|
| JDBC `Connection` | `sqlite3.connect()` / driver `connect()` | PEP 249 DB-API 2.0 |
| `DriverManager.getConnection(url)` | `sqlalchemy.create_engine(url)` | URL like `sqlite:///app.db` |
| `PreparedStatement` + `?` | `cursor.execute("... WHERE id = ?", (id,))` | **Always** bind params — never f-string SQL |
| `ResultSet` / `rs.next()` | `cursor.fetchone()` / `fetchall()` | rows as tuples or dict rows |
| `try/finally conn.close()` | `with conn:` / `with engine.connect()` | context managers |
| `conn.setAutoCommit(false)` | `conn.commit()` / `rollback()` | explicit transactions |
| `JdbcTemplate` (Spring) | SQLAlchemy **Core** `session.execute(text(...))` | SQL-first, less boilerplate than raw JDBC |
| JPA `@Entity` | SQLAlchemy **ORM** `class Book(Base):` + `Mapped` columns | declarative mapping |
| `EntityManager.persist` | `session.add(obj)`; `session.commit()` | unit of work |
| `EntityManager.find` | `session.get(Book, id)` / `session.scalars(select(...))` | 2.0 style queries |
| JPQL / Criteria API | SQLAlchemy `select(Book).where(...)` | composable query builder |
| Flyway / Liquibase | **Alembic** | migration scripts |
| HikariCP pool | SQLAlchemy `Engine` pool (built-in) | `create_engine(..., pool_size=5)` |
| Spring Data `JpaRepository` | Flask-SQLAlchemy / custom repo layer | not one stdlib answer |
| H2 / embedded DB in tests | `sqlite:///:memory:` | Lesson 16 Flask tests |
| PostgreSQL driver | **psycopg** (v3) | `postgresql+psycopg://...` in URL |

**Drivers (install per DB):** `sqlite3` is stdlib; Postgres → `psycopg`; MySQL → `mysqlclient` or `pymysql`.

**ORM choice:** **SQLAlchemy 2.0** is the default teaching ORM (ecosystem standard). Django ORM only if you adopt Django — out of scope unless we add a Django track.

Lesson: `lesson_17/` · Practice: `lesson_17/practice/01_db_api.py`, `02_sqlalchemy_crud.py`

## AWS (Lesson 8)

| Java Lambda | Python Lambda |
|-------------|---------------|
| `RequestHandler` | `def handler(event, context):` |
| AWS SDK v2 | `boto3` |
| API Gateway event POJO | `event` dict (JSON) |
