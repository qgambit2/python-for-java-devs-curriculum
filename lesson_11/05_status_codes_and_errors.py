"""Lesson 5e — Status codes & error responses (≈ ResponseEntity, @ExceptionHandler)."""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/divide")
def divide() -> tuple[dict[str, object] | dict[str, str], int]:
    body = request.get_json(silent=True) or {}
    a, b = body.get("a"), body.get("b")

    if a is None or b is None:
        return jsonify({"error": "a and b required"}), 400
    if b == 0:
        return jsonify({"error": "division by zero"}), 422

    return jsonify({"result": a / b}), 200


@app.errorhandler(404)
def not_found(_error: Exception) -> tuple[dict[str, str], int]:
    # ≈ @ExceptionHandler(NoHandlerFoundException.class) or custom error controller
    return jsonify({"error": "route not found"}), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
