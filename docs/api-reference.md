# API Reference

Complete technical reference for all API endpoints in the FastAPI GH AW Demo application.

## Base URL

- **Development**: `http://localhost:8000`
- **Production**: Configure via environment variables

## Authentication

Currently, this demo application does not require authentication. All endpoints are publicly accessible.

## Response Format

All responses are in JSON format with appropriate HTTP status codes.

### Success Response

```json
{
  "message": "Response content",
  "data": {}
}
```

### Error Response

```json
{
  "detail": "Error description"
}
```

## Endpoints

---

### Root

Get a welcome message from the API.

**Endpoint**: `GET /`

**Parameters**: None

**Response**:

```json
{
  "message": "Welcome to the FastAPI GH AW Demo!"
}
```

**Status Codes**:
- `200 OK`: Success

**Example Request**:

```bash
curl http://localhost:8000/
```

**Example with httpx**:

```python
import httpx

response = httpx.get("http://localhost:8000/")
print(response.json())
```

---

### Hello

Get a personalized greeting message.

**Endpoint**: `GET /api/hello`

**Parameters**:

| Name   | Type   | Required | Default | Description                    |
|--------|--------|----------|---------|--------------------------------|
| `name` | string | No       | "World" | Name to include in the greeting |

**Response**:

```json
{
  "message": "Hello, {name}!"
}
```

**Status Codes**:
- `200 OK`: Success

**Example Requests**:

Default greeting:
```bash
curl http://localhost:8000/api/hello
```

Response:
```json
{"message": "Hello, World!"}
```

Custom greeting:
```bash
curl "http://localhost:8000/api/hello?name=Developer"
```

Response:
```json
{"message": "Hello, Developer!"}
```

**Example with httpx**:

```python
import httpx

# Default greeting
response = httpx.get("http://localhost:8000/api/hello")
print(response.json())  # {"message": "Hello, World!"}

# Custom greeting
response = httpx.get(
    "http://localhost:8000/api/hello",
    params={"name": "Developer"}
)
print(response.json())  # {"message": "Hello, Developer!"}
```

**Example with JavaScript**:

```javascript
// Default greeting
fetch('http://localhost:8000/api/hello')
  .then(response => response.json())
  .then(data => console.log(data));

// Custom greeting
fetch('http://localhost:8000/api/hello?name=Developer')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

### Swagger UI

Access at: `http://localhost:8000/docs`

Features:
- Interactive endpoint testing
- Request/response examples
- Schema definitions
- Try out API calls directly from the browser

### ReDoc

Access at: `http://localhost:8000/redoc`

Features:
- Clean, three-panel layout
- Search functionality
- Detailed schema documentation
- Export to OpenAPI specification

### OpenAPI Schema

Raw OpenAPI (formerly Swagger) specification available at:

`http://localhost:8000/openapi.json`

This can be used with tools like:
- Postman
- Insomnia
- OpenAPI Generator for client SDK generation

## Rate Limiting

Currently, no rate limiting is implemented. For production deployments, consider adding rate limiting middleware.

## CORS (Cross-Origin Resource Sharing)

CORS is not currently configured. To enable CORS for frontend applications, add CORS middleware to `app/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Error Handling

### Validation Errors

When invalid parameters are provided, FastAPI returns a `422 Unprocessable Entity` status with details:

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

### Not Found Errors

When accessing non-existent endpoints, a `404 Not Found` status is returned:

```json
{
  "detail": "Not Found"
}
```

## Testing Endpoints

### Using the Test Client

FastAPI provides a test client for integration testing:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_hello():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Agent!"}
```

### Using pytest

Run tests with:

```bash
pytest -v
```

Or using the Makefile:

```bash
make test
```

## Extending the API

### Adding New Endpoints

Add endpoints to `app/api/routes.py`:

```python
@router.get("/status")
def status():
    return {
        "status": "healthy",
        "version": "0.1.0"
    }
```

### Creating Additional Routers

For larger applications, create separate router files:

```python
# app/api/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    return {"users": []}
```

Include in `app/main.py`:

```python
from app.api.users import router as users_router

app.include_router(users_router)
```

## API Versioning

For API versioning, use route prefixes:

```python
# app/api/v1/routes.py
router = APIRouter(prefix="/api/v1", tags=["v1"])

# app/api/v2/routes.py
router = APIRouter(prefix="/api/v2", tags=["v2"])
```

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Models](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/)
