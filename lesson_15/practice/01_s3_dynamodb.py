"""
Lesson 15 — S3 + DynamoDB practice (boto3, mocked with moto).

Read first:
    lesson_15/02_s3.py
    lesson_15/03_dynamodb.py

Fill in each function, then run:
    uv run python lesson_15/practice/01_s3_dynamodb.py

Notes:
  - The tests create the bucket and table for you and pass them in.
  - DynamoDB numbers come back as decimal.Decimal — compare with int(...) if needed.
"""

import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))

from boto3.dynamodb.conditions import Key


# Exercise 1: Put `data` (bytes) into the bucket under `key`. Return the key.
def upload_object(s3_client, bucket: str, key: str, data: bytes) -> str:
    pass


# Exercise 2: Return the sorted list of object keys under `prefix` in the bucket.
def list_keys(s3_client, bucket: str, prefix: str) -> list[str]:
    pass


# Exercise 3: Save a book item (author, title, year) into the table.
def save_book(table, author: str, title: str, year: int) -> None:
    pass


# Exercise 4: Return the list of titles for one author, in sort-key order.
def titles_for_author(table, author: str) -> list[str]:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import boto3
from moto import mock_aws

from _test_helpers import check_eq


@mock_aws
def _run_tests() -> None:
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="practice")

    check_eq(upload_object(s3, "practice", "docs/a.txt", b"hi"), "docs/a.txt", "upload_object returns key")
    upload_object(s3, "practice", "docs/b.txt", b"yo")
    upload_object(s3, "practice", "img/c.png", b"\x89")
    check_eq(list_keys(s3, "practice", "docs/"), ["docs/a.txt", "docs/b.txt"], "list_keys — prefix filter")

    ddb = boto3.resource("dynamodb", region_name="us-east-1")
    table = ddb.create_table(
        TableName="PracticeBooks",
        KeySchema=[
            {"AttributeName": "author", "KeyType": "HASH"},
            {"AttributeName": "title", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "author", "AttributeType": "S"},
            {"AttributeName": "title", "AttributeType": "S"},
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    table.wait_until_exists()

    save_book(table, "Martin", "Clean Code", 2008)
    save_book(table, "Martin", "Clean Coder", 2011)
    save_book(table, "Bloch", "Effective Java", 2018)
    check_eq(titles_for_author(table, "Martin"), ["Clean Code", "Clean Coder"], "titles_for_author — sorted")
    check_eq(titles_for_author(table, "Bloch"), ["Effective Java"], "titles_for_author — single")

    print("\nAll tests passed! S3 + DynamoDB practice complete.")


if __name__ == "__main__":
    _run_tests()
