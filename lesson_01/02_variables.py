"""Lesson 1b — variables and types (intro).

Full datatypes lesson → lesson_06/01_types_and_datatypes.py

Run:
    uv run python lesson_01/02_variables.py
"""

age = 25           # int
price = 9.99       # float
name = "Alex"      # str
is_active = True   # bool — capital T/F (not true/false)
nothing = None     # like Java's null

print(type(age), type(price), type(name), type(is_active), type(nothing))
# print takes any number of args — separated by space (sep=" "); see 01_syntax.py
