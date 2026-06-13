"""
Lesson 5 practice — build a Flask REST API (stub — fill in when you reach this lesson).

Suggested project: Task API
  - GET    /tasks
  - POST   /tasks          {"title": "..."}
  - GET    /tasks/<id>
  - PUT    /tasks/<id>
  - DELETE /tasks/<id>

Run server:
    uv run python lesson_11_practice.py

Test (separate terminal, after Lesson 4):
    curl http://127.0.0.1:5001/tasks
"""

from flask import Flask

app = Flask(__name__)

# TODO: implement Task API — see lesson_11/06_crud_rest_service.py for patterns


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
