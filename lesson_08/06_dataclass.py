"""Lesson 2f — @dataclass (≈ Java record / Scala case class)."""

from dataclasses import FrozenInstanceError, dataclass, replace
from types import MappingProxyType


def expect_error(label: str, exc_type: type[BaseException], action) -> None:
    """Run action(); print success if the expected exception is raised."""
    try:
        action()
        print(f"  ✗ {label} — expected {exc_type.__name__}, nothing raised")
    except exc_type as e:
        print(f"  ✓ {label} — {exc_type.__name__}: {e}")
    except Exception as e:
        print(f"  ✗ {label} — expected {exc_type.__name__}, got {type(e).__name__}: {e}")


@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # default — fields WITH defaults must come AFTER required fields

    # Optional hook — runs AFTER generated __init__ assigns fields.
    # ≈ Spring @PostConstruct (fields exist first, then validate).
    # NOT called on plain classes — only @dataclass.
    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValueError("age must be non-negative")


# --- Construction: positional, keyword, defaults, required fields ---

# Positional — order MUST match field order (name, age, email)
alice = Person("Alice", 30, "alice@example.com")

# Skip fields that have defaults (email omitted → "")
bob = Person("Bob", 25)

# Keyword args — order does NOT matter (no Java equivalent at call site)
carol = Person(age=18, name="Carol")
print(carol)  # Person(name='Carol', age=18, email='')

# Mix positional then keyword (positionals must come first)
dave = Person("Dave", age=40)

print(alice)
print(alice == Person("Alice", 30, "alice@example.com"))

# --- frozen=True: shallow immutability (≈ Java record) ---

@dataclass(frozen=True)
class Point:
    x: int
    y: int


origin = Point(0, 0)

# __eq__ / __hash__ (equals/hashCode): full lesson → lesson_08/07_eq_and_hash.py

# Shallow only: frozen blocks rebinding fields, NOT mutating objects inside them
@dataclass
class Inner:
    value: int


@dataclass(frozen=True)
class Wrapper:
    items: list[int]
    inner: Inner


w = Wrapper([1, 2], Inner(10))
w.items.append(3)  # OK — mutating the list object (same as Java record + mutable List)
w.inner.value = 99  # OK — Inner is a mutable dataclass
print(w)  # Wrapper(items=[1, 2, 3], inner=Inner(value=99))

# Truly fixed collections: use immutable field types
@dataclass(frozen=True)
class TagSet:
    tags: frozenset[str]  # immutable set — no .add()
    coords: tuple[int, int]  # tuple = frozen list (no stdlib frozenlist)


ts = TagSet(frozenset({"python", "java"}), (0, 0))

# Scala case class .copy(age = 31) ≈ dataclasses.replace
older_alice = replace(alice, age=31)
print(older_alice)

# --- Exception handling demos (Java: mostly compile-time errors; Python: runtime) ---

print("\n--- construction errors (TypeError) ---")
expect_error("Person() missing required fields", TypeError, lambda: Person())  # type: ignore[call-arg]
expect_error("Person('OnlyName') missing age", TypeError, lambda: Person("OnlyName"))  # type: ignore[call-arg]

print("\n--- __post_init__ validation (ValueError) ---")
expect_error(
    "negative age in __post_init__",
    ValueError,
    lambda: Person("Bad", -1),
)

print("\n--- frozen field reassignment (FrozenInstanceError) ---")
expect_error("origin.x = 1", FrozenInstanceError, lambda: setattr(origin, "x", 1))
expect_error("w.items = [9]", FrozenInstanceError, lambda: setattr(w, "items", [9]))

print("\n--- shallow freeze: mutation inside field is still OK ---")
try:
    w.items.append(100)
    print(f"  ✓ w.items.append(100) — no exception; items={w.items}")
except Exception as e:
    print(f"  ✗ w.items.append(100) — unexpected {type(e).__name__}: {e}")

print("\n--- immutable collection types ---")
expect_error("frozenset.add", AttributeError, lambda: ts.tags.add("go"))


def _tuple_item_assignment() -> None:
    coords = (0, 0)
    coords[0] = 9  # type: ignore[index]


expect_error("tuple item assignment", TypeError, _tuple_item_assignment)

print("\n--- MappingProxyType read-only dict (TypeError on write) ---")


def _proxy_write() -> None:
    readonly = MappingProxyType({"theme": "dark"})
    readonly["x"] = 1


expect_error("MappingProxyType['x'] = 1", TypeError, _proxy_write)

print("\n--- replace() builds a new instance (no exception) ---")
moved = replace(origin, x=5)
print(f"  ✓ replace(origin, x=5) → {moved}; origin still {origin}")
