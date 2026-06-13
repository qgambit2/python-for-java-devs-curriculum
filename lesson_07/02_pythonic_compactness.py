"""Lesson 1o — writing compact Python (for Java devs who already think in steps)."""

# --- Rule 1: working beats clever ---
# Java habit: explicit loops, temp variables, mutate a Map — totally valid in Python.
# Idiomatic Python is often the SAME logic with less ceremony — not a different algorithm.

# --- Rule 2: loop first, compress second ---
# Step 1 — make tests pass with a loop (collections_practice style)
words = ["hi", "hey", "yo", "a"]


def group_by_length_loop(items: list[str]) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}
    for word in items:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result


# Step 2 — compress only when you recognize "group by key"
# (defaultdict or setdefault also fine; loop version is enough for learning)
print(group_by_length_loop(words))

# --- Rule 3: common loop shapes → idioms ---
# filter + collect list     →  [f(x) for x in xs if cond(x)]
# filter + collect map      →  {k: v for ... if cond}
# parallel lists → map       →  dict(zip(keys, vals))  or comp with zip
# transpose matrix           →  [list(col) for col in zip(*rows)]  — * unpacks rows
# merge maps (sum values)    →  {k: a.get(k,0)+b.get(k,0) for k in a.keys()|b.keys()}
# invert map                 →  {v: k for k, v in d.items()}
# transform map values       →  {k: sorted(v) for k, v in d.items()}  NOT for k,v in d
# group into map of lists    →  d.setdefault(key, []).append(item)
# shallow copy list          →  lst[:]  lst.copy()  list(lst)  — Java new ArrayList<>
# shallow copy dict          →  {**d}  d.copy()  dict(d)  — NOT d[:]  — Java new HashMap<>
# merge dicts (new dict)     →  {**defaults, **user}  — Java putAll; filter keys for configure

names = ["alice", "bob", "carol"]
scores = [90, 55, 88]
threshold = 60

# Loop version
passing_loop: dict[str, int] = {}
for name, score in zip(names, scores):
    if score >= threshold:
        passing_loop[name] = score

# Compressed — same logic, one expression
passing_comp = {name: score for name, score in zip(names, scores) if score >= threshold}
print(passing_loop == passing_comp)

# --- Rule 4: built-ins replace boilerplate loops ---
# len, sum, min, max, sorted, any, all, zip, enumerate — no import needed
nums = [3, 1, 4, 1, 5]
print(sorted(nums, reverse=True)[:2])          # top 2 — like stream sorted limit
print(any(s >= 60 for s in scores))            # anyMatch
print(sum(1 for s in scores if s >= 60))       # filter + count

# --- Rule 5: when NOT to one-liner ---
# - side effects (print, file I/O, append to shared state)
# - multi-step business rules (improved_names, configure pipelines)
# - when a name helps: result = right.copy() reads better than inline mutation
# Bad style: [print(x) for x in nums]   # use a for loop for side effects

# --- Rule 6: how to get better (practical) ---
# 1. Solve practice files with loops — you are doing this correctly.
# 2. After tests pass, ask: "is this filter/map/collect/group-by?"
# 3. Re-read lesson 11_comprehensions.py + compare your loop to the comp.
# 4. Steal patterns from solutions one at a time — don't skip the loop phase.
# Compactness is pattern recognition, not a separate skill.
