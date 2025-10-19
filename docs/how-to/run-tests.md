# How to Run Tests

This guide covers testing strategies for the FastAPI application.

## Quick Start

Run all tests:

```bash
make test
```

Run with verbose output:

```bash
pytest -v
```

Run specific test file:

```bash
pytest tests/test_routes.py -v
```

## Test Structure

Tests are located in the `tests/` directory:

```
tests/
├── __init__.py
└── test_routes.py
```

## Running Tests

### Using Make

The simplest way:

```bash
make test
```

### Using pytest Directly

```bash
# All tests
pytest

# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf

# Run specific test
pytest tests/test_routes.py::test_hello -v
```

### With Coverage

Install coverage:

```bash
uv add --dev pytest-cov
```

Run with coverage report:

```bash
pytest --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html
```

Generate terminal coverage report:

```bash
pytest --cov=app --cov-report=term-missing
```

## Writing Tests

### Basic Test Structure

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoint():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert "message" in response.json()
```

### Testing Different HTTP Methods

#### GET Request

```python
def test_get_request():
    response = client.get("/api/users/123")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 123
```

#### POST Request

```python
def test_post_request():
    payload = {
        "username": "testuser",
        "email": "test@example.com"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"
```

#### PUT Request

```python
def test_put_request():
    payload = {"username": "updated"}
    response = client.put("/api/users/123", json=payload)
    assert response.status_code == 200
```

#### DELETE Request

```python
def test_delete_request():
    response = client.delete("/api/users/123")
    assert response.status_code == 200
    assert response.json()["deleted"] is True
```

### Testing Query Parameters

```python
def test_query_parameters():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Agent!"
```

### Testing Headers

```python
def test_with_headers():
    headers = {"Authorization": "Bearer token123"}
    response = client.get("/api/secure", headers=headers)
    assert response.status_code == 200
```

### Testing Error Cases

```python
def test_not_found():
    response = client.get("/api/users/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_validation_error():
    payload = {"username": ""}  # Invalid empty username
    response = client.post("/api/users", json=payload)
    assert response.status_code == 422
```

## Using Fixtures

### Basic Fixture

```python
import pytest

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "email": "test@example.com"
    }

def test_create_user(test_user):
    response = client.post("/api/users", json=test_user)
    assert response.status_code == 201
```

### Database Fixture (Future Use)

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///./test.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    # Cleanup
    os.remove("test.db")
```

### Application Fixture

```python
@pytest.fixture
def app():
    from app.main import app
    return app

@pytest.fixture
def client(app):
    return TestClient(app)

def test_with_fixture(client):
    response = client.get("/")
    assert response.status_code == 200
```

## Test Organization

### Grouping Tests with Classes

```python
class TestUserEndpoints:
    def test_create_user(self):
        response = client.post("/api/users", json={
            "username": "test"
        })
        assert response.status_code == 201
    
    def test_get_user(self):
        response = client.get("/api/users/1")
        assert response.status_code == 200

class TestAuthEndpoints:
    def test_login(self):
        response = client.post("/api/login", json={
            "username": "test",
            "password": "pass"
        })
        assert response.status_code == 200
```

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("name,expected", [
    ("Alice", "Hello, Alice!"),
    ("Bob", "Hello, Bob!"),
    ("", "Hello, World!"),  # Default value
])
def test_hello_parametrized(name, expected):
    url = f"/api/hello?name={name}" if name else "/api/hello"
    response = client.get(url)
    assert response.json()["message"] == expected
```

## Async Tests

For async endpoints:

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/hello")
    assert response.status_code == 200
```

Install pytest-asyncio:

```bash
uv add --dev pytest-asyncio
```

## Mocking

### Mock External API Calls

```python
from unittest.mock import patch, MagicMock

@patch('app.services.external_api.get_data')
def test_with_mock(mock_get_data):
    mock_get_data.return_value = {"data": "mocked"}
    
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.json()["data"] == "mocked"
    mock_get_data.assert_called_once()
```

### Mock Database

```python
@patch('app.database.get_user')
def test_mock_database(mock_get_user):
    mock_get_user.return_value = {
        "id": 1,
        "username": "test"
    }
    
    response = client.get("/api/users/1")
    assert response.status_code == 200
```

## Test Configuration

### pytest.ini or pyproject.toml

Add to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
```

### Mark Tests

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    # Long-running test
    pass

@pytest.mark.integration
def test_integration():
    # Integration test
    pass
```

Run specific markers:

```bash
# Run only slow tests
pytest -m slow

# Skip slow tests
pytest -m "not slow"
```

## Continuous Integration

### GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install uv
          uv sync
      - name: Run tests
        run: make test
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

## Best Practices

1. **Test naming**: Use descriptive names (`test_user_creation_with_valid_data`)
2. **One assertion per test**: Focus each test on one behavior
3. **AAA pattern**: Arrange, Act, Assert
4. **Independent tests**: Tests should not depend on each other
5. **Fast tests**: Mock external dependencies
6. **Clean up**: Use fixtures to clean up test data
7. **Coverage**: Aim for >80% code coverage
8. **Test edge cases**: Empty values, boundary conditions, errors

## Example: Complete Test Suite

```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestHelloEndpoint:
    """Tests for the /api/hello endpoint."""
    
    def test_hello_default(self):
        """Test hello endpoint with default name."""
        response = client.get("/api/hello")
        assert response.status_code == 200
        assert response.json()["message"] == "Hello, World!"
    
    def test_hello_with_name(self):
        """Test hello endpoint with custom name."""
        response = client.get("/api/hello?name=Agent")
        assert response.status_code == 200
        assert response.json()["message"] == "Hello, Agent!"
    
    @pytest.mark.parametrize("name,expected", [
        ("Alice", "Hello, Alice!"),
        ("123", "Hello, 123!"),
        ("test@example.com", "Hello, test@example.com!"),
    ])
    def test_hello_various_names(self, name, expected):
        """Test hello endpoint with various name formats."""
        response = client.get(f"/api/hello?name={name}")
        assert response.status_code == 200
        assert response.json()["message"] == expected

class TestRootEndpoint:
    """Tests for the root endpoint."""
    
    def test_root_success(self):
        """Test root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        assert "Welcome" in response.json()["message"]
```

## Troubleshooting

### Tests Not Found

Ensure:
- Test files start with `test_`
- Test functions start with `test_`
- You're in the project root directory

### Import Errors

```bash
# Add project to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest
```

### Slow Tests

Use pytest-xdist for parallel testing:

```bash
uv add --dev pytest-xdist
pytest -n auto
```

## See Also

- [API Reference](../reference/endpoints.md)
- [How to Add Endpoints](add-endpoint.md)
- [Architecture](../explanation/architecture.md)
