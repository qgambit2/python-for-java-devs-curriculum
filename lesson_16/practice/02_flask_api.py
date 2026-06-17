"""
Lesson 16 — Flask API testing practice (Spring MockMvc parallel).

Read:
    lesson_11/06_crud_rest_service.py
    lesson_16/05_flask_testing.py

Replace each pytest.fail("TODO") with a real test using client fixture, then:
    uv run pytest lesson_16/practice/02_flask_api.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from flask import Flask
from flask.testing import FlaskClient

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _flask_sample_app import create_app  # noqa: E402


@pytest.fixture
def app() -> Flask:
    return create_app(testing=True)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


# Exercise 1: GET /health → 200, body {"status": "ok"}
def test_health(client: FlaskClient) -> None:
    pytest.fail("TODO: client.get('/health') — assert status and JSON")


# Exercise 2: GET /books on fresh app → 200, empty list
def test_list_empty(client: FlaskClient) -> None:
    pytest.fail("TODO")


# Exercise 3: POST /books with title → 201, id == 1, title matches
def test_create_book(client: FlaskClient) -> None:
    pytest.fail("TODO: client.post('/books', json={...})")


# Exercise 4: GET /books/999 → 404, error message
def test_get_missing(client: FlaskClient) -> None:
    pytest.fail("TODO")


# Exercise 5: POST without title → 400
def test_create_validation(client: FlaskClient) -> None:
    pytest.fail("TODO")


# Exercise 6: create two books, GET /books → list length 2
def test_list_after_creates(client: FlaskClient) -> None:
    pytest.fail("TODO")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"]))
