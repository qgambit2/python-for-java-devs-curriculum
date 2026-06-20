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

## Transactions and migrations

```python
conn.execute("BEGIN")
conn.execute("INSERT INTO books ...", (...))
conn.commit()    # or conn.rollback()
```

**Alembic** versions schema changes (≈ Flyway):

```bash
alembic revision -m "add column"
alembic upgrade head
```

Lesson demo: `lesson_17/02_schema_and_migrations.py`.

---

## SQLAlchemy Core — explicit SQL

```python
from sqlalchemy import create_engine, text, select

engine = create_engine("sqlite:///:memory:")
with engine.connect() as conn:
    conn.execute(text("INSERT INTO books (title) VALUES (:t)"), {"t": "Hi"})
    conn.commit()
    rows = conn.execute(select(Book.title)).all()
```

≈ **JdbcTemplate** — SQL you control, less JDBC boilerplate.

---

## SQLAlchemy ORM — ≈ JPA

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

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
- **Example:** [lesson_17/04_sqlalchemy_orm.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/04_sqlalchemy_orm.py)
- **Practice (DB-API):** [lesson_17/practice/01_db_api.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/practice/01_db_api.py)
- **Practice (ORM):** [lesson_17/practice/02_sqlalchemy_crud.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_17/practice/02_sqlalchemy_crud.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
