# API Reference

Complete technical reference for the FastAPI GH-AW Demo API.

## Table of Contents

- [Application](#application)
- [Endpoints](#endpoints)
  - [Root Endpoints](#root-endpoints)
  - [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Project Modules](#project-modules)
- [Development Commands](#development-commands)

---

## Application

### FastAPI Application Instance

**Location**: `app/main.py`

```python
app = FastAPI(title="FastAPI GH-AW Demo", version="0.1.0")
```

**Properties**:
- `title`: "FastAPI GH-AW Demo"
- `version`: "0.1.0"
- `docs_url`: `/docs` (Swagger UI)
- `redoc_url`: `/redoc` (ReDoc documentation)

---

## Endpoints

### Root Endpoints

#### GET /

Returns a welcome message.

**Path**: `/`

**Method**: `GET`

**Authentication**: None required

**Query Parameters**: None

**Request Body**: None

**Response**: 

```json
{
  "message": "Welcome to the FastAPI GH AW Demo!"
}
```

**Status Codes**:
- `200 OK`: Success

**Example**:

```bash
curl http://localhost:8000/
```

**Response Example**:

```json
{
  "message": "Welcome to the FastAPI GH AW Demo!"
}
```

---

### API Endpoints

All API endpoints are prefixed with `/api` and tagged as `demo`.

#### GET /api/hello

Returns a greeting message with an optional custom name.

**Path**: `/api/hello`

**Method**: `GET`

**Authentication**: None required

**Query Parameters**:

| Parameter | Type   | Required | Default | Description           |
|-----------|--------|----------|---------|-----------------------|
| `name`    | string | No       | "World" | Name to greet        |

**Request Body**: None

**Response**:

```json
{
  "message": "Hello, {name}!"
}
```

**Status Codes**:
- `200 OK`: Success

**Examples**:

Default greeting:
```bash
curl http://localhost:8000/api/hello
```

Response:
```json
{
  "message": "Hello, World!"
}
```

Custom name:
```bash
curl "http://localhost:8000/api/hello?name=Developer"
```

Response:
```json
{
  "message": "Hello, Developer!"
}
```

**Implementation**:

```python
@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
```

---

## Configuration

### Settings Class

**Location**: `app/core/config.py`

The `Settings` class manages application configuration.

**Attributes**:

| Attribute  | Type | Default              | Description                    |
|------------|------|----------------------|--------------------------------|
| `APP_NAME` | str  | "FastAPI GH-AW Demo" | Application name               |
| `ENV`      | str  | "development"        | Environment (development/production) |

**Environment Variables**:

Configuration can be overridden using environment variables:

```bash
export ENV=production
```

**Usage**:

```python
from app.core.config import settings

print(settings.APP_NAME)  # "FastAPI GH-AW Demo"
print(settings.ENV)       # "development"
```

**Instance**:

```python
settings = Settings()
```

---

## Project Modules

### app.main

**Description**: Main FastAPI application module.

**Location**: `app/main.py`

**Exports**:
- `app`: FastAPI application instance

**Functions**:

#### root()

Root endpoint handler.

```python
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI GH AW Demo!"}
```

**Returns**: Dictionary with welcome message

---

### app.api.routes

**Description**: API route definitions.

**Location**: `app/api/routes.py`

**Exports**:
- `router`: APIRouter instance with `/api` prefix

**Router Configuration**:

```python
router = APIRouter(prefix="/api", tags=["demo"])
```

**Functions**:

#### hello(name: str = "World")

Greeting endpoint handler.

```python
@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
```

**Parameters**:
- `name` (str, optional): Name to include in greeting. Default: "World"

**Returns**: Dictionary with greeting message

---

### app.core.config

**Description**: Application configuration management.

**Location**: `app/core/config.py`

**Exports**:
- `Settings`: Configuration class
- `settings`: Settings instance

**Classes**:

#### Settings

Application settings with environment variable support.

**Attributes**:
- `APP_NAME` (str): Application name
- `ENV` (str): Environment name

**Example**:

```python
from app.core.config import settings

if settings.ENV == "production":
    # Production configuration
    pass
```

---

## Development Commands

### Make Commands

The project includes a Makefile with common development tasks.

**Location**: `Makefile`

#### make run

Start the development server with auto-reload.

```bash
make run
```

**Equivalent to**:
```bash
uvicorn app.main:app --reload
```

**Output**: Server starts on `http://127.0.0.1:8000`

---

#### make test

Run the test suite with pytest.

```bash
make test
```

**Equivalent to**:
```bash
pytest -v
```

**Output**: Test results with verbose output

---

#### make lint

Check code quality with Ruff.

```bash
make lint
```

**Equivalent to**:
```bash
ruff check app tests
```

**Output**: List of linting issues (if any)

---

#### make format

Auto-fix code quality issues with Ruff.

```bash
make format
```

**Equivalent to**:
```bash
ruff check --fix app tests
```

**Output**: Fixes applied to code files

---

## Testing

### Test Client

The test suite uses FastAPI's TestClient for endpoint testing.

**Location**: `tests/test_routes.py`

**Setup**:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
```

### Test Functions

#### test_root()

Tests the root endpoint.

```python
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]
```

**Assertions**:
- Status code is 200
- Response contains "Welcome"

---

#### test_hello()

Tests the `/api/hello` endpoint with a custom name.

```python
def test_hello():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Agent!"}
```

**Assertions**:
- Status code is 200
- Response matches expected message

---

## Dependencies

### Python Version

**Required**: Python >= 3.12

### Runtime Dependencies

**Location**: `pyproject.toml`

| Package    | Version   | Purpose                          |
|------------|-----------|----------------------------------|
| `fastapi`  | >= 0.119.0| Web framework                    |
| `uvicorn`  | >= 0.38.0 | ASGI server                      |
| `httpx`    | >= 0.28.1 | HTTP client (for testing)        |
| `pytest`   | >= 8.4.2  | Testing framework                |
| `ruff`     | >= 0.14.1 | Linter and formatter             |

### Installing Dependencies

Using uv (recommended):
```bash
uv sync
```

Using pip:
```bash
pip install fastapi>=0.119.0 uvicorn>=0.38.0 httpx>=0.28.1 pytest>=8.4.2 ruff>=0.14.1
```

---

## Code Quality Configuration

### Ruff Configuration

**Location**: `pyproject.toml`

```toml
[tool.ruff]
line-length = 88
target-version = "py311"
fix = true

[tool.ruff.lint]
extend-select = ["I"]  # Enables import sorting

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true
```

**Settings**:
- Line length: 88 characters
- Target Python version: 3.11
- Auto-fix enabled
- Import sorting enabled (like isort)
- Double quotes for strings
- Space indentation
- Format code in docstrings

---

## API Response Models

### Standard Response Format

All endpoints return JSON responses with appropriate HTTP status codes.

### Success Response

```json
{
  "message": "Success message or data"
}
```

### Error Response

```json
{
  "detail": "Error description"
}
```

**Common Status Codes**:

| Code | Meaning              | Usage                           |
|------|----------------------|---------------------------------|
| 200  | OK                   | Successful GET request          |
| 201  | Created              | Successful POST/resource creation|
| 400  | Bad Request          | Invalid request data            |
| 404  | Not Found            | Resource doesn't exist          |
| 422  | Unprocessable Entity | Validation error                |
| 500  | Internal Server Error| Server-side error               |

---

## Interactive Documentation

### Swagger UI

**URL**: `http://localhost:8000/docs`

Features:
- Interactive API testing
- Request/response examples
- Schema documentation
- "Try it out" functionality

### ReDoc

**URL**: `http://localhost:8000/redoc`

Features:
- Clean, readable documentation
- Three-panel layout
- Code samples
- Schema exploration

### OpenAPI Schema

**URL**: `http://localhost:8000/openapi.json`

Raw OpenAPI 3.0 schema in JSON format.

---

## Related Documentation

- **Getting Started**: See the [Tutorial](tutorial.md)
- **Common Tasks**: Check the [How-To Guides](how-to.md)
- **Architecture**: Read the [Explanation](explanation.md)

---

## Version History

### 0.1.0 (Current)

Initial release with:
- Basic FastAPI application structure
- Root and hello endpoints
- Testing framework
- Code quality tools
- Documentation
