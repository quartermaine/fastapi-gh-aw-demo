# API Reference

Complete technical reference for the FastAPI GH AW Demo application.

## Table of Contents

- [Application Entry Point](#application-entry-point)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Data Models](#data-models)
- [Testing Utilities](#testing-utilities)

---

## Application Entry Point

### `app.main`

Main FastAPI application module.

#### `app`

**Type**: `FastAPI`

The main FastAPI application instance.

**Attributes**:

- `title`: `"FastAPI GH-AW Demo"`
- `version`: `"0.1.0"`

**Example**:

```python
from app.main import app
```

#### `root()`

**Endpoint**: `GET /`

**Description**: Returns a welcome message.

**Parameters**: None

**Returns**:

```python
{
    "message": str  # Welcome message
}
```

**Response Example**:

```json
{
    "message": "Welcome to the FastAPI GH AW Demo!"
}
```

**Status Codes**:

- `200 OK`: Successful response

---

## API Endpoints

### Module: `app.api.routes`

API routes are organized under the `/api` prefix with the `demo` tag.

#### `router`

**Type**: `APIRouter`

**Configuration**:

- `prefix`: `/api`
- `tags`: `["demo"]`

### Endpoints

#### `hello(name: str = "World")`

**Endpoint**: `GET /api/hello`

**Description**: Returns a personalized greeting.

**Query Parameters**:

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `name` | `str` | `"World"` | No | Name to greet |

**Returns**:

```python
{
    "message": str  # Greeting message
}
```

**Response Example**:

```json
{
    "message": "Hello, Developer!"
}
```

**Status Codes**:

- `200 OK`: Successful response

**Usage Examples**:

```bash
# Default greeting
curl http://localhost:8000/api/hello

# Custom name
curl http://localhost:8000/api/hello?name=Developer
```

```python
import httpx

response = httpx.get("http://localhost:8000/api/hello", params={"name": "Developer"})
print(response.json())
# {"message": "Hello, Developer!"}
```

---

## Configuration

### Module: `app.core.config`

Application configuration management.

#### `Settings`

**Description**: Configuration settings class.

**Attributes**:

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `APP_NAME` | `str` | `"FastAPI GH-AW Demo"` | Application name |
| `ENV` | `str` | `"development"` | Environment (development/production) |

**Environment Variables**:

- `ENV`: Override the environment setting

**Example**:

```python
from app.core.config import settings

print(settings.APP_NAME)  # "FastAPI GH-AW Demo"
print(settings.ENV)       # "development" or value from ENV environment variable
```

#### `settings`

**Type**: `Settings`

**Description**: Global settings instance.

**Usage**:

```python
from app.core.config import settings

if settings.ENV == "production":
    # Production-specific configuration
    pass
```

---

## Data Models

Currently, the application uses simple dictionary responses. For applications requiring structured data validation, define Pydantic models:

### Example Model Definition

```python
from pydantic import BaseModel, Field

class GreetingResponse(BaseModel):
    """Response model for greeting endpoints."""
    message: str = Field(..., description="The greeting message")

class GreetingRequest(BaseModel):
    """Request model for creating greetings."""
    name: str = Field("World", description="Name to greet", min_length=1, max_length=100)
```

### Using Models in Endpoints

```python
@router.get("/hello", response_model=GreetingResponse)
def hello(name: str = "World") -> GreetingResponse:
    return GreetingResponse(message=f"Hello, {name}!")
```

---

## Testing Utilities

### Module: `tests.test_routes`

Test suite for API endpoints.

#### `client`

**Type**: `TestClient`

**Description**: FastAPI test client for making test requests.

**Usage**:

```python
from tests.test_routes import client

response = client.get("/")
assert response.status_code == 200
```

### Test Functions

#### `test_root()`

**Description**: Tests the root endpoint.

**Assertions**:

- Response status code is 200
- Response contains "Welcome" in the message

**Source**:

```python
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]
```

#### `test_hello()`

**Description**: Tests the hello endpoint with a custom name.

**Assertions**:

- Response status code is 200
- Response message matches expected format

**Source**:

```python
def test_hello():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Agent!"}
```

---

## CLI Entry Point

### Module: `main`

Command-line interface entry point.

#### `main()`

**Description**: Prints a hello message.

**Usage**:

```bash
python main.py
```

**Output**:

```
Hello from fastapi-gh-aw-demo!
```

**Source**:

```python
def main():
    print("Hello from fastapi-gh-aw-demo!")

if __name__ == "__main__":
    main()
```

---

## Development Commands (Makefile)

### `make run`

Runs the development server with auto-reload.

**Command**: `uvicorn app.main:app --reload`

### `make test`

Runs the test suite with verbose output.

**Command**: `pytest -v`

### `make lint`

Checks code style and quality.

**Command**: `ruff check app tests`

### `make format`

Auto-fixes code style issues.

**Command**: `ruff check --fix app tests`

---

## Interactive Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

**URL**: `http://localhost:8000/docs`

**Features**:

- Interactive API exploration
- Try-it-out functionality
- Request/response examples
- Schema visualization

### ReDoc

**URL**: `http://localhost:8000/redoc`

**Features**:

- Clean, readable documentation
- Downloadable OpenAPI spec
- Code samples in multiple languages

### OpenAPI Schema

**URL**: `http://localhost:8000/openapi.json`

**Description**: Raw OpenAPI 3.0 specification in JSON format.

---

## HTTP Status Codes

The application uses standard HTTP status codes:

| Code | Meaning | Usage |
|------|---------|-------|
| `200` | OK | Successful GET/POST requests |
| `422` | Unprocessable Entity | Validation error in request data |
| `500` | Internal Server Error | Unexpected server error |

---

## Response Formats

All responses are JSON-formatted with `Content-Type: application/json`.

### Success Response

```json
{
    "message": "Response data"
}
```

### Error Response (Validation)

```json
{
    "detail": [
        {
            "loc": ["query", "name"],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

---

## Dependencies

From `pyproject.toml`:

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | ≥0.119.0 | Web framework |
| `uvicorn` | ≥0.38.0 | ASGI server |
| `httpx` | ≥0.28.1 | HTTP client for testing |
| `pytest` | ≥8.4.2 | Testing framework |
| `ruff` | ≥0.14.1 | Code formatter and linter |

### Python Version

**Required**: Python ≥3.12

---

## Type Hints

The application uses Python type hints throughout for better IDE support and type checking.

### Example

```python
def hello(name: str = "World") -> dict[str, str]:
    return {"message": f"Hello, {name}!"}
```

### Running Type Checks (Optional)

Install and run `mypy` for static type checking:

```bash
pip install mypy
mypy app tests
```

---

## See Also

- [Getting Started Tutorial](./tutorial.md) - Learn by building
- [How-To Guides](./how-to-guides.md) - Practical task guides
- [Architecture Explanation](./explanation.md) - Design and concepts
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Official FastAPI docs
