# API Reference

Complete technical reference for the FastAPI GH-AW Demo API.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, this API does not require authentication.

## Endpoints

### Root Endpoint

Get a welcome message.

**Endpoint**: `GET /`

**Response**:

- **Status Code**: `200 OK`
- **Content-Type**: `application/json`

**Response Schema**:

```json
{
  "message": "string"
}
```

**Example Request**:

```bash
curl http://localhost:8000/
```

**Example Response**:

```json
{
  "message": "Welcome to the FastAPI GH AW Demo!"
}
```

---

### Hello Endpoint

Get a personalized greeting.

**Endpoint**: `GET /api/hello`

**Query Parameters**:

| Parameter | Type   | Required | Default | Description              |
|-----------|--------|----------|---------|--------------------------|
| `name`    | string | No       | "World" | The name to greet        |

**Response**:

- **Status Code**: `200 OK`
- **Content-Type**: `application/json`

**Response Schema**:

```json
{
  "message": "string"
}
```

**Example Requests**:

Without parameters:
```bash
curl http://localhost:8000/api/hello
```

Response:
```json
{
  "message": "Hello, World!"
}
```

With name parameter:
```bash
curl "http://localhost:8000/api/hello?name=Alice"
```

Response:
```json
{
  "message": "Hello, Alice!"
}
```

---

## Interactive Documentation

### Swagger UI

Access interactive API documentation with a try-it-out feature:

```
http://localhost:8000/docs
```

Features:
- Interactive API exploration
- Request/response examples
- Schema validation
- Direct API testing

### ReDoc

Access alternative documentation with a focus on readability:

```
http://localhost:8000/redoc
```

Features:
- Clean, readable layout
- Code samples
- Search functionality
- Mobile-friendly

---

## Application Configuration

### Settings Class

Located in `app/core/config.py`.

**Attributes**:

| Attribute  | Type   | Description                    | Default         |
|------------|--------|--------------------------------|-----------------|
| `APP_NAME` | string | Application name               | "FastAPI GH-AW Demo" |
| `ENV`      | string | Environment (development/production) | "development" |

**Environment Variables**:

| Variable | Description           | Default       |
|----------|-----------------------|---------------|
| `ENV`    | Application environment | "development" |

**Example**:

```python
from app.core.config import settings

print(settings.APP_NAME)  # "FastAPI GH-AW Demo"
print(settings.ENV)       # "development"
```

---

## FastAPI Application

### App Instance

Located in `app/main.py`.

**Configuration**:

```python
app = FastAPI(
    title="FastAPI GH-AW Demo",
    version="0.1.0"
)
```

**Attributes**:

- **title**: Application name displayed in documentation
- **version**: Current API version

### Router

Located in `app/api/routes.py`.

**Configuration**:

```python
router = APIRouter(
    prefix="/api",
    tags=["demo"]
)
```

**Attributes**:

- **prefix**: Base path for all routes (`/api`)
- **tags**: OpenAPI tags for grouping endpoints

---

## Response Models

### Message Response

Generic message response used by all endpoints.

**Schema**:

```python
{
  "message": str  # A message string
}
```

**Example**:

```json
{
  "message": "Hello, World!"
}
```

---

## Error Responses

### 422 Unprocessable Entity

Returned when request validation fails.

**Example**:

Request with invalid query parameter type:
```bash
curl "http://localhost:8000/api/hello?name[]=invalid"
```

Response:
```json
{
  "detail": [
    {
      "loc": ["query", "name"],
      "msg": "str type expected",
      "type": "type_error.str"
    }
  ]
}
```

---

## Testing Client

### TestClient

Located in `tests/test_routes.py`.

**Usage**:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Make a request
response = client.get("/")

# Assert response
assert response.status_code == 200
assert response.json() == {"message": "Welcome to the FastAPI GH AW Demo!"}
```

**Available Methods**:

- `client.get(url, params=None, headers=None)`
- `client.post(url, json=None, data=None, headers=None)`
- `client.put(url, json=None, data=None, headers=None)`
- `client.delete(url, headers=None)`
- `client.patch(url, json=None, data=None, headers=None)`

---

## OpenAPI Specification

The OpenAPI (Swagger) specification is automatically generated and available at:

```
http://localhost:8000/openapi.json
```

This JSON file describes the complete API schema and can be imported into API testing tools like Postman or Insomnia.

---

## Version Information

**Current Version**: 0.1.0

**Python Version**: >= 3.12

**FastAPI Version**: >= 0.119.0

---

## Dependencies

Core dependencies defined in `pyproject.toml`:

| Package    | Version   | Purpose                        |
|------------|-----------|--------------------------------|
| fastapi    | >=0.119.0 | Web framework                  |
| uvicorn    | >=0.38.0  | ASGI server                    |
| httpx      | >=0.28.1  | HTTP client for testing        |
| pytest     | >=8.4.2   | Testing framework              |
| ruff       | >=0.14.1  | Linting and formatting         |

For a complete list with locked versions, see `uv.lock`.
