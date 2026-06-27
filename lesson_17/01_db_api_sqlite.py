"""Lesson 17a — DB-API 2.0 with sqlite3 (≈ JDBC).

Run:
    uv run python lesson_17/01_db_api_sqlite.py

Practice:
    uv run python lesson_17/practice/01_db_api.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from _lesson17_schema import connect_sqlite_memory


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java JDBC map")

print("""
| Java JDBC                         | Python DB-API (sqlite3)              |
|-----------------------------------|--------------------------------------|
| DriverManager.getConnection(url)  | sqlite3.connect(":memory:")          |
| Connection                        | connection object                    |
| PreparedStatement                 | cursor.execute(sql, params)          |
| ResultSet / rs.next()             | cursor.fetchone() / fetchall()       |
| setString(1, x)                   | tuple params: (x,)                   |
| try/finally conn.close()          | with conn:  (context manager)        |
| commit() / rollback()             | conn.commit() / conn.rollback()    |
""")


section("1. Connect and CREATE TABLE")

# Java:
#   Connection conn = DriverManager.getConnection("jdbc:sqlite::memory:");
#   Statement st = conn.createStatement();
#   st.execute("CREATE TABLE books (...)");
conn = connect_sqlite_memory()
print("connected — in-memory sqlite, schema created")
conn.close()


section("2. INSERT with bound parameters — never f-string SQL")

conn = connect_sqlite_memory()
# Java: PreparedStatement ps = conn.prepareStatement(
#           "INSERT INTO books (title, author) VALUES (?, ?)");
#       ps.setString(1, title); ps.setString(2, author); ps.executeUpdate();
title, author = "Clean Code", "Martin"
cursor = conn.execute(
    "INSERT INTO books (title, author) VALUES (?, ?)",
    (title, author),
)
conn.commit()
print(f"inserted id={cursor.lastrowid}")

conn.execute(
    "INSERT INTO books (title, author) VALUES (?, ?)",
    ("Effective Java", "Bloch"),
)
conn.commit()


section("3. SELECT — fetchone / fetchall")

# Java: ResultSet rs = ps.executeQuery(); while (rs.next()) { rs.getString("title"); }
row = conn.execute("SELECT id, title, author FROM books WHERE id = ?", (1,)).fetchone()
print(f"fetchone: id={row['id']} title={row['title']}")  # Row acts like dict

rows = conn.execute("SELECT title FROM books ORDER BY title").fetchall()
print("titles:", [r["title"] for r in rows])
conn.close()


section("4. Context manager — auto-close")

with connect_sqlite_memory() as conn:
    count = conn.execute("SELECT COUNT(*) AS n FROM books").fetchone()["n"]
    print(f"book count (empty db): {count}")
# conn closed


section("5. SQL injection — why ? placeholders matter")

# BAD (don't): f"SELECT * FROM books WHERE title = '{user_input}'"
# GOOD:
user_input = "Clean Code"
with connect_sqlite_memory() as conn:
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (user_input, "Martin"))
    conn.commit()
    safe = conn.execute(
        "SELECT title FROM books WHERE title = ?",
        (user_input,),
    ).fetchone()
    print(f"safe query found: {safe['title']}")
