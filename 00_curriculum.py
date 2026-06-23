"""
Python for Java Developers — full curriculum
==========================================

One folder per lesson. Files numbered 01_, 02_, … in teaching order.
Each lesson folder may also contain basics.py (index runner) and practice/ exercises.

Status: ✅ done  ·  🔶 partial  ·  📋 planned

    uv run python 00_curriculum.py
    uv run python lesson_00/basics.py --list
    uv run python lesson_02/basics.py --list

Tutor docs: .claude/skills/python-for-java-devs/


================================================================================
LESSON 0 — Environment setup (macOS / Linux / Windows)                     ✅
================================================================================
    lesson_00/01_setup_mac_linux.py   — install uv, uv sync, editor setup, how to run
    lesson_00/02_setup_windows.py   — same for Windows paths & PowerShell
    lesson_00/03_verify_environment.py — ✓ checklist before Lesson 1

    Start here if you are new. Run verify:
        uv run python lesson_00/03_verify_environment.py


================================================================================
LESSON 1 — Syntax & variables                                              ✅
================================================================================
    lesson_01/01_syntax.py
    lesson_01/02_variables.py
    lesson_01/03_control_flow.py   — if/for/while/match (Java control flow)
    Practice: lesson_01/practice/01_practice.py
               lesson_01/practice/02_control_flow.py


================================================================================
LESSON 2 — Collections (list, dict, tuple, set) & slicing                    ✅
================================================================================
    lesson_02/01_collections.py
    lesson_02/02_slicing.py
    lesson_02/03_collections_stdlib.py
    lesson_02/04_heapq.py
    Practice: lesson_02/practice/01_collections.py, lesson_02/practice/02_collections.py
              lesson_02/practice/03_collections_stdlib.py, lesson_02/practice/04_heapq.py


================================================================================
LESSON 3 — Strings: operations & formatting                                ✅
================================================================================
    lesson_03/01_strings.py
    Practice: lesson_03/practice/01_strings.py
               lesson_03/practice/02_string_ops.py  (incl. re ex 11–12)


================================================================================
LESSON 4 — Loops, truthiness, functions                                    ✅
================================================================================
    lesson_04/01_loops.py
    lesson_04/02_truthiness.py
    lesson_04/03_functions.py


================================================================================
LESSON 5 — Builtins, comprehensions, functional style                      ✅
================================================================================
    lesson_05/01_builtins.py
    lesson_05/02_comprehensions.py
    lesson_05/03_functional_style.py
    Practice: lesson_05/practice/01_builtins.py, lesson_05/practice/02_builtins.py
               lesson_05/practice/03_comprehensions.py


================================================================================
LESSON 6 — Types, math, datetime, recursion                                ✅
================================================================================
    lesson_06/01_types_and_datatypes.py
    lesson_06/02_math_and_numbers.py
    lesson_06/03_datetime.py
    lesson_06/04_recursion.py
    Practice: lesson_06/practice/ (planned)   📋 planned


================================================================================
LESSON 7 — Java gotchas, pythonic style, cheat sheet                       ✅
================================================================================
    lesson_07/01_java_gotchas.py
    lesson_07/02_pythonic_compactness.py
    lesson_07/03_cheat_sheet.py


================================================================================
LESSON 8 — Classes, OOP & dataclasses                                      🔶
================================================================================
    lesson_08/01_class_basics.py
    lesson_08/02_self_explained.py
    lesson_08/03_str_repr_and_formatting.py
    lesson_08/04_inheritance.py
    lesson_08/05_class_vs_instance.py
    lesson_08/06_dataclass.py
    lesson_08/07_eq_and_hash.py
    lesson_08/08_collections_and_sorting.py
    lesson_08/09_ordered_dict_lru.py
    Practice: lesson_08/practice/01_classes.py, lesson_08/practice/02_eq_hash.py,
              lesson_08/practice/03_string_formatting.py


================================================================================
LESSON 9 — Modules, imports, dotenv                                        📋
================================================================================


================================================================================
LESSON 10 — JSON + blocking HTTP client                                    📋
================================================================================


================================================================================
LESSON 11 — Flask REST API server                                          🔶
================================================================================
    lesson_11/01_hello_flask.py … 06_crud_rest_service.py
    Practice: lesson_11/practice/01_rest.py


================================================================================
LESSON 12 — File I/O & XML (sync)                                         📋
================================================================================


================================================================================
LESSON 13 — Concurrency & async I/O                                        📋
================================================================================


================================================================================
LESSON 14 — Reading agents course code                                     📋
================================================================================


================================================================================
LESSON 15 — AWS with boto3 (S3, DynamoDB, SNS/SQS, Redis, config)           ✅
================================================================================
    lesson_15/01_connect_and_credentials.py — Session, client vs resource, cred chain
    lesson_15/02_s3.py                  — buckets, objects, presigned URLs
    lesson_15/03_dynamodb.py            — partition/sort keys, put/get/query
    lesson_15/04_sns_sqs.py             — queues, pub/sub, SNS→SQS fan-out
    lesson_15/05_redis.py               — ElastiCache via redis-py (not boto3)
    lesson_15/06_secrets_and_config.py  — Secrets Manager + SSM Parameter Store
    Practice: lesson_15/practice/01_s3_dynamodb.py
               lesson_15/practice/02_messaging_config.py

    Install: uv sync --group aws   (boto3, moto, redis, fakeredis)
    Run:     uv run python lesson_15/basics.py --list
    Note:    every demo runs offline — moto mocks AWS, fakeredis mocks Redis
    Java:    boto3 ≈ AWS SDK for Java v2; cred chain ≈ DefaultCredentialsProvider


================================================================================
LESSON 16 — Unit testing (JUnit 5 / pytest, Mockito)                       ✅
================================================================================
    lesson_16/01_pytest_junit5.py           — @Test, assert, assertThrows
    lesson_16/02_fixtures_and_parametrize.py — @BeforeEach, @ParameterizedTest
    lesson_16/03_mocking.py                 — Mockito / unittest.mock
    lesson_16/04_unittest_legacy.py         — JUnit 4 / unittest (legacy only)
    lesson_16/05_flask_testing.py           — Flask test_client ≈ MockMvc
    Practice: lesson_16/practice/01_write_tests.py
               lesson_16/practice/02_flask_api.py

    Install: uv sync --group dev
    Run:     uv run pytest lesson_16/ -v


================================================================================
LESSON 17 — Database access (DB-API, SQLAlchemy, Flask)                     🔶
================================================================================
    lesson_17/01_db_api_sqlite.py       — sqlite3 ≈ JDBC
    lesson_17/02_schema_and_migrations.py — DDL, transactions; Alembic ≈ Flyway
    lesson_17/03_sqlalchemy_core.py     — Engine, text(), explicit SQL
    lesson_17/04_sqlalchemy_orm.py      — declarative models, Session ≈ JPA
    lesson_17/05_flask_sqlalchemy.py    — Flask CRUD with SQLAlchemy (port 5002)
    lesson_17/06_transactions.py        — commit/rollback, with conn:, SAVEPOINT
    Practice: lesson_17/practice/01_db_api.py
               lesson_17/practice/02_sqlalchemy_crud.py

    Deps: sqlalchemy (uv sync) · sqlite3 is stdlib
    Prereqs: L8 (classes), L11 (Flask), L16 (sqlite :memory: tests)


================================================================================
CROSS-CUTTING INDEX
================================================================================
    Collections          → L2    Strings (basics)     → L3
    Strings (OOP)        → L8:03 Java Streams        → L5:02, 01, 03
    equals/hashCode      → L8:07 Sorting             → L5:01; L8:08
    File / async I/O     → L12 / L13 (planned)
    Unit testing         → L16   (JUnit 5 / pytest / Mockito)
    Database (JDBC/JPA)  → L17   (DB-API / SQLAlchemy)
"""

if __name__ == "__main__":
    print(__doc__)
