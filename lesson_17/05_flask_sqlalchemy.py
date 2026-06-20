"""Lesson 17e — Flask REST + SQLAlchemy (replaces in-memory dict from Lesson 11).

Run (starts server on port 5002):
    uv run python lesson_17/05_flask_sqlalchemy.py

Test:
    curl http://127.0.0.1:5002/books
"""

from __future__ import annotations

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from flask import Flask, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import Session

from _lesson17_db import DEMO_DB_PATH, Book, book_to_dict, make_engine, seed_books

# File-backed sqlite so data survives between HTTP requests (unlike :memory:)
_db_url = f"sqlite:///{DEMO_DB_PATH}"
engine = make_engine(_db_url)

app = Flask(__name__)


def _session() -> Session:
    return Session(engine)


@app.get("/books")
def list_books() -> tuple[list[dict[str, object]], int]:
    with _session() as session:
        seed_books(session)
        books = session.scalars(select(Book).order_by(Book.id)).all()
        return jsonify([book_to_dict(b) for b in books]), 200


@app.get("/books/<int:book_id>")
def get_book(book_id: int) -> tuple[dict[str, object] | dict[str, str], int]:
    with _session() as session:
        book = session.get(Book, book_id)
        if book is None:
            return jsonify({"error": "not found"}), 404
        return jsonify(book_to_dict(book)), 200


@app.post("/books")
def create_book() -> tuple[dict[str, object] | dict[str, str], int]:
    body = request.get_json(silent=True) or {}
    title = body.get("title")
    if not title:
        return jsonify({"error": "title required"}), 400

    with _session() as session:
        book = Book(title=title, author=body.get("author", ""))
        session.add(book)
        session.commit()
        session.refresh(book)
        return jsonify(book_to_dict(book)), 201


@app.delete("/books/<int:book_id>")
def delete_book(book_id: int) -> tuple[dict[str, str], int]:
    with _session() as session:
        book = session.get(Book, book_id)
        if book is None:
            return jsonify({"error": "not found"}), 404
        session.delete(book)
        session.commit()
        return jsonify({"status": "deleted"}), 200


if __name__ == "__main__":
    print(f"Flask + SQLAlchemy — DB file: {DEMO_DB_PATH}")
    print("curl http://127.0.0.1:5002/books")
    app.run(host="127.0.0.1", port=5002, debug=True)
