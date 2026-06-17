"""Minimal Flask REST app for Lesson 16 testing demos.

Application factory — fresh in-memory store per `create_app()` call.
Same routes as lesson_11/06_crud_rest_service.py, structured for pytest.

Java parallel: @SpringBootApplication + @RestController, but you build
the app explicitly instead of component scan.
"""

from __future__ import annotations

from flask import Flask, jsonify, request


def normalize_title(title: str) -> str:
    """Hook for testing — patch this instead of Flask's request proxy."""
    return title.strip()


def create_app(*, testing: bool = False) -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = testing

    books: dict[int, dict[str, object]] = {}
    next_id = 1

    def _find(book_id: int) -> dict[str, object] | None:
        return books.get(book_id)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return jsonify({"status": "ok"}), 200

    @app.get("/books")
    def list_books() -> tuple[list[dict[str, object]], int]:
        return jsonify(list(books.values())), 200

    @app.get("/books/<int:book_id>")
    def get_book(book_id: int) -> tuple[dict[str, object] | dict[str, str], int]:
        book = _find(book_id)
        if book is None:
            return jsonify({"error": "not found"}), 404
        return jsonify(book), 200

    @app.post("/books")
    def create_book() -> tuple[dict[str, object] | dict[str, str], int]:
        nonlocal next_id
        body = request.get_json(silent=True) or {}
        title = body.get("title")
        if not title:
            return jsonify({"error": "title required"}), 400
        title = normalize_title(str(title))

        book = {"id": next_id, "title": title, "author": body.get("author", "")}
        books[next_id] = book
        next_id += 1
        return jsonify(book), 201

    @app.delete("/books/<int:book_id>")
    def delete_book(book_id: int) -> tuple[dict[str, str], int]:
        if book_id not in books:
            return jsonify({"error": "not found"}), 404
        del books[book_id]
        return jsonify({"status": "deleted"}), 200

    return app
