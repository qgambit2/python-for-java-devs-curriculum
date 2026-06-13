"""Lesson 5a — Hello Flask (≈ minimal Spring Boot app + one @GetMapping)."""

from flask import Flask, jsonify

# Flask app ≈ Spring Boot application context (much smaller)
app = Flask(__name__)


@app.get("/")
def hello() -> tuple[dict[str, str], int]:
    # Return JSON — like @RestController returning a Map or DTO
    return jsonify({"message": "Hello from Flask"}), 200


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # Dev server only — use gunicorn/waitress in production (≈ embedded Tomcat vs prod deploy)
    print("Open http://127.0.0.1:5001/ and http://127.0.0.1:5001/health")
    print("Ctrl+C to stop")
    app.run(host="127.0.0.1", port=5001, debug=True)
