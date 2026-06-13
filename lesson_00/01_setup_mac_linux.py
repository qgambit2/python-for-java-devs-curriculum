"""
Lesson 0a — Environment setup (macOS & Linux)
=============================================

Complete this **before Lesson 1**. You need: a terminal, this repo on disk,
and about 10 minutes.

Java analogy: **uv** ≈ Maven/Gradle (deps + run), **.venv** ≈ project JDK +
classpath, **uv run** ≈ `mvn exec:java` with the right environment.


--------------------------------------------------------------------------------
1. Install uv (one-time)
--------------------------------------------------------------------------------

macOS / Linux — paste in Terminal:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Restart the terminal (or `source` your shell rc file), then:

    uv --version

Alternatives: `brew install uv` (macOS), or see https://docs.astral.sh/uv/


--------------------------------------------------------------------------------
2. Open the project
--------------------------------------------------------------------------------

Clone or open the **python_learning** project in Cursor (or VS Code). All commands below
run from the **project root** — the folder that contains `pyproject.toml`.


--------------------------------------------------------------------------------
3. Create the virtual environment & install dependencies
--------------------------------------------------------------------------------

    cd /path/to/python_learning
    uv sync

What this does:
  - Downloads Python 3.12 if needed (see `.python-version`)
  - Creates `.venv/` in the project root
  - Installs packages from `pyproject.toml` (Flask, httpx, … for later lessons)

You do **not** need a separate `python.org` install if uv manages Python for you.


--------------------------------------------------------------------------------
4. Run your first lesson file
--------------------------------------------------------------------------------

    uv run python lesson_01/01_syntax.py

`uv run` always uses **this project's** `.venv` — no `source .venv/bin/activate`
required (though activation still works if you prefer).


--------------------------------------------------------------------------------
5. Configure Cursor / VS Code
--------------------------------------------------------------------------------

Extensions (one-time):
  - Python  (ms-python.python)
  - Jupyter (ms-toolsai.jupyter) — optional, for notebooks elsewhere in the course

Select interpreter:
  - Command Palette → **Python: Select Interpreter**
  - Choose: `.venv/bin/python`  (under the project folder)

This repo's `.vscode/settings.json` already points at that path on macOS/Linux.

Save before run: **Cmd+S** — the editor buffer is not the file on disk.


--------------------------------------------------------------------------------
6. How to run lesson files (do this, not Run Selection)
--------------------------------------------------------------------------------

✓  Whole file in terminal:
       uv run python lesson_NN/01_….py

✓  Right-click → **Run Python File in Terminal**

✗  Avoid **Run Selection** in a `>>>` REPL for `if` / `def` / `for` blocks —
   indented code often breaks in the terminal REPL.


--------------------------------------------------------------------------------
7. Verify you're ready
--------------------------------------------------------------------------------

    uv run python lesson_00/03_verify_environment.py

All checks should print ✓. Then start **Lesson 1**:

    uv run python lesson_01/01_syntax.py


--------------------------------------------------------------------------------
Quick reference
--------------------------------------------------------------------------------

| Task              | Command |
|-------------------|---------|
| Install deps      | `uv sync` |
| Run a script      | `uv run python path/to/file.py` |
| List Lesson 2 files | `uv run python lesson_02/basics.py --list` |
| Full curriculum   | `uv run python 00_curriculum.py` |

Tutor docs: `.cursor/skills/python-for-java-devs/` (SKILL.md, faq.md)
"""

if __name__ == "__main__":
    print(__doc__)
