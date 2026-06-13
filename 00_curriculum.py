"""
Python for Java Developers — full curriculum
==========================================

One folder per lesson. Files numbered 01_, 02_, … in teaching order.
Each lesson folder may also contain basics.py (index runner) and practice/ exercises.

Status: ✅ done  ·  🔶 partial  ·  📋 planned

    uv run python 00_curriculum.py
    uv run python lesson_00/basics.py --list
    uv run python lesson_02/basics.py --list

Tutor docs: .cursor/skills/python-for-java-devs/


================================================================================
LESSON 0 — Environment setup (macOS / Linux / Windows)                     ✅
================================================================================
    lesson_00/01_setup_mac_linux.py   — install uv, uv sync, Cursor, how to run
    lesson_00/02_setup_windows.py   — same for Windows paths & PowerShell
    lesson_00/03_verify_environment.py — ✓ checklist before Lesson 1

    Start here if you are new. Run verify:
        uv run python lesson_00/03_verify_environment.py


================================================================================
LESSON 1 — Syntax & variables                                              ✅
================================================================================
    lesson_01/01_syntax.py
    lesson_01/02_variables.py
    Practice: lesson_01/practice/01_practice.py


================================================================================
LESSON 2 — Collections (list, dict, tuple, set) & slicing                    ✅
================================================================================
    lesson_02/01_collections.py
    lesson_02/02_slicing.py
    Practice: lesson_02/practice/01_collections.py, lesson_02/practice/02_collections.py


================================================================================
LESSON 3 — Strings & formatting                                            ✅
================================================================================
    lesson_03/01_strings.py
    Practice: lesson_03/practice/01_strings.py


================================================================================
LESSON 4 — Loops, truthiness, functions                                    ✅
================================================================================
    lesson_04/01_loops.py
    lesson_04/02_truthiness.py
    lesson_04/03_functions.py


================================================================================
LESSON 5 — Builtins, comprehensions, functional style                      ✅
================================================================================
    lesson_05/01_builtins.py
    lesson_05/02_comprehensions.py
    lesson_05/03_functional_style.py
    Practice: lesson_05/practice/01_builtins.py, lesson_05/practice/02_builtins.py
               lesson_05/practice/03_comprehensions.py


================================================================================
LESSON 6 — Types, math, datetime, recursion                                ✅
================================================================================
    lesson_06/01_types_and_datatypes.py
    lesson_06/02_math_and_numbers.py
    lesson_06/03_datetime.py
    lesson_06/04_recursion.py
    Practice: lesson_06/practice/ (planned)   📋 planned


================================================================================
LESSON 7 — Java gotchas, pythonic style, cheat sheet                       ✅
================================================================================
    lesson_07/01_java_gotchas.py
    lesson_07/02_pythonic_compactness.py
    lesson_07/03_cheat_sheet.py


================================================================================
LESSON 8 — Classes, OOP & dataclasses                                      🔶
================================================================================
    lesson_08/01_class_basics.py
    lesson_08/02_self_explained.py
    lesson_08/03_str_repr_and_formatting.py
    lesson_08/04_inheritance.py
    lesson_08/05_class_vs_instance.py
    lesson_08/06_dataclass.py
    lesson_08/07_eq_and_hash.py
    lesson_08/08_collections_and_sorting.py
    Practice: lesson_08/practice/01_classes.py, lesson_08/practice/02_eq_hash.py,
              lesson_08/practice/03_string_formatting.py


================================================================================
LESSON 9 — Modules, imports, dotenv                                        📋
================================================================================


================================================================================
LESSON 10 — JSON + blocking HTTP client                                    📋
================================================================================


================================================================================
LESSON 11 — Flask REST API server                                          🔶
================================================================================
    lesson_11/01_hello_flask.py … 06_crud_rest_service.py
    Practice: lesson_11/practice/01_rest.py


================================================================================
LESSON 12 — File I/O & XML (sync)                                         📋
================================================================================


================================================================================
LESSON 13 — Concurrency & async I/O                                        📋
================================================================================


================================================================================
LESSON 14 — Reading agents course code                                     📋
================================================================================


================================================================================
LESSON 15 — AWS Lambda & boto3 (optional)                                  📋
================================================================================


================================================================================
CROSS-CUTTING INDEX
================================================================================
    Collections          → L2    Strings (basics)     → L3
    Strings (OOP)        → L8:03 Java Streams        → L5:02, 01, 03
    equals/hashCode      → L8:07 Sorting             → L5:01; L8:08
    File / async I/O     → L12 / L13 (planned)
"""

if __name__ == "__main__":
    print(__doc__)
