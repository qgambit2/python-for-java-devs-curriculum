# Python for Java Developers

Hands-on Python curriculum for **expert Java developers**. Each lesson is a small runnable file; practice modules use assert-based checks.

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
```

List files in a lesson:

```bash
uv run python lesson_02_basics.py --list
```

## Read along

Chapter prose (preview edition) lives in `book/content/` — markdown you can read in GitHub or any editor. Lessons are the labs; the book explains the *why* before you run the code.

## Java reference

See `docs/java-equivalents.md` for side-by-side Java ↔ Python tables.

## Practice

```bash
uv run python lesson_02_collections_practice.py
```

Fix one exercise at a time until you see checkmarks from `_check()`.

## Requirements

- Python 3.12+ (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) package manager
