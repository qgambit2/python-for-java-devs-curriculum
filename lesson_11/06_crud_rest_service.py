"""Lesson 5f — Mini REST CRUD service (≈ Spring @RestController resource)."""

from flask import Flask, jsonify, request

app = Flask(__name__)

_books: dict[int, dict[str, object]] = {}
_next_id = 1


def _find(book_id: int) -> dict[str, object] | None:
    return _books.get(book_id)


@app.get("/books")
def list_books() -> tuple[list[dict[str, object]], int]:
    return jsonify(list(_books.values())), 200


@app.get("/books/<int:book_id>")
def get_book(book_id: int) -> tuple[dict[str, object] | dict[str, str], int]:
    book = _find(book_id)
    if book is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(book), 200


@app.post("/books")
def create_book() -> tuple[dict[str, object] | dict[str, str], int]:
    global _next_id
    body = request.get_json(silent=True) or {}
    title = body.get("title")
    if not title:
        return jsonify({"error": "title required"}), 400

    book = {"id": _next_id, "title": title, "author": body.get("author", "")}
    _books[_next_id] = book
    _next_id += 1
    return jsonify(book), 201


@app.put("/books/<int:book_id>")
def update_book(book_id: int) -> tuple[dict[str, object] | dict[str, str], int]:
    book = _find(book_id)
    if book is None:
        return jsonify({"error": "not found"}), 404

    body = request.get_json(silent=True) or {}
    if "title" in body:
        book["title"] = body["title"]
    if "author" in body:
        book["author"] = body["author"]
    return jsonify(book), 200


@app.delete("/books/<int:book_id>")
def delete_book(book_id: int) -> tuple[dict[str, str], int]:
    if book_id not in _books:
        return jsonify({"error": "not found"}), 404
    del _books[book_id]
    return jsonify({"status": "deleted"}), 200


if __name__ == "__main__":
    print("Mini REST API — test with curl or Lesson 4 requests client")
    app.run(host="127.0.0.1", port=5001, debug=True)
