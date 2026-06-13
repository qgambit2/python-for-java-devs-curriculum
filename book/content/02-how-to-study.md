# How to study with this curriculum

Reading alone is not enough. Each chapter points at runnable files. The loop is: read a section, run the file, predict the output, then change one line and run again.

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
uv run python lesson_02_collections_practice.py
```

They use a `_check()` helper that prints a checkmark when an assertion passes. Fix one exercise at a time.

## When you are stuck

1. Ask what the Java equivalent would be.
2. Read the FAQ: `.cursor/skills/python-for-java-devs/faq.md`
3. Compare tables in `java-equivalents.md`

> **Key idea:** If you find yourself writing Java with Python punctuation, pause. There is usually a shorter, more idiomatic form — and we will collect those as you go.
