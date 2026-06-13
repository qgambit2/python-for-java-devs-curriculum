"""Shared helper for lesson_XX_basics.py index runners."""

from __future__ import annotations

from pathlib import Path
import runpy
import sys


def run_lesson_index(lesson_num: int, lesson_files: list[str]) -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        for name in lesson_files:
            print(f"uv run python lesson_{lesson_num:02d}/{name}")
        return

    lesson_dir = Path(__file__).parent / f"lesson_{lesson_num:02d}"
    for name in lesson_files:
        path = lesson_dir / name
        print(f"\n{'=' * 60}")
        print(f"Running {path.relative_to(Path(__file__).parent)}")
        print("=" * 60)
        runpy.run_path(str(path), run_name="__main__")
