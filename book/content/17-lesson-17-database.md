# Lesson 17 — Database access (DB-API, SQLAlchemy, Flask)

Java **JDBC** (direct SQL) and **JPA/Hibernate** (ORM) map to Python in **layers** — there is no single stdlib ORM.

**Install:**

```bash
uv sync
```

**Run:**

```bash
uv run python lesson_17/basics.py --list
uv run python lesson_17/01_db_api_sqlite.py
uv run python lesson_17/06_transactions.py
uv run python lesson_17/04_sqlalchemy_orm.py
```

**Prereqs:** Lesson 8 (classes), Lesson 11 (Flask CRUD), Lesson 16 (sqlite `:memory:` in tests).

---

## Java → Python stack

| Layer | Java | Python |
|-------|------|--------|
| Driver API | JDBC | **DB-API 2.0** (`sqlite3`, `psycopg`) |
| Connection pool / URL | `DataSource`, HikariCP | **SQLAlchemy `Engine`** |
| SQL-first | `JdbcTemplate` | **SQLAlchemy Core** |
| ORM | JPA `EntityManager` | **SQLAlchemy ORM** `Session` |
| Migrations | Flyway / Liquibase | **Alembic** |
| REST + DB | Spring Data JPA | Flask + SQLAlchemy session per request |

---

## DB-API — sqlite3 ≈ JDBC

```java
Connection conn = DriverManager.getConnection(url);
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO books (title, author) VALUES (?, ?)");
ps.setString(1, title);
ps.executeUpdate();
conn.close();
```

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute(
    "INSERT INTO books (title, author) VALUES (?, ?)",
    (title, author),
)
conn.commit()
row = conn.execute("SELECT title FROM books WHERE id = ?", (id,)).fetchone()
```

| Java JDBC | Python DB-API |
|-----------|---------------|
| `?` placeholders | `?` placeholders (same) |
| `ResultSet` | `fetchone()` / `fetchall()` |
| `try/finally close` | `with conn:` |

**Rule:** never build SQL with f-strings or `+` for user input — SQL injection. Always bind parameters.

---

## Transactions

A transaction is a unit of work that is **all-or-nothing**: either every statement commits together or none of them do. In Java this is so familiar it is almost invisible — JDBC opens a connection in `autoCommit = true`, so each statement is its own transaction unless you call `conn.setAutoCommit(false)`, and Spring hides the whole thing behind `@Transactional`.

Python's DB-API works the **opposite way around**, and that difference trips up Java developers on day one.

> **Java:** JDBC defaults to *auto-commit on* — every `executeUpdate` is committed immediately. You opt **out** with `setAutoCommit(false)`, then `commit()` / `rollback()` yourself, usually inside a `try/catch`.

> **Key idea:** `sqlite3` defaults to *auto-commit off* — a transaction opens implicitly before the first data-modifying statement and stays open until **you** call `commit()`. Forget the `commit()` and your INSERT silently vanishes when the connection closes. This is the single most common "my row didn't save" bug for Java devs.

### The `with conn:` idiom

The idiomatic fix is to let the connection's context manager own the transaction boundary:

```python
with conn:                       # commits on success, rolls back on exception
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.execute("UPDATE stats SET book_count = book_count + 1")
# both statements committed together; either both land or neither does
```

When the block exits cleanly the connection commits; if an exception propagates out of the block it rolls back. Note the subtlety that trips up Java developers expecting try-with-resources: `with conn:` commits or rolls back but does **not** close the connection. (`sqlite3` connections are never closed by a `with` block — not even `with sqlite3.connect(...) as conn:`; call `conn.close()` yourself or wrap it in `contextlib.closing`.)

> **Java:** `with conn:` ≈ Spring's `@Transactional` — the happy path commits, any thrown exception rolls back. You write the business logic; the boundary handles commit/rollback.

### Explicit commit and rollback

When you need finer control — partial commits, savepoints, or a `try/except` that decides per-error — drive it by hand, exactly like JDBC with auto-commit disabled:

```python
try:
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.execute("INSERT INTO authors (name) VALUES (?)", (author,))
    conn.commit()                # both rows persist atomically
except sqlite3.IntegrityError:
    conn.rollback()             # neither row persists
    raise
```

| Java JDBC | Python DB-API |
|-----------|---------------|
| `setAutoCommit(false)` | (default — transaction already open) |
| `conn.commit()` | `conn.commit()` |
| `conn.rollback()` | `conn.rollback()` |
| `@Transactional` method | `with conn:` block |
| `Connection.TRANSACTION_SERIALIZABLE` | `isolation_level` / `PRAGMA` |

### Transactions in the ORM

SQLAlchemy gives you the same two styles. The `Session` tracks pending changes and flushes them on `commit()`; `engine.begin()` wraps a block the way `with conn:` does:

```python
with Session(engine) as session:
    session.add(Book(title="Clean Code"))
    session.add(Book(title="Refactoring"))
    session.commit()             # one transaction; rollback() on error

with engine.begin() as conn:     # Core: commit on success, rollback on exception
    conn.execute(text("UPDATE books SET title = :t WHERE id = :id"),
                 {"t": "Clean Code 2e", "id": 1})
```

> **Java:** `Session` ≈ JPA `EntityManager` + its persistence context — `add()` stages, `commit()` flushes and commits, `rollback()` discards. `engine.begin()` ≈ `TransactionTemplate.execute(...)`.

> **Key idea:** never leave a transaction implicitly open across a web request or a long pause — an idle open transaction holds locks. Commit or roll back promptly, and in Flask use one `Session` per request (see below).

---

## Migrations

**Alembic** versions schema changes (≈ Flyway / Liquibase):

```bash
alembic revision -m "add column"
alembic upgrade head
```

Lesson demo: `lesson_17/02_schema_and_migrations.py`. Transaction demo (commit, rollback, `with conn:`, savepoints): `lesson_17/06_transactions.py`.

---

## SQLAlchemy Core — explicit SQL

```python
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")
with engine.begin() as conn:                 # begin() = transaction that auto-commits on success
    conn.execute(text("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)"))
    conn.execute(text("INSERT INTO books (title) VALUES (:t)"), {"t": "Hi"})
    rows = conn.execute(text("SELECT title FROM books")).all()
    print([r.title for r in rows])           # ['Hi']
```

≈ **JdbcTemplate** — SQL you control (`text()` is raw SQL with `:name` binds), less JDBC boilerplate. Mapped entities like `Book` belong to the ORM section below, not here.

---

## SQLAlchemy ORM — ≈ JPA

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

with Session(engine) as session:
    book = Book(title="Clean Code")
    session.add(book)      # persist
    session.commit()
    found = session.get(Book, 1)   # find by id
```

| JPA | SQLAlchemy ORM |
|-----|----------------|
| `@Entity` | `class Book(Base)` |
| `persist` | `session.add()` + `commit()` |
| `find` | `session.get(Book, id)` |
| JPQL | `select(Book).where(...)` |

---

## Flask + database

Lesson 11 used an in-memory `dict`. Lesson 17 replaces it with a **file sqlite** DB and a `Session` per request:

```bash
uv run python lesson_17/05_flask_sqlalchemy.py
curl http://127.0.0.1:5002/books
```

Use `sqlite:///:memory:` for unit tests; use a file URL when the server must persist between HTTP requests.

---

## Pause and practice

```bash
uv run python lesson_17/practice/01_db_api.py
uv run python lesson_17/practice/02_sqlalchemy_crud.py
```

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_17/01_db_api_sqlite.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/01_db_api_sqlite.py)
- **Example (transactions):** [lesson_17/06_transactions.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/06_transactions.py)
- **Example:** [lesson_17/04_sqlalchemy_orm.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/04_sqlalchemy_orm.py)
- **Practice (DB-API):** [lesson_17/practice/01_db_api.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/practice/01_db_api.py)
- **Practice (ORM):** [lesson_17/practice/02_sqlalchemy_crud.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/practice/02_sqlalchemy_crud.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
