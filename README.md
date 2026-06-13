# Python for Java Developers

Hands-on Python curriculum for **expert Java developers**. Each lesson lives in one folder: demos, `basics.py` index, and `practice/` exercises.

## Layout

```
lesson_02/
  basics.py              # list / run all demos: --list
  01_collections.py
  02_slicing.py
  practice/
    01_collections.py
    02_collections.py
```

## Quick start

```bash
git clone https://github.com/qgambit2/python-for-java-devs-curriculum.git
cd python-for-java-devs-curriculum
uv sync
uv run python lesson_00/03_verify_environment.py
uv run python lesson_02/01_collections.py
```

## Roadmap

```bash
uv run python 00_curriculum.py
uv run python lesson_02/basics.py --list
```

## Read along

Chapter prose (preview edition) lives in `book/content/`.

## Java reference

See `docs/java-equivalents.md` for side-by-side Java ↔ Python tables.

## Practice

```bash
uv run python lesson_02/practice/01_collections.py
```

Fix one exercise at a time until you see checkmarks from `_check()`.

## Requirements

- Python 3.12+ (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) package manager
