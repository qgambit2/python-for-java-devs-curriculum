"""Lesson 15c — DynamoDB with boto3 (≈ DynamoDbClient / Enhanced client).

DynamoDB is a managed key-value / document store. Every table has a partition
key (and optional sort key); items are schemaless JSON-ish maps. Runs offline
under moto.

Run:
    uv run python lesson_15/03_dynamodb.py
"""

from __future__ import annotations

import boto3
from boto3.dynamodb.conditions import Key
from moto import mock_aws


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


@mock_aws
def main() -> None:
    # The `resource` API (≈ DynamoDB Enhanced client) lets you work with plain
    # Python dicts instead of the verbose {"S": "..."} attribute-value wire
    # format the low-level client requires.
    ddb = boto3.resource("dynamodb", region_name="us-east-1")

    section("1. Create a table — partition key + sort key")
    # Books keyed by author (partition) + title (sort).
    # Java: dynamoDb.createTable(builder with KeySchema + AttributeDefinitions)
    table = ddb.create_table(
        TableName="Books",
        KeySchema=[
            {"AttributeName": "author", "KeyType": "HASH"},   # partition key
            {"AttributeName": "title", "KeyType": "RANGE"},    # sort key
        ],
        AttributeDefinitions=[
            {"AttributeName": "author", "AttributeType": "S"},
            {"AttributeName": "title", "AttributeType": "S"},
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    table.wait_until_exists()
    print("created table: Books (author HASH, title RANGE)")

    section("2. put_item — upsert a whole item")
    # Java: table.putItem(book);   put_item REPLACES the item at that key.
    table.put_item(Item={"author": "Martin", "title": "Clean Code", "year": 2008})
    table.put_item(Item={"author": "Martin", "title": "Clean Coder", "year": 2011})
    table.put_item(Item={"author": "Bloch", "title": "Effective Java", "year": 2018})
    print("put 3 items")

    section("3. get_item — fetch by full primary key")
    # Java: table.getItem(Key.builder()...);
    item = table.get_item(Key={"author": "Martin", "title": "Clean Code"})["Item"]
    print("got:", item)   # numbers come back as Decimal

    section("4. query — all items for one partition key")
    # query hits the partition key (efficient); scan reads the whole table (avoid).
    # Java: table.query(QueryConditional.keyEqualTo(...))
    resp = table.query(KeyConditionExpression=Key("author").eq("Martin"))
    titles = [i["title"] for i in resp["Items"]]
    print("Martin's books (sorted by sort key):", titles)

    section("5. update_item — change one attribute in place")
    # Java: table.updateItem(...);  SET expression updates without rewriting the item.
    table.update_item(
        Key={"author": "Bloch", "title": "Effective Java"},
        UpdateExpression="SET edition = :e",
        ExpressionAttributeValues={":e": 3},
    )
    updated = table.get_item(Key={"author": "Bloch", "title": "Effective Java"})["Item"]
    print("after update:", updated)

    section("6. delete_item")
    table.delete_item(Key={"author": "Martin", "title": "Clean Coder"})
    left = table.query(KeyConditionExpression=Key("author").eq("Martin"))["Items"]
    print("Martin's books after delete:", [i["title"] for i in left])


if __name__ == "__main__":
    main()
