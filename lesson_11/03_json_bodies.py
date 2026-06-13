"""Lesson 5c — JSON request/response (≈ @RequestBody, ResponseEntity, Jackson)."""

from flask import Flask, jsonify, request

app = Flask(__name__)

_items: list[dict[str, object]] = []
_next_id = 1


@app.get("/items")
def list_items() -> tuple[list[dict[str, object]], int]:
    return jsonify(_items), 200


@app.post("/items")
def create_item() -> tuple[dict[str, object] | dict[str, str], int]:
    global _next_id
    # request.json ≈ @RequestBody Map or DTO (parsed from Content-Type: application/json)
    body = request.get_json(silent=True)
    if not body or "name" not in body:
        return jsonify({"error": "name required"}), 400

    item = {"id": _next_id, "name": body["name"]}
    _next_id += 1
    _items.append(item)
    return jsonify(item), 201


if __name__ == "__main__":
    print('Try: curl -X POST http://127.0.0.1:5001/items -H "Content-Type: application/json" -d \'{"name":"bolt"}\'')
    app.run(host="127.0.0.1", port=5001, debug=True)
