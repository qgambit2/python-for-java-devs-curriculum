"""Lesson 5b — HTTP methods on routes (≈ @GetMapping, @PostMapping, …)."""

from flask import Flask, jsonify

app = Flask(__name__)

# In-memory "database" for demos
_items: list[dict[str, object]] = [{"id": 1, "name": "widget"}]


@app.get("/items")
def list_items() -> tuple[list[dict[str, object]], int]:
    return jsonify(_items), 200


@app.post("/items")
def create_item() -> tuple[dict[str, str], int]:
    # Body handling in 03_json_bodies.py — stub for method routing
    return jsonify({"note": "POST /items — see 03_json_bodies.py"}), 501


if __name__ == "__main__":
    print("Try: curl http://127.0.0.1:5001/items")
    app.run(host="127.0.0.1", port=5001, debug=True)
