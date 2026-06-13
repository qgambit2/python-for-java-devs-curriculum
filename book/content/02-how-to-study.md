# How to study with this curriculum

Reading alone is not enough. Each chapter points at runnable files. The loop is: read a section, run the file, predict the output, then change one line and run again.

## Repo layout

Each lesson lives in one folder:

```
lesson_02/
  basics.py              # uv run python lesson_02/basics.py --list
  01_collections.py
  02_slicing.py
  practice/
    01_collections.py
```

Full roadmap:

```bash
uv run python 00_curriculum.py
```

## Your environment

From the project root (where `pyproject.toml` lives):

```bash
uv sync
uv run python lesson_00/03_verify_environment.py
```

Point Cursor's Python interpreter at `.venv/bin/python`.

## How to run a lesson

```bash
uv run python lesson_02/01_collections.py
```

Run the **whole file** in the terminal. Avoid pasting indented blocks into a `>>>` REPL in the IDE — it breaks easily.

Save files before running. The editor buffer and the file on disk can differ.

## Practice files

After the lesson files, open the practice modules:

```bash
uv run python lesson_02/practice/01_collections.py
```

They use a `_check()` helper that prints a checkmark when an assertion passes. Fix one exercise at a time. Round 2 for Lesson 2:

```bash
uv run python lesson_02/practice/02_collections.py
```

## Study loop (repeat every section)

1. Read one `##` section in this book or the lesson file comments.
2. Run the matching demo file before scrolling output.
3. Predict the next printed line, then verify.
4. Change one line in the lesson file and re-run.
5. Open practice only after the demos make sense.

> **Java:** Treat each `lesson_NN/*.py` like a JShell script you execute top-to-bottom — not a class to compile in isolation.

## When you are stuck

1. Ask what the Java equivalent would be.
2. Read the FAQ: `.cursor/skills/python-for-java-devs/faq.md`
3. Compare tables in `java-equivalents.md`

> **Key idea:** If you find yourself writing Java with Python punctuation, pause. There is usually a shorter, more idiomatic form — and we will collect those as you go.
