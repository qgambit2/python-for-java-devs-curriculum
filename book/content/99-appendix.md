# Appendix — commands and files

## Project layout

| Path | Purpose |
|------|---------|
| `lesson_NN/` | Demos, `basics.py` index, `practice/` exercises |
| `lesson_NN/practice/` | Exercises with asserts |
| `00_curriculum.py` | Full roadmap |
| `.cursor/skills/python-for-java-devs/` | Tutor FAQ and Java tables |
| `book/content/` | This book's source markdown |
| `book/generate_book.py` | PDF builder |

## Essential commands

```bash
uv sync
uv sync --group book
uv run python 00_curriculum.py
uv run python lesson_02/01_collections.py
uv run python book/generate_book.py
```

## Regenerate this PDF

```bash
uv sync --group book
uv run python book/generate_book.py
```

Output: `book/output/python-for-java-devs-preview.pdf`

When lesson content changes, edit the matching file under `book/content/` — then regenerate.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [00_curriculum.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/00_curriculum.py)
- **Practice:** [lesson_02/practice/01_collections.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_02/practice/01_collections.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
