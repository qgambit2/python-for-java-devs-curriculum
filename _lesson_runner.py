"""Shared helper for lesson_NN/basics.py index runners."""

from __future__ import annotations

from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).parent


def run_lesson_index(lesson_files: list[str], *, lesson_dir: Path) -> None:
    rel_dir = lesson_dir.relative_to(ROOT)
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        for name in lesson_files:
            print(f"uv run python {rel_dir}/{name}")
        return

    for name in lesson_files:
        path = lesson_dir / name
        print(f"\n{'=' * 60}")
        print(f"Running {path.relative_to(ROOT)}")
        print("=" * 60)
        runpy.run_path(str(path), run_name="__main__")
