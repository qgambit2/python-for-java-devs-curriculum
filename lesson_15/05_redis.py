"""Lesson 15e — Redis / ElastiCache with redis-py (≈ Jedis / Lettuce).

IMPORTANT: Redis is NOT a boto3 service. On AWS you run it as **ElastiCache**
(managed Redis), but you talk to it over the Redis wire protocol with the
**redis-py** library — boto3 only creates/describes the cluster, it never reads
or writes keys. This is the one service in this lesson you do not call through
boto3.

This demo uses `fakeredis` so it runs offline. Against real ElastiCache you would
write `redis.Redis(host="my-cluster.xxxx.cache.amazonaws.com", port=6379)`.

Run:
    uv run python lesson_15/05_redis.py
"""

from __future__ import annotations

import fakeredis


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


def main() -> None:
    # Real code:  r = redis.Redis(host=..., port=6379, decode_responses=True)
    # Java:       Jedis jedis = new Jedis(host, port);   (or Lettuce RedisClient)
    r = fakeredis.FakeStrictRedis(decode_responses=True)

    section("1. Strings + TTL — the cache-aside pattern")
    # Java: jedis.setex("key", 60, "value");
    r.set("user:42:name", "Alice", ex=60)   # ex=60 → expires in 60s
    print("get:", r.get("user:42:name"))
    print("ttl seconds:", r.ttl("user:42:name"))

    section("2. Atomic counter — INCR")
    # Java: jedis.incr("page:views");
    r.delete("page:views")
    r.incr("page:views")
    r.incrby("page:views", 5)
    print("page:views =", r.get("page:views"))   # "6"

    section("3. Hash — store a small object as fields")
    # Java: jedis.hset("book:1", map);
    r.hset("book:1", mapping={"title": "Clean Code", "author": "Martin"})
    print("hgetall:", r.hgetall("book:1"))
    print("one field:", r.hget("book:1", "title"))

    section("4. List — queue / recent-items")
    # Java: jedis.lpush / jedis.rpop
    r.delete("recent")
    r.lpush("recent", "a", "b", "c")    # pushes c, b, a to the head
    print("range:", r.lrange("recent", 0, -1))
    print("rpop (oldest):", r.rpop("recent"))

    section("5. Cache-aside helper — the everyday use")
    calls = {"db": 0}

    def load_book(book_id: str) -> dict:
        key = f"book:cache:{book_id}"
        cached = r.hgetall(key)
        if cached:
            return cached                      # cache hit
        calls["db"] += 1                        # cache miss → hit the DB
        book = {"title": "Refactoring", "author": "Fowler"}
        r.hset(key, mapping=book)
        r.expire(key, 300)
        return book

    load_book("99")   # miss
    load_book("99")   # hit
    print("DB reads for 2 loads (should be 1):", calls["db"])


if __name__ == "__main__":
    main()
