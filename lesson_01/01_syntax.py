"""Lesson 1a — syntax (Java vs Python indentation).

Run:
    uv run python lesson_01/01_syntax.py
"""

# Java:
#   if (x > 0) {
#       System.out.println("positive");
#   }
#
# Python:
x = 10
if x > 0:
    print("positive")  # indentation defines the block — no { }


# --- print() — any number of arguments (unlike println(one thing)) ---
#
# Java: System.out.println(a + " " + b)  — one expression
# Python: print(a, b, c)                 — any count; str() each; join with sep
#
# print()          → blank line
# print("one")     → one
# print("a", "b")  → a b          (default sep=" ")
#
# print("x", end="")     → no newline (Java: print without println — use end)
# print("a", "b", sep="-")  → a-b

print("hello", "world")
print(type(42), type("hi"))   # preview — full types in lesson_06
print("same line", end=" → ")
print("continued")
