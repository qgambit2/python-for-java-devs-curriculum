"""Lesson 16c — unittest.mock ≈ Mockito (with pytest).

JUnit 5 + Mockito (typical):

    @ExtendWith(MockitoExtension.class)
    class GreeterTest {
        @Mock NameProvider provider;
        @InjectMocks Greeter greeter;

        @Test
        void greet() {
            when(provider.getName()).thenReturn("Alex");
            assertEquals("Hello, Alex!", greeter.greet());
            verify(provider).getName();
        }
    }

Python: same unittest.mock library works inside pytest tests — no @ExtendWith needed.

Run:
    uv run python lesson_16/03_mocking.py
    uv run pytest lesson_16/03_mocking.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _code_under_test import Greeter


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


section("0. Mockito ↔ unittest.mock")

print("""
| Mockito (Java)                | unittest.mock (Python)           |
|-------------------------------|----------------------------------|
| @Mock                         | MagicMock()                      |
| @InjectMocks                  | Greeter(mock_provider) manually  |
| when(x.f()).thenReturn(v)     | mock.f.return_value = v          |
| when(x.f()).thenThrow(ex)     | mock.f.side_effect = ex          |
| verify(x).f()                 | mock.f.assert_called_once()      |
| verify(x, times(2)).f()       | assert mock.f.call_count == 2    |
| ArgumentCaptor                | mock.call_args / call_args_list  |
| @MockBean / static mock       | @patch("pkg.module.name")        |
""")


section("1. when(...).thenReturn + verify — pytest test")

# JUnit 5 + Mockito:
#   when(provider.getName()).thenReturn("Alex");
#   assertEquals("Hello, Alex!", greeter.greet());
#   verify(provider).getName();


def test_greeter_with_mock() -> None:
    provider = MagicMock()
    provider.get_name.return_value = "Alex"

    greeter = Greeter(provider)
    assert greeter.greet() == "Hello, Alex!"
    provider.get_name.assert_called_once()


def test_greeter_verify_call_count() -> None:
    provider = MagicMock()
    provider.get_name.return_value = "Bob"

    Greeter(provider).greet()
    Greeter(provider).greet()

    assert provider.get_name.call_count == 2
    provider.get_name.assert_has_calls([call(), call()])


section("2. thenThrow → side_effect")


def test_greeter_provider_failure() -> None:
    provider = MagicMock()
    provider.get_name.side_effect = RuntimeError("db down")

    with pytest.raises(RuntimeError, match="db down"):
        Greeter(provider).greet()


section("3. @patch — inject mock at import site")

# Patch where the name is **used**, not where it is defined.


@patch("builtins.open")
def test_read_config_mocked(mock_open: MagicMock) -> None:
    mock_open.return_value.__enter__.return_value.read.return_value = "theme=dark"

    with open("settings.ini") as f:
        text = f.read()

    assert text == "theme=dark"
    mock_open.assert_called_once_with("settings.ini")


section("4. Demo prints (run when executing as script)")


def _demo_magic_mock() -> None:
    provider = MagicMock()
    provider.get_name.return_value = "Alex"
    result = Greeter(provider).greet()
    print(f"  greet() → {result!r}")
    provider.get_name.assert_called_once()
    print("  ✓ verify(provider).getName() equivalent")


if __name__ == "__main__":
    _demo_magic_mock()
    raise SystemExit(pytest.main([__file__, "-v", "--tb=short"] + sys.argv[1:]))
