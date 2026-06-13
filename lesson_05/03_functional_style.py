"""Lesson 1q — functional style for Java developers (not a Haskell course).

Ties together: lambdas, map/filter, generators, functools.
Java Streams ≈ comprehensions + generators — no stdlib Stream API.

Prerequisites: 05/02_comprehensions.py, 05/01_builtins.py

Run:
    uv run python lesson_05/03_functional_style.py
"""

from functools import partial, reduce
from itertools import chain, islice
from operator import attrgetter, itemgetter


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. Functions are first-class — pass them like Java lambdas")

def double(n: int) -> int:
    return n * 2


nums = [1, 2, 3]
fn = double          # reference to function object — no () 
print(f"fn(5): {fn(5)}")
print(f"map(double, nums): {list(map(double, nums))}")
# Java: nums.stream().map(this::double).collect(toList())


section("2. lambda — single expression only (no statements)")

# Java: n -> n * 2
square = lambda n: n * n
print(f"square(4): {square(4)}")

# key= in sorted — most common real use of lambda in Python
people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
print(sorted(people, key=lambda p: p["age"]))
# Java: Comparator.comparing(p -> p.get("age"))


section("3. No :: method references — lambda, itemgetter, or attrgetter")

# Java: Comparator.comparing(Person::getName)
# Dict rows — itemgetter (bracket access):
print(sorted(people, key=itemgetter("name")))
# Object rows — attrgetter (dot access); Lesson 2 @dataclass:
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

team = [Person("Bob", 30), Person("Alice", 25)]
print(sorted(team, key=attrgetter("name")))
# Or always: key=lambda p: p["name"] / key=lambda p: p.name


section("4. map / filter vs comprehensions — both exist; comps usually win")

nums = [1, 2, 3, 4, 5, 6]

# map/filter return lazy iterators (consume once)
evens_map = map(lambda n: n * 2, filter(lambda n: n % 2 == 0, nums))
print(f"map+filter: {list(evens_map)}")

# Idiomatic — same result, clearer to most Python readers
evens_comp = [n * 2 for n in nums if n % 2 == 0]
print(f"comprehension: {evens_comp}")

# Java: stream().filter().map().collect()  →  prefer [expr for x in xs if cond]


section("5. Generator expression — lazy pipeline (Stream before collect)")

# Parentheses = lazy; square brackets = eager list
odd_squares = (n * n for n in nums if n % 2 == 1)
print(f"sum of odd squares: {sum(odd_squares)}")   # consumes generator
# odd_squares is exhausted now — create again if you need another pass

# any / all short-circuit — like anyMatch / allMatch
print(f"any > 5: {any(n > 5 for n in nums)}")
print(f"all > 0: {all(n > 0 for n in nums)}")


section("6. yield — generator functions (lazy, pausable)")

def count_up_to(n: int):
    """Java has no direct equivalent — manual Iterator or Stream.iterate."""
    i = 1
    while i <= n:
        yield i
        i += 1


print(f"list(count_up_to(5)): {list(count_up_to(5))}")
for x in count_up_to(3):
    print(f"  yielded: {x}")


section("7. functools.partial — fix some arguments")

def power(base: int, exp: int) -> int:
    return base ** exp


square_fn = partial(power, exp=2)
print(f"partial(power, exp=2)(5): {square_fn(5)}")


section("8. reduce exists — loops / sum usually clearer")

# Java: stream().reduce(0, Integer::sum)
print(f"reduce add: {reduce(lambda a, b: a + b, nums)}")
print(f"sum(nums): {sum(nums)}")   # prefer this


section("9. itertools teaser — chain, islice")

a = [1, 2]
b = [3, 4]
print(f"chain: {list(chain(a, b))}")
print(f"first 3 of range(100): {list(islice(range(100), 3))}")


section("10. What Python is NOT")

print("""
- Not immutable by default — tuple/frozenset help; lists/dicts mutate freely
- No tail-call optimization — deep recursion is a bad idea
- No stdlib Stream / Optional monad — use comprehensions, generators, plain None checks
- parallelStream() → multiprocessing / ProcessPoolExecutor (not built into comps)

See also: lesson_05/02_comprehensions.py, lesson_05/01_builtins.py
""")
