"""
Lesson 15 — SQS + Secrets Manager practice (boto3, mocked with moto).

Read first:
    lesson_15/04_sns_sqs.py
    lesson_15/06_secrets_and_config.py

Fill in each function, then run:
    uv run python lesson_15/practice/02_messaging_config.py

Notes:
  - The tests create the queue and secret for you and pass them in.
  - Messages are JSON strings; parse them with json.loads.
"""

import json
import sys
from pathlib import Path

_p = Path(__file__).resolve().parent
while not (_p / "_lesson_runner.py").is_file():
    _p = _p.parent
if str(_p) not in sys.path:
    sys.path.insert(0, str(_p))


# Exercise 1: Send `payload` (a dict) to the queue as JSON. Return the MessageId.
def send_event(sqs_client, queue_url: str, payload: dict) -> str:
    pass


# Exercise 2: Receive ALL messages, delete (ack) each, and return the parsed
# bodies as a list of dicts. (Use MaxNumberOfMessages up to 10.)
def drain_queue(sqs_client, queue_url: str) -> list[dict]:
    pass


# Exercise 3: Read the secret by name and return it parsed into a dict.
def read_secret(secrets_client, name: str) -> dict:
    pass


# ---------------------------------------------------------------------------
# Tests — don't edit below
# ---------------------------------------------------------------------------
import boto3
from moto import mock_aws

from _test_helpers import check, check_eq


@mock_aws
def _run_tests() -> None:
    sqs = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs.create_queue(QueueName="practice-events")["QueueUrl"]

    mid = send_event(sqs, queue_url, {"order": 1})
    check(isinstance(mid, str) and len(mid) > 0, "send_event returns a MessageId")
    send_event(sqs, queue_url, {"order": 2})

    drained = drain_queue(sqs, queue_url)
    check_eq(sorted(d["order"] for d in drained), [1, 2], "drain_queue — both messages")
    check_eq(drain_queue(sqs, queue_url), [], "drain_queue — empty after ack")

    sm = boto3.client("secretsmanager", region_name="us-east-1")
    sm.create_secret(Name="prac/db", SecretString=json.dumps({"user": "app", "pw": "x"}))
    check_eq(read_secret(sm, "prac/db"), {"user": "app", "pw": "x"}, "read_secret — parsed dict")

    print("\nAll tests passed! Messaging + config practice complete.")


if __name__ == "__main__":
    _run_tests()
