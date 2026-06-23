"""Lesson 15a — Connecting to AWS with boto3 (≈ AWS SDK for Java v2).

boto3 is the AWS SDK for Python. You connect the same way from a laptop, an
EC2/ECS host, or a Lambda — what changes is only *where the credentials come
from*, never your code.

This demo runs fully offline: `moto`'s `mock_aws` intercepts the AWS calls, so
no account, no credentials, and no network are needed.

Install:
    uv sync --group aws

Run:
    uv run python lesson_15/01_connect_and_credentials.py
"""

from __future__ import annotations

import boto3
from moto import mock_aws


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Java AWS SDK v2 map")

print("""
| Java (AWS SDK for Java v2)            | Python (boto3)                      |
|---------------------------------------|--------------------------------------|
| S3Client.builder().build()            | boto3.client("s3")                  |
| DynamoDbClient.builder()...           | boto3.client("dynamodb")            |
| DefaultCredentialsProvider.create()   | default credential chain (built in) |
| Region.US_EAST_1                      | region_name="us-east-1"             |
| DynamoDbEnhancedClient (mapper)       | boto3.resource("dynamodb")          |
| software.amazon.awssdk.*              | import boto3                        |
""")


section("1. client vs resource — two API styles")

# A `client` is the low-level 1:1 mapping of the AWS API (like the Java v2
# `XxxClient`): verbs return raw dicts. A `resource` is a higher-level,
# object-oriented layer (closer to the Java *Enhanced* clients) — not every
# service has one (S3, DynamoDB, SQS, SNS do).
with mock_aws():
    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_resource = boto3.resource("s3", region_name="us-east-1")
    print("client type   :", type(s3_client).__name__)       # low-level
    print("resource type :", type(s3_resource).__name__)      # high-level
    print("rule: use a client when in doubt; resource for nicer object APIs")


section("2. Session — explicit credentials/region container")

# A Session bundles credentials + region. Most code uses the implicit default
# session (boto3.client(...)), but an explicit Session is how you pin a profile
# or region, or hold temporary assume-role credentials.
with mock_aws():
    session = boto3.Session(region_name="us-east-1")
    sts = session.client("sts")
    identity = sts.get_caller_identity()
    print("account:", identity["Account"])   # moto returns 123456789012
    print("a Session ≈ holding an SdkClient builder pre-configured with creds + region")


section("3. The credential chain — where creds come from (no hardcoding)")

# boto3 resolves credentials in this order (first hit wins) — the same idea as
# Java's DefaultCredentialsProvider:
#   1. explicit keys passed to Session/client  (avoid outside tests)
#   2. environment vars  AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
#   3. shared config      ~/.aws/credentials  (profiles)
#   4. container creds    (ECS task role)
#   5. instance/role creds (EC2 IMDS, Lambda execution role)
print("""
resolution order (first match wins):
  1. params passed to client/Session   (tests only — never commit keys)
  2. env: AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN
  3. ~/.aws/credentials profile         (local dev: aws configure)
  4. ECS container role
  5. EC2 / Lambda IAM role (IMDS)        (production: no keys on disk)
≈ Java DefaultCredentialsProvider — same chain, same 'role in prod' rule.
""")


section("4. Same code from anywhere — Lambda is just one host")

# This function does not know or care where it runs. On a laptop it uses your
# ~/.aws profile; on Lambda it uses the execution role — identical code.
def count_buckets(session: boto3.Session) -> int:
    s3 = session.client("s3")
    return len(s3.list_buckets()["Buckets"])


with mock_aws():
    session = boto3.Session(region_name="us-east-1")
    session.client("s3").create_bucket(Bucket="demo-bucket")
    print("buckets visible to this identity:", count_buckets(session))
    print("the SAME function runs on a laptop, EC2, ECS, or Lambda — only creds differ")
