# Appendix — commands and files

## Project layout

| Path | Purpose |
|------|---------|
| `lesson_NN/` | Runnable lesson files |
| `lesson_NN_*_practice.py` | Exercises with asserts |
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
