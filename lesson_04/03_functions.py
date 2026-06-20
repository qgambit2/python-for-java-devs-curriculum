"""Lesson 4 — functions: defaults, *args, **kwargs, safe dict merge.

Run:
    uv run python lesson_04/03_functions.py
"""


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. def — defaults and keyword args at call site")

def greet(person: str, times: int = 1) -> str:
    """Return a greeting repeated `times` times. Type hints are optional."""
    return (f"Hi, {person}! ") * times


# Java: no overloading — one method; use default parameter instead:
#   void greet(String person) { greet(person, 1); }
#   void greet(String person, int times) { ... }
print(greet("Java dev"))
print(greet("Java dev", times=3))   # keyword arg — order doesn't matter after positional


section("2. *args and **kwargs — Java varargs comparison")

# Java varargs — positional only, last parameter:
#   static int sum(int... values) { int t = 0; for (int v : values) t += v; return t; }
#   sum(1, 2, 3);   // values is int[]
#
# Python splits extra arguments two ways:
#   *args    → tuple of extra POSITIONAL args   (≈ int... values)
#   **kwargs → dict of extra KEYWORD args      (no Java equivalent)


def demo(a: int, *args: int, **kwargs: object) -> None:
    print(f"  a={a}")
    print(f"  args={args}")        # tuple
    print(f"  kwargs={kwargs}")    # dict


print("demo(1, 2, 3, name='Ann', total=9.5):")
demo(1, 2, 3, name="Ann", total=9.5)
# a=1  args=(2, 3)  kwargs={'name': 'Ann', 'total': 9.5}


def sum_all(first: int, *rest: int) -> int:
    return first + sum(rest)


print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")   # Java: sum(1, 2, 3, 4) with int...


def format_template(template: str, **kwargs: object) -> str:
    # Caller: format_template("Dear {name}", name="Ann")
    # kwargs inside: {"name": "Ann"}
    # template.format(**kwargs) unpacks dict → .format(name="Ann")
    return template.format(**kwargs)


print(format_template("Dear {name}, total=${total:.2f}", name="Ann", total=9.5))

# Unpacking at CALL site (opposite of collecting in def):
values = (10, 20)
print("{} + {}".format(*values))   # 10 + 20 — same as .format(10, 20); Java: no spread


section("3. Do not mutate caller's collections")

def merge_into_right_bad(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    for name, score in left.items():
        right[name] = right.get(name, 0) + score
    return right


right = {"bob": 3, "carol": 7}
merge_into_right_bad({"alice": 10, "bob": 5}, right)
print(f"bad — caller's right mutated: {right}")


def merge_scores(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    result = right.copy()
    for name, score in left.items():
        result[name] = result.get(name, 0) + score
    return result


right = {"bob": 3, "carol": 7}
out = merge_scores({"alice": 10, "bob": 5}, right)
print(f"good — out={out}")
print(f"good — right unchanged: {right}")


section("4. Mutable default args — classic gotcha")

# WRONG: def add(item, bucket=[]):  — same list shared across calls
def add_item(item: str, bucket: list[str] | None = None) -> list[str]:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item("a"))        # ['a']
print(add_item("b"))        # ['b']  — not ['a', 'b']
