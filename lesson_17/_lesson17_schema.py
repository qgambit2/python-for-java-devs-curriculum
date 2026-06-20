"""Lesson 17 — sqlite schema and DB-API helpers (no SQLAlchemy import)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

BOOKS_DDL = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL DEFAULT ''
);
"""

DEMO_DB_PATH = Path(__file__).resolve().parent / "demo_books.db"


def connect_sqlite_memory() -> sqlite3.Connection:
    """DB-API connection on :memory: with row dict access."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript(BOOKS_DDL)
    return conn
