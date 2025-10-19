# API Endpoints Reference

Complete reference for all API endpoints in the FastAPI GitHub Actions Workflow Demo.

## Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## Root Endpoints

### GET /

Returns a welcome message.

**Response**

```json
{
  "message": "Welcome to the FastAPI GH AW Demo!"
}
```

**Status Codes**
- `200 OK`: Success

**Example**

```bash
curl http://localhost:8000/
```

## API Endpoints

All API endpoints are prefixed with `/api`.

### GET /api/hello

Returns a personalized greeting message.

**Query Parameters**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | string | No | "World" | Name to greet |

**Response**

```json
{
  "message": "Hello, {name}!"
}
```

**Status Codes**
- `200 OK`: Success

**Examples**

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

Custom greeting:
```bash
curl "http://localhost:8000/api/hello?name=Agent"
```

Response:
```json
{
  "message": "Hello, Agent!"
}
```

## Common Response Formats

### Success Response

```json
{
  "message": "Operation successful",
  "data": {}
}
```

### Error Response

```json
{
  "detail": "Error description"
}
```

### Validation Error Response

When request data is invalid:

```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## HTTP Status Codes

The API uses standard HTTP status codes:

| Code | Meaning | Usage |
|------|---------|-------|
| `200` | OK | Successful GET, PUT, DELETE |
| `201` | Created | Successful POST creating a resource |
| `204` | No Content | Successful DELETE with no response body |
| `400` | Bad Request | Invalid request data |
| `404` | Not Found | Resource not found |
| `422` | Unprocessable Entity | Validation error |
| `500` | Internal Server Error | Server error |

## Rate Limiting

Currently, no rate limiting is implemented. This may be added in future versions.

## Authentication

Currently, no authentication is required. Future versions may implement:
- API key authentication
- JWT tokens
- OAuth2

## Versioning

The API is currently at version `0.1.0`. Version is included in:
- Application metadata
- OpenAPI schema
- Response headers

## CORS

Cross-Origin Resource Sharing (CORS) is not currently configured. To enable CORS, see the [How-to Guide](../how-to/enable-cors.md).

## Request/Response Headers

### Common Request Headers

```
Content-Type: application/json
Accept: application/json
```

### Common Response Headers

```
Content-Type: application/json
```

## Error Handling

All errors follow FastAPI's standard error format:

### 404 Not Found

```json
{
  "detail": "Not found"
}
```

### 422 Validation Error

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

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```

## Data Types

### Common Data Types

- **string**: Text values
- **integer**: Whole numbers
- **float**: Decimal numbers
- **boolean**: `true` or `false`
- **array**: List of values
- **object**: JSON object

### Date/Time Format

ISO 8601 format:
```
2025-10-19T09:00:00.000000
```

## Pagination

Pagination is not currently implemented. Future endpoints may use:

**Query Parameters**
- `skip`: Number of items to skip (default: 0)
- `limit`: Maximum items to return (default: 10)

**Response Format**
```json
{
  "items": [],
  "total": 100,
  "skip": 0,
  "limit": 10
}
```

## Filtering and Sorting

Not currently implemented. Future endpoints may support:

**Filtering**
```
GET /api/items?status=active&category=demo
```

**Sorting**
```
GET /api/items?sort_by=created_at&order=desc
```

## WebSocket Endpoints

No WebSocket endpoints are currently available.

## Batch Operations

Batch operations are not currently supported.

## Testing Endpoints

Use the interactive documentation at http://localhost:8000/docs to test endpoints directly in your browser.

Alternatively, use tools like:
- **curl**: Command-line HTTP client
- **HTTPie**: User-friendly HTTP client
- **Postman**: API development platform
- **Insomnia**: API client

## Examples with Different Tools

### curl

```bash
# GET request
curl http://localhost:8000/api/hello?name=Agent

# POST request (future)
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username": "test"}'
```

### HTTPie

```bash
# GET request
http GET http://localhost:8000/api/hello name==Agent

# POST request (future)
http POST http://localhost:8000/api/users username=test
```

### Python requests

```python
import requests

# GET request
response = requests.get(
    "http://localhost:8000/api/hello",
    params={"name": "Agent"}
)
print(response.json())

# POST request (future)
response = requests.post(
    "http://localhost:8000/api/users",
    json={"username": "test"}
)
print(response.json())
```

### JavaScript fetch

```javascript
// GET request
fetch('http://localhost:8000/api/hello?name=Agent')
  .then(response => response.json())
  .then(data => console.log(data));

// POST request (future)
fetch('http://localhost:8000/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({username: 'test'}),
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## OpenAPI Schema

The complete OpenAPI schema is available at:

```
http://localhost:8000/openapi.json
```

This schema can be used to:
- Generate client libraries
- Import into API testing tools
- Generate documentation
- Validate requests

## See Also

- [How to Add Endpoints](../how-to/add-endpoint.md)
- [How to Run Tests](../how-to/run-tests.md)
- [Application Architecture](../explanation/architecture.md)
