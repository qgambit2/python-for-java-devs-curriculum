# Lesson 15 — AWS with boto3 (connect, S3, DynamoDB, SNS/SQS, Redis, config)

In Java you reach for the **AWS SDK for Java v2** — `S3Client`, `DynamoDbClient`, a `DefaultCredentialsProvider`. Python's equivalent is **boto3**, the official AWS SDK, and the mental model transfers almost one-to-one. The part that trips up newcomers is not the API — it is realizing that *connecting to AWS is the same from everywhere*. A script on your laptop, a service on EC2 or ECS, and a Lambda function all use identical boto3 code; the only thing that changes is **where the credentials come from**. This lesson covers that connection model first, then walks the services you will actually wire up: S3, DynamoDB, SNS/SQS, Redis (ElastiCache), and Secrets Manager / SSM for config.

**Install:**

```bash
uv sync --group aws
```

**Run** (every demo runs offline — `moto` mocks AWS, so no account or credentials needed):

```bash
uv run python lesson_15/basics.py --list
uv run python lesson_15/01_connect_and_credentials.py
uv run python lesson_15/03_dynamodb.py
```

**Prereqs:** Lesson 8 (classes), Lesson 17 (database — DynamoDB contrasts with SQL).

---

## Java SDK v2 → boto3

| Java (AWS SDK for Java v2) | Python (boto3) |
|-----------------------------|----------------|
| `S3Client.builder().build()` | `boto3.client("s3")` |
| `DynamoDbClient` / `SqsClient` | `boto3.client("dynamodb")` / `("sqs")` |
| `DefaultCredentialsProvider.create()` | the default credential chain (built in) |
| `Region.US_EAST_1` | `region_name="us-east-1"` |
| `DynamoDbEnhancedClient` (mapper) | `boto3.resource("dynamodb")` |
| `software.amazon.awssdk.*` | `import boto3` |

---

## The connection model — client vs resource

boto3 gives you two API styles. A **client** is the low-level, 1:1 mapping of the AWS API — every call returns a raw dict, exactly like the Java v2 `XxxClient`. A **resource** is a higher-level, object-oriented layer that hides some of the wire format, closer to the Java *Enhanced* clients. Not every service has a resource (S3, DynamoDB, SQS, and SNS do).

```python
import boto3

s3_client = boto3.client("s3", region_name="us-east-1")      # low-level
s3_resource = boto3.resource("s3", region_name="us-east-1")  # high-level
```

> **Java:** `boto3.client("s3")` ≈ `S3Client.builder().build()`; `boto3.resource("dynamodb")` ≈ `DynamoDbEnhancedClient`. When in doubt use a client — it exposes every operation; reach for a resource when its object API is genuinely nicer (DynamoDB `Table`, S3 `Bucket`).

A **Session** bundles credentials and region. Most code uses the implicit default session (`boto3.client(...)`), but an explicit `Session` is how you pin a named profile or hold temporary assume-role credentials.

```python
session = boto3.Session(region_name="us-east-1")
sts = session.client("sts")
print(sts.get_caller_identity()["Account"])
```

---

## Credentials — where they come from (never hardcode)

This is the heart of "how to connect." boto3 resolves credentials through a chain, first match wins — the same idea as Java's `DefaultCredentialsProvider`:

1. Keys passed explicitly to a `client`/`Session` — **tests only; never commit keys**
2. Environment: `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`
3. Shared config: `~/.aws/credentials` profiles (local dev, via `aws configure`)
4. ECS container role
5. EC2 / Lambda IAM role via the instance metadata service

```python
def count_buckets(session: boto3.Session) -> int:
    return len(session.client("s3").list_buckets()["Buckets"])
```

That function never names a credential. On your laptop it uses your `~/.aws` profile; on Lambda it uses the execution role — **identical code**.

> **Java:** the chain mirrors `DefaultCredentialsProvider` (env → profile → container → instance). The production rule is the same in both languages: attach an **IAM role**, don't ship access keys.

> **Key idea:** "Connecting to AWS" is a credentials question, not a code question. Write the call once; let the environment supply the identity. Lambda is just one more host that happens to inject a role.

---

## S3 — object storage

S3 stores opaque objects (bytes) under string keys in a bucket. There are no real folders — `data/book.json` is one flat key; the `/` is convention, and listing "a folder" means listing by **prefix**.

```python
s3 = boto3.client("s3", region_name="us-east-1")
s3.create_bucket(Bucket="reports-bucket")
s3.put_object(Bucket="reports-bucket", Key="data/book.json", Body=b"{...}")
body = s3.get_object(Bucket="reports-bucket", Key="data/book.json")["Body"].read()
```

The response `Body` is a stream — call `.read()` to get the bytes, like `getObject(...).readAllBytes()` in Java.

> **Java:** `s3.putObject(req, RequestBody.fromBytes(b))` / `s3.getObject(req).readAllBytes()`. Listing by prefix is `listObjectsV2(b -> b.prefix("data/"))`.

A **presigned URL** grants time-limited access without credentials — hand it to a browser to upload or download directly:

```python
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": "reports-bucket", "Key": "data/book.json"},
    ExpiresIn=3600,
)
```

> **Java:** `S3Presigner.presignGetObject(...)` — same purpose, time-boxed direct access.

---

## DynamoDB — managed key-value / document store

DynamoDB tables have a **partition key** (and optional **sort key**); items are schemaless maps. The `resource` API lets you pass plain dicts instead of the `{"S": "..."}` attribute-value wire format the low-level client needs.

```python
ddb = boto3.resource("dynamodb", region_name="us-east-1")
table = ddb.create_table(
    TableName="Books",
    KeySchema=[
        {"AttributeName": "author", "KeyType": "HASH"},   # partition
        {"AttributeName": "title", "KeyType": "RANGE"},    # sort
    ],
    AttributeDefinitions=[
        {"AttributeName": "author", "AttributeType": "S"},
        {"AttributeName": "title", "AttributeType": "S"},
    ],
    BillingMode="PAY_PER_REQUEST",
)
```

Reads and writes work on dicts. `put_item` is an upsert (it replaces the whole item at that key); `query` targets one partition efficiently, while `scan` reads the whole table and should be avoided.

```python
from boto3.dynamodb.conditions import Key

table.put_item(Item={"author": "Martin", "title": "Clean Code", "year": 2008})
item = table.get_item(Key={"author": "Martin", "title": "Clean Code"})["Item"]
resp = table.query(KeyConditionExpression=Key("author").eq("Martin"))
```

> **Java:** `boto3.resource("dynamodb").Table(...)` ≈ the `DynamoDbEnhancedClient` mapper; `query(KeyConditionExpression=Key("author").eq(x))` ≈ `QueryConditional.keyEqualTo(...)`. One difference to expect: numbers round-trip as Python `Decimal`, not `int` or `float`.

> **Key idea:** design around the partition key. `query` on a key is fast and cheap; `scan` is a full-table read. This is the opposite of the "just add a WHERE clause" reflex from SQL in Lesson 17.

---

## SNS + SQS — messaging

**SQS** is a queue: each message is pulled and acknowledged by one consumer. **SNS** is pub/sub fan-out: one publish reaches many subscribers. The classic pattern is **SNS → SQS** — publish once, deliver a copy to each subscribed queue.

```python
sqs = boto3.client("sqs", region_name="us-east-1")
queue_url = sqs.create_queue(QueueName="orders")["QueueUrl"]
sqs.send_message(QueueUrl=queue_url, MessageBody='{"order": 42}')

resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
for msg in resp.get("Messages", []):
    handle(msg["Body"])
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
```

A received message becomes invisible until you `delete_message` (acknowledge) or its visibility timeout expires and it reappears — **at-least-once** delivery, so make consumers idempotent.

> **Java:** `sqs.receiveMessage(...)` then `sqs.deleteMessage(...)` to ack; `sns.publish(...)` to fan out. Same at-least-once contract as the Java SDK — design for duplicate delivery.

---

## Redis / ElastiCache — the one that is not boto3

This is the important exception. On AWS you run Redis as **ElastiCache**, but you do **not** read and write keys through boto3 — boto3 only creates and describes the cluster. You talk to Redis over its own wire protocol using the **redis-py** library.

```python
import redis

r = redis.Redis(host="my-cluster.xxxx.cache.amazonaws.com", port=6379, decode_responses=True)
r.set("user:42:name", "Alice", ex=60)     # ex=60 → 60-second TTL
r.incr("page:views")                        # atomic counter
r.hset("book:1", mapping={"title": "Clean Code"})
```

> **Java:** redis-py ≈ **Jedis** or **Lettuce**, not the AWS SDK. The mental split is the same as in Java: the AWS SDK provisions ElastiCache; a Redis client library does the `GET`/`SET`/`INCR`.

> **Key idea:** the everyday use is **cache-aside** — look in Redis first, fall back to the database on a miss, then populate the cache with a TTL. It cuts read load on the DynamoDB/SQL store from Lesson 17.

---

## Secrets Manager + SSM Parameter Store — config and credentials

Where does the connection's database password come from? Not from code, and not from a committed file. Two services answer this, replacing the `application.yml` + Vault combination a Java dev knows:

- **Secrets Manager** — encrypted secrets (DB credentials, API keys), with rotation support.
- **SSM Parameter Store** — config values: free `String` parameters and KMS-encrypted `SecureString`.

```python
sm = boto3.client("secretsmanager", region_name="us-east-1")
creds = json.loads(sm.get_secret_value(SecretId="prod/db")["SecretString"])
dsn = f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}/app"

ssm = boto3.client("ssm", region_name="us-east-1")
flag = ssm.get_parameter(Name="/app/feature/new_checkout")["Parameter"]["Value"]
api_key = ssm.get_parameter(Name="/app/api_key", WithDecryption=True)["Parameter"]["Value"]
```

Fetch secrets **once at startup**, build your connection, and never log the password.

> **Java:** Secrets Manager ≈ the `SecretsManagerClient` you already use, or a Spring `@Value` backed by the AWS config provider; SSM Parameter Store ≈ externalized `application.yml` properties. `get_parameters_by_path("/app/")` hydrates a whole config tree in one call.

---

## Testing — moto mocks AWS offline

Every demo and practice file in this lesson runs with no AWS account because of **moto**. Wrap a function or block and all boto3 calls are intercepted in memory:

```python
from moto import mock_aws

@mock_aws
def test_upload():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="t")
    ...
```

> **Java:** moto ≈ **LocalStack** or the AWS SDK test utilities — a local stand-in for AWS so unit tests need no real account. It pairs naturally with the pytest patterns from Lesson 16.

---

## Pause and practice

```bash
uv run python lesson_15/practice/01_s3_dynamodb.py
uv run python lesson_15/practice/02_messaging_config.py
```

The tests create the bucket, table, queue, and secret for you and run under moto — implement each function until every `✓` check passes.

---

## On GitHub

Runnable examples and exercises in the public curriculum repository:

- **Example:** [lesson_15/01_connect_and_credentials.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_15/01_connect_and_credentials.py)
- **Example:** [lesson_15/03_dynamodb.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_15/03_dynamodb.py)
- **Practice (S3 + DynamoDB):** [lesson_15/practice/01_s3_dynamodb.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_15/practice/01_s3_dynamodb.py)
- **Practice (messaging + config):** [lesson_15/practice/02_messaging_config.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_15/practice/02_messaging_config.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
