"""Lesson 15d — SNS + SQS messaging with boto3 (≈ SnsClient / SqsClient).

SQS is a queue (one consumer group pulls each message). SNS is pub/sub fan-out
(one publish → many subscribers). The classic pattern is SNS → SQS: publish once,
deliver to many queues. Runs offline under moto.

Run:
    uv run python lesson_15/04_sns_sqs.py
"""

from __future__ import annotations

import json

import boto3
from moto import mock_aws


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


@mock_aws
def main() -> None:
    sqs = boto3.client("sqs", region_name="us-east-1")
    sns = boto3.client("sns", region_name="us-east-1")

    section("1. SQS — create a queue and send a message")
    # Java: sqs.createQueue(b -> b.queueName("orders"));
    queue_url = sqs.create_queue(QueueName="orders")["QueueUrl"]
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps({"order": 42}))
    print("sent message to queue:", queue_url.rsplit("/", 1)[-1])

    section("2. SQS — receive and delete (the consumer loop)")
    # Java: sqs.receiveMessage(...); then sqs.deleteMessage(...) to ack.
    # A message stays invisible after receive until you delete it (ack) or the
    # visibility timeout expires and it reappears — at-least-once delivery.
    resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    for msg in resp.get("Messages", []):
        print("received:", json.loads(msg["Body"]))
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
        print("deleted (acked) the message")

    section("3. SNS — create a topic")
    # Java: sns.createTopic(b -> b.name("book-events"));
    topic_arn = sns.create_topic(Name="book-events")["TopicArn"]
    print("created topic:", topic_arn.rsplit(":", 1)[-1])

    section("4. SNS → SQS fan-out — subscribe a queue to a topic")
    # Publish once to the topic; every subscribed queue gets a copy.
    fanout_url = sqs.create_queue(QueueName="book-events-consumer")["QueueUrl"]
    queue_arn = sqs.get_queue_attributes(
        QueueUrl=fanout_url, AttributeNames=["QueueArn"]
    )["Attributes"]["QueueArn"]
    sns.subscribe(TopicArn=topic_arn, Protocol="sqs", Endpoint=queue_arn)
    print("subscribed queue to topic")

    section("5. Publish — one publish reaches the subscriber")
    # Java: sns.publish(b -> b.topicArn(arn).message(json));
    sns.publish(TopicArn=topic_arn, Message=json.dumps({"event": "book_added", "id": 7}))
    delivered = sqs.receive_message(QueueUrl=fanout_url, MaxNumberOfMessages=10)
    for msg in delivered.get("Messages", []):
        # SNS wraps the payload in an envelope; the original is under "Message".
        envelope = json.loads(msg["Body"])
        print("fan-out delivered:", json.loads(envelope["Message"]))


if __name__ == "__main__":
    main()
