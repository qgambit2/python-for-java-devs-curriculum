"""Lesson 15b — S3 object storage with boto3 (≈ S3Client / S3 in Java v2).

S3 stores opaque objects (bytes) under string keys in a bucket — there are no
folders, only key prefixes. Runs offline under moto.

Run:
    uv run python lesson_15/02_s3.py
"""

from __future__ import annotations

import json

import boto3
from moto import mock_aws


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


BUCKET = "reports-bucket"


@mock_aws
def main() -> None:
    # @mock_aws as a decorator wraps the whole function — every boto3 call
    # inside is intercepted. (Same effect as `with mock_aws():`.)
    s3 = boto3.client("s3", region_name="us-east-1")

    section("1. Create a bucket")
    # Java: s3.createBucket(b -> b.bucket(BUCKET));
    s3.create_bucket(Bucket=BUCKET)
    print(f"created bucket: {BUCKET}")

    section("2. Put objects — bytes, text, JSON")
    # Java: s3.putObject(req, RequestBody.fromBytes(bytes));
    s3.put_object(Bucket=BUCKET, Key="raw/notes.txt", Body=b"hello s3")
    s3.put_object(
        Bucket=BUCKET,
        Key="data/book.json",
        Body=json.dumps({"title": "Clean Code", "author": "Martin"}).encode(),
        ContentType="application/json",
    )
    print("put 2 objects (raw/notes.txt, data/book.json)")

    section("3. Get an object — read the body stream")
    # Java: s3.getObject(req).readAllBytes();  (response is a stream)
    body = s3.get_object(Bucket=BUCKET, Key="data/book.json")["Body"].read()
    print("round-tripped JSON:", json.loads(body))

    section("4. List by prefix — 'folders' are just key prefixes")
    # Java: s3.listObjectsV2(b -> b.bucket(BUCKET).prefix("data/"));
    resp = s3.list_objects_v2(Bucket=BUCKET, Prefix="data/")
    keys = [obj["Key"] for obj in resp.get("Contents", [])]
    print("keys under 'data/':", keys)

    section("5. Presigned URL — time-limited direct access")
    # A presigned URL lets a browser GET/PUT without AWS credentials.
    # Java: S3Presigner.presignGetObject(...).url();
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": "raw/notes.txt"},
        ExpiresIn=3600,
    )
    print("presigned GET url starts with:", url.split("?")[0])
    print("(hand this to a client; it expires in 1 hour)")

    section("6. Delete")
    s3.delete_object(Bucket=BUCKET, Key="raw/notes.txt")
    remaining = s3.list_objects_v2(Bucket=BUCKET).get("Contents", [])
    print("objects after delete:", [o["Key"] for o in remaining])


if __name__ == "__main__":
    main()
