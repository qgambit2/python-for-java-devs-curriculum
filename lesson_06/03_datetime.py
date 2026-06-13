"""Lesson 1t — dates, times & calendars.

Java: java.time (LocalDate, ZonedDateTime, Duration). Python: datetime stdlib.

Run:
    uv run python lesson_06/03_datetime.py
"""

from datetime import date, datetime, timedelta, timezone


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("1. date, datetime, time — naive by default")

today = date.today()
now = datetime.now()
print(f"date.today(): {today}")
print(f"datetime.now(): {now}")
# Java: LocalDate.now(), LocalDateTime.now()


section("2. Constructing & field access")

d = date(2026, 6, 9)
print(f"{d.year}-{d.month:02d}-{d.day:02d}, weekday={d.weekday()}")  # Mon=0
# Java: LocalDate.of(2026, 6, 9); getDayOfWeek()


section("3. timedelta — duration arithmetic")

deadline = today + timedelta(days=14)
print(f"two weeks from today: {deadline}")
delta = deadline - today
print(f"days until deadline: {delta.days}")
# Java: date.plusDays(14); ChronoUnit.DAYS.between(a, b)


section("4. strftime / strptime — format & parse")

formatted = now.strftime("%Y-%m-%d %H:%M")
print(f"strftime: {formatted}")
parsed = datetime.strptime("2026-06-09 14:30", "%Y-%m-%d %H:%M")
print(f"strptime: {parsed}")
# Java: DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")


section("5. Time zones — datetime.timezone (stdlib); zoneinfo for IANA names")

utc_now = datetime.now(timezone.utc)
print(f"UTC: {utc_now.isoformat()}")

# Python 3.9+: from zoneinfo import ZoneInfo
# eastern = datetime.now(ZoneInfo("America/New_York"))
# Java: ZonedDateTime.now(ZoneId.of("America/New_York"))


section("6. Compare & sort — dates are orderable")

events = [date(2026, 1, 1), date(2026, 12, 31), date(2026, 6, 9)]
print(f"sorted events: {sorted(events)}")
