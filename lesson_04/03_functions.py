"""Lesson 1f — functions."""


def greet(person: str, times: int = 1) -> str:
    """Return a greeting repeated `times` times. Type hints are optional."""
    return (f"Hi, {person}! ") * times


print(greet("Java dev"))
print(greet("Java dev", times=3))

# Don't mutate the caller's dict — surprising side effect (like map.put on a passed-in Map)
def merge_into_right_bad(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    for name, score in left.items():
        right[name] = right.get(name, 0) + score
    return right

right = {"bob": 3, "carol": 7}
merge_into_right_bad({"alice": 10, "bob": 5}, right)
print(right)   # {'bob': 8, 'carol': 7, 'alice': 10} — caller's dict was modified!

# Safe: copy first, then return new dict
def merge_scores(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    result = right.copy()
    for name, score in left.items():
        result[name] = result.get(name, 0) + score
    return result

right = {"bob": 3, "carol": 7}
out = merge_scores({"alice": 10, "bob": 5}, right)
print(out)     # merged result
print(right)   # {'bob': 3, 'carol': 7} — unchanged
