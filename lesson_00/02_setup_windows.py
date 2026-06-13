"""
Lesson 0b — Environment setup (Windows)
=======================================

Complete this **before Lesson 1**. Use **PowerShell** or **Windows Terminal**
(not the old `cmd.exe` unless you know what you're doing).

Java analogy: **uv** ≈ Maven/Gradle, **.venv** ≈ project JDK + classpath,
**uv run** ≈ running with the project's configured environment.


--------------------------------------------------------------------------------
1. Install uv (one-time)
--------------------------------------------------------------------------------

PowerShell (Run as your user — not necessarily Administrator):

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Close and reopen the terminal, then:

    uv --version

If the install script is blocked, see https://docs.astral.sh/uv/getting-started/installation/


--------------------------------------------------------------------------------
2. Open the project
--------------------------------------------------------------------------------

Clone or open the **python_learning** project in Cursor (or VS Code). All commands run from
the **project root** — the folder containing `pyproject.toml`.


--------------------------------------------------------------------------------
3. Create the virtual environment & install dependencies
--------------------------------------------------------------------------------

    cd C:\path\to\python_learning
    uv sync

What this does:
  - Downloads Python 3.12 if needed (see `.python-version`)
  - Creates `.venv\` in the project root
  - Installs packages from `pyproject.toml`

Requirements: Windows 10 or newer (64-bit x86_64 is Tier-1 supported).


--------------------------------------------------------------------------------
4. Run your first lesson file
--------------------------------------------------------------------------------

    uv run python lesson_01/01_syntax.py

`uv run` uses **this project's** `.venv` automatically.

Manual activation (optional):

    .venv\Scripts\activate


--------------------------------------------------------------------------------
5. Configure Cursor / VS Code
--------------------------------------------------------------------------------

Extensions (one-time):
  - Python  (ms-python.python)
  - Jupyter (ms-toolsai.jupyter) — optional

Select interpreter:
  - Command Palette → **Python: Select Interpreter**
  - Choose: `.venv\Scripts\python.exe`

On Windows, set these if the interpreter is not detected (User settings or
`.vscode/settings.json`):

    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe"
    "python.venvPath": "${workspaceFolder}"

Save before run: **Ctrl+S**.


--------------------------------------------------------------------------------
6. How to run lesson files
--------------------------------------------------------------------------------

✓  Whole file in terminal:
       uv run python lesson_NN/01_….py

✓  Right-click → **Run Python File in Terminal**

✗  Avoid **Run Selection** in a `>>>` REPL for indented blocks (`if`, `def`, `for`).


--------------------------------------------------------------------------------
7. Verify you're ready
--------------------------------------------------------------------------------

    uv run python lesson_00/03_verify_environment.py

All checks should print ✓. Then start **Lesson 1**:

    uv run python lesson_01/01_syntax.py


--------------------------------------------------------------------------------
Windows path cheat sheet
--------------------------------------------------------------------------------

| macOS / Linux              | Windows                    |
|----------------------------|----------------------------|
| `.venv/bin/python`         | `.venv\Scripts\python.exe` |
| `source .venv/bin/activate`| `.venv\Scripts\activate`   |
| `Cmd+S` save               | `Ctrl+S` save              |

Same `uv run python …` commands on every OS.

Tutor docs: `.cursor/skills/python-for-java-devs/`
"""

if __name__ == "__main__":
    print(__doc__)
