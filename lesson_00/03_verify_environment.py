"""
Lesson 0c — Verify your environment
=====================================

Run from the **repo root** after setup:

    uv run python lesson_00/03_verify_environment.py

Every line should show ✓ before you start Lesson 1.
"""

from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path


def _check(label: str, ok: bool, hint: str = "") -> bool:
    mark = "✓" if ok else "✗"
    print(f"{mark} {label}")
    if not ok and hint:
        print(f"    → {hint}")
    return ok


def _repo_root() -> Path:
    # lesson_00/03_verify_environment.py → project root
    return Path(__file__).resolve().parents[1]


def main() -> None:
    root = _repo_root()
    venv_dir = root / ".venv"
    pyproject = root / "pyproject.toml"
    python_version = root / ".python-version"

    print("=" * 60)
    print("Lesson 0 — environment verification")
    print("=" * 60)
    print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Repo root: {root}")
    print()

    ok = True
    ok &= _check(
        "Python 3.12+",
        sys.version_info >= (3, 12),
        f"got {sys.version_info.major}.{sys.version_info.minor} — run `uv sync` from repo root",
    )
    ok &= _check(
        "pyproject.toml at repo root",
        pyproject.is_file(),
        "run this script from the project root (folder with pyproject.toml)",
    )
    ok &= _check(
        ".python-version pins 3.12",
        python_version.is_file() and python_version.read_text().strip().startswith("3.12"),
        "expected `.python-version` with 3.12",
    )
    ok &= _check(
        ".venv/ exists (run `uv sync` first)",
        venv_dir.is_dir(),
        "from repo root: `uv sync`",
    )

    in_venv = hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ok &= _check(
        "Interpreter is the project venv",
        in_venv and str(venv_dir) in Path(sys.prefix).resolve().as_posix(),
        "use `uv run python …` or select .venv interpreter in Cursor",
    )

    try:
        uv_version = subprocess.run(
            ["uv", "--version"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        ok &= _check("uv on PATH", True)
        print(f"    {uv_version}")
    except (FileNotFoundError, subprocess.CalledProcessError):
        ok &= _check(
            "uv on PATH",
            False,
            "install: https://docs.astral.sh/uv/getting-started/installation/",
        )

    ok &= _check(
        "Can import a project dependency (flask)",
        _try_import("flask"),
        "run `uv sync` from repo root",
    )

    lesson1 = root / "lesson_01" / "01_syntax.py"
    ok &= _check("Lesson 1 files present", lesson1.is_file())

    print()
    if ok:
        print("All checks passed — start Lesson 1:")
        print("    uv run python lesson_01/01_syntax.py")
    else:
        print("Fix the ✗ items above, then re-run this script.")
        if platform.system() == "Windows":
            print("Setup guide: uv run python lesson_00/02_setup_windows.py")
        else:
            print("Setup guide: uv run python lesson_00/01_setup_mac_linux.py")
        sys.exit(1)


def _try_import(module: str) -> bool:
    try:
        __import__(module)
        return True
    except ImportError:
        return False


if __name__ == "__main__":
    main()
