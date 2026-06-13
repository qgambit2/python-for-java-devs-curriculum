"""Lesson 5d — Path variables & query params (≈ @PathVariable, @RequestParam)."""

from flask import Flask, jsonify, request

app = Flask(__name__)

_users: dict[int, dict[str, object]] = {
    1: {"id": 1, "name": "alice"},
    2: {"id": 2, "name": "bob"},
}


@app.get("/users/<int:user_id>")
def get_user(user_id: int) -> tuple[dict[str, object] | dict[str, str], int]:
    # <int:user_id> ≈ @GetMapping("/users/{userId}")
    user = _users.get(user_id)
    if user is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(user), 200


@app.get("/users")
def search_users() -> tuple[list[dict[str, object]], int]:
    # request.args ≈ @RequestParam — /users?q=ali
    q = request.args.get("q", "").lower()
    results = [u for u in _users.values() if q in str(u["name"]).lower()]
    return jsonify(results), 200


if __name__ == "__main__":
    print("Try: curl http://127.0.0.1:5001/users/1")
    print("     curl 'http://127.0.0.1:5001/users?q=ali'")
    app.run(host="127.0.0.1", port=5001, debug=True)
