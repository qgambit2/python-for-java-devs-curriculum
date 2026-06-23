"""Lesson 15f — Secrets Manager + SSM Parameter Store (≈ Spring config / Vault).

How a connection actually gets its DB password and config without hardcoding:
  - Secrets Manager: encrypted secrets (DB creds, API keys), supports rotation.
  - SSM Parameter Store: config values; free-tier `String` + encrypted `SecureString`.

Both replace the "where do the credentials/config come from" question that Java
devs answer with application.yml + a secrets backend (Vault / AWS). Runs offline
under moto.

Run:
    uv run python lesson_15/06_secrets_and_config.py
"""

from __future__ import annotations

import json

import boto3
from moto import mock_aws


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


@mock_aws
def main() -> None:
    section("1. Secrets Manager — store a JSON secret")
    sm = boto3.client("secretsmanager", region_name="us-east-1")
    # Java: secretsClient.createSecret(b -> b.name("prod/db").secretString(json));
    sm.create_secret(
        Name="prod/db",
        SecretString=json.dumps({"username": "app", "password": "s3cr3t", "host": "db.internal"}),
    )
    print("stored secret: prod/db")

    section("2. Read it back at startup — build a connection string")
    # Java: secretsClient.getSecretValue(b -> b.secretId("prod/db")).secretString();
    raw = sm.get_secret_value(SecretId="prod/db")["SecretString"]
    creds = json.loads(raw)
    dsn = f"postgresql://{creds['username']}:***@{creds['host']}/app"
    print("resolved DSN (password masked):", dsn)
    print("rule: fetch once at startup; never log the password")

    section("3. SSM Parameter Store — plain config values")
    ssm = boto3.client("ssm", region_name="us-east-1")
    # Java: ssmClient.putParameter(b -> b.name("/app/...").value(...).type(STRING));
    ssm.put_parameter(Name="/app/feature/new_checkout", Value="true", Type="String")
    ssm.put_parameter(Name="/app/max_retries", Value="3", Type="String")
    flag = ssm.get_parameter(Name="/app/feature/new_checkout")["Parameter"]["Value"]
    print("feature flag new_checkout:", flag)

    section("4. SecureString — encrypted parameter")
    # SecureString is KMS-encrypted at rest; WithDecryption=True returns plaintext.
    ssm.put_parameter(Name="/app/api_key", Value="key-abc-123", Type="SecureString")
    key = ssm.get_parameter(Name="/app/api_key", WithDecryption=True)["Parameter"]["Value"]
    print("decrypted api_key:", key)

    section("5. Load a whole config tree by path")
    # get_parameters_by_path pulls every key under a prefix — one call to hydrate config.
    # Java: ssmClient.getParametersByPath(b -> b.path("/app/").recursive(true));
    page = ssm.get_parameters_by_path(Path="/app/", Recursive=True, WithDecryption=True)
    config = {p["Name"]: p["Value"] for p in page["Parameters"]}
    print("loaded config keys:", sorted(config))


if __name__ == "__main__":
    main()
