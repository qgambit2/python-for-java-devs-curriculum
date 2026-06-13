"""Lesson 2b — why `self` exists."""

from dataclasses import dataclass


class Counter:
    def __init__(self) -> None:
        # REQUIRED — Java gives `private int count` default 0; Python does not.
        # Without this line, increment()/get() raise AttributeError.
        self.count = 0

    def increment(self) -> None:
        # Java: this.count++
        # Python: self is how the method knows WHICH object's count to change
        self.count += 1

    def get(self) -> int:
        return self.count


a = Counter()
b = Counter()
a.increment()
a.increment()
b.increment()
print(a.get())  # 2
print(b.get())  # 1

# --- What breaks without __init__? ---
class CounterNoInit:
    def increment(self) -> None:
        self.count += 1

    def get(self) -> int:
        return self.count


try:
    CounterNoInit().increment()
except AttributeError as e:
    print(f"no __init__: {e}")

# WRONG: class-level count = 0 — self.count += 1 creates per-instance attrs (shadows class).
# Looks like it works but never uses __init__; class count stays 0. Don't do this.
class ShadowCounter:
    count = 0

    def increment(self) -> None:
        self.count += 1


x, y = ShadowCounter(), ShadowCounter()
x.increment()
x.increment()
y.increment()
print(f"ShadowCounter: class={ShadowCounter.count}, x={x.count}, y={y.count}")
# class=0, x=2, y=1 — confusing shadows, not real fields from __init__

# @dataclass generates __init__ that sets self.name per instance
@dataclass
class Person:
    name: str
    age: int = 0
