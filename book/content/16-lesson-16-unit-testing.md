# Lesson 16 — Unit testing (JUnit 5 and pytest)

Capstone lesson — verify functions, classes, and modules the way you do in Java with **JUnit 5** + **Mockito**. In Python the default stack is **pytest** + **`unittest.mock`**.

**Install (once):**

```bash
uv sync --group dev
```

**Run:**

```bash
uv run python lesson_16/basics.py --list
uv run pytest lesson_16/01_pytest_junit5.py -v
```

---

## JUnit 5 test class — side by side

**Java (`src/test/java`):**

```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Arithmetic")
class ArithmeticTest {

    @Test
    void add() {
        assertEquals(5, add(2, 3));
    }

    @Test
    void divideByZero() {
        assertThrows(ZeroDivisionError.class, () -> divide(1, 0));
    }

    @Test
    void clampEdges() {
        assertAll(
            () -> assertEquals(0, clamp(-5, 0, 10)),
            () -> assertEquals(10, clamp(99, 0, 10))
        );
    }
}
```

**Python (pytest) — same ideas, less boilerplate:**

```python
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)

def test_clamp_edges():
    assert clamp(-5, 0, 10) == 0
    assert clamp(99, 0, 10) == 10
```

Discovery: `test_*.py` files and `test_*` functions. Run: `uv run pytest`.

---

## JUnit 5 ↔ pytest map

| JUnit 5 | pytest |
|---------|--------|
| `@Test` | `def test_*():` |
| `assertEquals(expected, actual)` | `assert actual == expected` |
| `assertTrue` / `assertFalse` | `assert condition` |
| `assertNull` / `assertNotNull` | `assert x is None` / `is not None` |
| `assertThrows(Ex.class, () -> …)` | `with pytest.raises(Ex): …` |
| `assertAll(() -> …, () -> …)` | multiple `assert` lines in one test |
| `@BeforeEach` | `@pytest.fixture` (default scope = per test) |
| `@BeforeAll` | `@pytest.fixture(scope="module")` |
| `@ParameterizedTest` + `@CsvSource` | `@pytest.mark.parametrize` |
| `@Disabled` | `@pytest.mark.skip` |
| `@ExtendWith(MockitoExtension.class)` | pass `MagicMock()` into constructor |
| `mvn test` | `uv run pytest` |

---

## @ParameterizedTest

**Java:**

```java
@ParameterizedTest
@CsvSource({"2, 3, 5", "0, 0, 0", "-1, 1, 0"})
void add(int a, int b, int want) {
    assertEquals(want, add(a, b));
}
```

**Python:**

```python
@pytest.mark.parametrize("a,b,want", [(2, 3, 5), (0, 0, 0), (-1, 1, 0)])
def test_add_cases(a, b, want):
    assert add(a, b) == want
```

---

## @BeforeEach → fixture

**Java:**

```java
class ScoreBoardTest {
    private ScoreBoard board;

    @BeforeEach
    void setUp() {
        board = new ScoreBoard();
        board.add("alice", 10);
    }

    @Test
    void aliceScore() {
        assertEquals(10, board.get("alice"));
    }
}
```

**Python:**

```python
@pytest.fixture
def board():
    b = ScoreBoard()
    b.add("alice", 10)
    return b

def test_alice_score(board):
    assert board.get("alice") == 10
```

`yield` in a fixture adds teardown after the test — like `@AfterEach`.

---

## Mockito → unittest.mock

**Java:**

```java
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
```

**Python (pytest test):**

```python
from unittest.mock import MagicMock

def test_greeter():
    provider = MagicMock()
    provider.get_name.return_value = "Alex"
    assert Greeter(provider).greet() == "Hello, Alex!"
    provider.get_name.assert_called_once()
```

`@patch("mymodule.open")` on a test parameter replaces a name where it is imported — same rule as Mockito + Spring: patch the **lookup site**.

---

## Project layout

```
myapp/
  bank.py
tests/
  test_bank.py
```

Or colocated: `bank.py` + `test_bank.py`.

---

## Flask REST — Spring Boot Test / MockMvc

After **Lesson 11** (Flask routes). Sample app: `lesson_16/_flask_sample_app.py` (application factory).

| Spring Boot Test | Flask + pytest |
|------------------|----------------|
| `@WebMvcTest` + `MockMvc` | `client = app.test_client()` |
| `mockMvc.perform(get("/books"))` | `client.get("/books")` |
| `.andExpect(status().isOk())` | `assert response.status_code == 200` |
| `.andExpect(jsonPath("$.title").value("x"))` | `assert response.get_json()["title"] == "x"` |
| `@SpringBootTest` | `create_app(testing=True)` in a fixture |
| `@MockBean BookService` | `@patch("myapp.module.service_fn")` |

**Java:**

```java
@WebMvcTest(BookController.class)
class BookControllerTest {
    @Autowired MockMvc mockMvc;

    @Test
    void createBook() throws Exception {
        mockMvc.perform(post("/books")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"title\":\"Dune\"}"))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.title").value("Dune"));
    }
}
```

**Python:**

```python
@pytest.fixture
def app():
    return create_app(testing=True)

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_book(client):
    response = client.post("/books", json={"title": "Dune"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Dune"
```

`test_client` hits your app **in memory** (no real port) — closest to `MockMvc`.

> **Tip:** patch your **service functions**, not Flask's `request` object (it's a request-context proxy and breaks `@patch`).

Run: `uv run pytest lesson_16/05_flask_testing.py -v`

---

## Legacy: unittest (JUnit 4 shape)

stdlib `unittest.TestCase` exists in older code — `self.assertEqual`, `setUp`. See `lesson_16/04_unittest_legacy.py`. **Do not start new projects with it** — use pytest.

---

## Pause and practice

```bash
uv run pytest lesson_16/practice/01_write_tests.py -v
uv run pytest lesson_16/practice/02_flask_api.py -v
```

Replace each `pytest.fail("TODO")` with a real test.

---

## On GitHub

- **Example:** [lesson_16/05_flask_testing.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_16/05_flask_testing.py)
- **Practice (pytest):** [lesson_16/practice/01_write_tests.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_16/practice/01_write_tests.py)
- **Practice (Flask API):** [lesson_16/practice/02_flask_api.py](https://github.com/qgambit2/python-for-java-devs-curriculum/blob/main/lesson_16/practice/02_flask_api.py)
- **Repository:** [https://github.com/qgambit2/python-for-java-devs-curriculum](https://github.com/qgambit2/python-for-java-devs-curriculum)
