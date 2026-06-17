"""Lesson 16e — Flask API testing (≈ Spring Boot Test + MockMvc).

Prerequisites: lesson_11/ (Flask routes) · lesson_16/01–03 (pytest, fixtures, mock).

Spring:
    @WebMvcTest(BookController.class) + MockMvc
    @SpringBootTest(webEnvironment = RANDOM_PORT) + TestRestTemplate

Flask:
    pytest fixture + app.test_client()  — in-memory WSGI, no real port (≈ MockMvc)

Run:
    uv run python lesson_16/05_flask_testing.py
    uv run pytest lesson_16/05_flask_testing.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from flask import Flask
from flask.testing import FlaskClient

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _flask_sample_app import create_app


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Spring Boot Test ↔ Flask pytest")

print(r"""
| Spring Boot Test                         | Flask + pytest                    |
|------------------------------------------|-----------------------------------|
| @WebMvcTest(Controller.class)            | test only HTTP layer via client   |
| @Autowired MockMvc mockMvc               | client = app.test_client()        |
| mockMvc.perform(get("/books"))           | client.get("/books")              |
| .andExpect(status().isOk())              | assert response.status_code == 200|
| .andExpect(jsonPath("$.title").value(x)) | assert response.get_json()["title"] == x |
| @SpringBootTest (full context)           | create_app(testing=True) fixture  |
| @MockBean BookService                    | @patch("routes.module.service_fn") |
| @AutoConfigureTestDatabase               | test config / sqlite :memory: in fixture |
| TestRestTemplate (real HTTP)             | test_client preferred; or httpx to live port |

Flask has no @WebMvcTest slice annotation — you build create_app() and choose what to mock.
""")


section("1. Fixtures — @SpringBootTest ≈ create_app() per test")

print(r"""
@pytest.fixture
def app():
    return create_app(testing=True)   # fresh in-memory DB each test

@pytest.fixture
def client(app):
    return app.test_client()          # ≈ MockMvc

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
""")


@pytest.fixture
def app() -> Flask:
    """Fresh app + empty book store — like @SpringBootTest with clean context."""
    return create_app(testing=True)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


section("2. Runnable tests below — run with pytest")


def test_health(client: FlaskClient) -> None:
    # Java: mockMvc.perform(get("/health")).andExpect(status().isOk());
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_list_books_empty(client: FlaskClient) -> None:
    response = client.get("/books")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_and_get_book(client: FlaskClient) -> None:
    # Java: mockMvc.perform(post("/books").contentType(APPLICATION_JSON).content(...))
    create = client.post(
        "/books",
        json={"title": "Clean Code", "author": "Robert Martin"},
    )
    assert create.status_code == 201
    body = create.get_json()
    assert body["title"] == "Clean Code"
    assert body["id"] == 1

    fetch = client.get("/books/1")
    assert fetch.status_code == 200
    assert fetch.get_json()["author"] == "Robert Martin"


def test_get_book_not_found(client: FlaskClient) -> None:
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "not found"


def test_create_book_missing_title(client: FlaskClient) -> None:
    response = client.post("/books", json={"author": "Nobody"})
    assert response.status_code == 400
    assert "title" in response.get_json()["error"]


def test_delete_book(client: FlaskClient) -> None:
    client.post("/books", json={"title": "Temporary"})
    deleted = client.delete("/books/1")
    assert deleted.status_code == 200
    assert client.get("/books/1").status_code == 404


section("3. @MockBean — patch a dependency")

print(r"""
If a route called external_service.fetch(), stub it in the test:

    @patch("myapp.routes.external_service.fetch", return_value={"ok": True})
    def test_route(mock_fetch, client):
        r = client.get("/external")
        assert r.get_json()["ok"] is True
""")


@patch("_flask_sample_app.normalize_title", return_value="Patched Title")
def test_mock_service_layer(mock_normalize, client: FlaskClient) -> None:
    """≈ @MockBean on a service method — patch plain functions, not Flask request."""
    response = client.post("/books", json={"title": "  raw  "})

    assert response.status_code == 201
    assert response.get_json()["title"] == "Patched Title"
    mock_normalize.assert_called_once()


section("4. How to run")

print("""
uv sync --group dev
uv run pytest lesson_16/05_flask_testing.py -v
uv run pytest lesson_16/practice/02_flask_api.py -v   # after you fill in TODOs
""")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"] + sys.argv[1:]))
