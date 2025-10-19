# How-To Guides

Practical, step-by-step guides for accomplishing specific tasks with the FastAPI GH-AW Demo project.

## Table of Contents

- [Development](#development)
  - [Add a New API Endpoint](#add-a-new-api-endpoint)
  - [Add Request Validation](#add-request-validation)
  - [Handle Errors Gracefully](#handle-errors-gracefully)
- [Testing](#testing)
  - [Write Unit Tests](#write-unit-tests)
  - [Test with Query Parameters](#test-with-query-parameters)
  - [Test Error Responses](#test-error-responses)
- [Configuration](#configuration)
  - [Change Application Settings](#change-application-settings)
  - [Use Environment Variables](#use-environment-variables)
- [Deployment](#deployment)
  - [Run in Production Mode](#run-in-production-mode)
  - [Deploy with Docker](#deploy-with-docker)

---

## Development

### Add a New API Endpoint

**Goal**: Create a new endpoint to handle specific functionality.

**Steps**:

1. Open `app/api/routes.py`

2. Add your endpoint function:

```python
@router.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    """Retrieve an item by ID with optional query parameter."""
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    return result
```

3. The server auto-reloads in development mode

4. Test your endpoint:

```bash
curl http://localhost:8000/api/items/42?q=test
```

5. Check the auto-generated docs at `http://localhost:8000/docs`

**Related**: See [API Reference](reference.md#endpoints) for endpoint patterns.

---

### Add Request Validation

**Goal**: Validate request data using Pydantic models.

**Steps**:

1. Create a models file `app/models.py`:

```python
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)
    in_stock: bool = True
```

2. Use the model in your endpoint (`app/api/routes.py`):

```python
from fastapi import HTTPException
from app.models import ItemCreate

@router.post("/items")
def create_item(item: ItemCreate):
    """Create a new item with validation."""
    return {
        "item": item.dict(),
        "message": "Item created successfully"
    }
```

3. Test with valid data:

```bash
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 29.99}'
```

4. Test with invalid data to see validation errors:

```bash
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "", "price": -10}'
```

**Result**: FastAPI automatically validates requests and returns detailed error messages for invalid data.

---

### Handle Errors Gracefully

**Goal**: Return meaningful error messages when things go wrong.

**Steps**:

1. Import HTTPException in `app/api/routes.py`:

```python
from fastapi import HTTPException, status
```

2. Add error handling to your endpoint:

```python
@router.get("/items/{item_id}")
def get_item(item_id: int):
    """Get an item by ID."""
    # Simulate database lookup
    if item_id > 1000:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found"
        )
    
    return {"item_id": item_id, "name": f"Item {item_id}"}
```

3. Test the error case:

```bash
curl http://localhost:8000/api/items/9999
```

**Result**: Returns a 404 status with a clear error message.

---

## Testing

### Write Unit Tests

**Goal**: Test your endpoints to ensure they work correctly.

**Steps**:

1. Open `tests/test_routes.py`

2. Add a test function:

```python
def test_get_item():
    response = client.get("/api/items/5")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 5
```

3. Run the tests:

```bash
make test
```

4. For verbose output:

```bash
pytest -v
```

**Tip**: Name test functions with the `test_` prefix so pytest discovers them automatically.

---

### Test with Query Parameters

**Goal**: Test endpoints that accept query parameters.

**Steps**:

1. Add a test with query parameters:

```python
def test_hello_with_name():
    response = client.get("/api/hello?name=Tester")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Tester!"}

def test_hello_default():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
```

2. Run the tests:

```bash
pytest tests/test_routes.py::test_hello_with_name -v
```

---

### Test Error Responses

**Goal**: Verify that your error handling works correctly.

**Steps**:

1. Add a test for error cases:

```python
def test_item_not_found():
    response = client.get("/api/items/9999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
```

2. Run the test:

```bash
make test
```

**Result**: Confirms your API returns appropriate error responses.

---

## Configuration

### Change Application Settings

**Goal**: Modify application configuration like name or version.

**Steps**:

1. Open `app/main.py`

2. Update the FastAPI initialization:

```python
app = FastAPI(
    title="My Custom API",
    version="1.0.0",
    description="A custom FastAPI application"
)
```

3. Restart the server and check the docs at `http://localhost:8000/docs`

**Result**: The API documentation reflects your new configuration.

---

### Use Environment Variables

**Goal**: Configure the application using environment variables.

**Steps**:

1. Update `app/core/config.py`:

```python
import os

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI GH-AW Demo")
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    API_PREFIX: str = os.getenv("API_PREFIX", "/api")

settings = Settings()
```

2. Use the settings in your app:

```python
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
```

3. Run with custom environment variables:

```bash
APP_NAME="Production API" ENV=production uvicorn app.main:app
```

**Tip**: Create a `.env` file for local development (don't commit it to Git).

---

## Deployment

### Run in Production Mode

**Goal**: Run the application optimized for production.

**Steps**:

1. Install production ASGI server (already included):

```bash
pip install uvicorn[standard]
```

2. Run with production settings:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

Options explained:
- `--host 0.0.0.0`: Accept connections from any IP
- `--port 8000`: Listen on port 8000
- `--workers 4`: Run 4 worker processes

3. For better performance, use gunicorn with uvicorn workers:

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Warning**: Never use `--reload` in production.

---

### Deploy with Docker

**Goal**: Containerize the application for deployment.

**Steps**:

1. Create `Dockerfile` in the project root:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY app ./app
COPY main.py ./

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Create `.dockerignore`:

```
__pycache__
*.pyc
.git
.github
tests
docs
*.md
.env
```

3. Build the image:

```bash
docker build -t fastapi-demo .
```

4. Run the container:

```bash
docker run -p 8000:8000 fastapi-demo
```

5. Test the containerized app:

```bash
curl http://localhost:8000/
```

**Next Step**: Deploy to your cloud platform (AWS, GCP, Azure, etc.).

---

## Tips and Best Practices

### Development Workflow

1. **Always run tests** before committing:
   ```bash
   make test && make lint
   ```

2. **Use type hints** for better IDE support and documentation

3. **Write tests first** (Test-Driven Development) when adding new features

4. **Keep endpoints focused** - one endpoint, one responsibility

### Performance

1. **Use async endpoints** for I/O-bound operations:
   ```python
   @router.get("/async-example")
   async def async_endpoint():
       # Use await with async operations
       return {"message": "Async response"}
   ```

2. **Limit response size** - paginate large datasets

3. **Cache frequently accessed data** when appropriate

### Security

1. **Never commit secrets** - use environment variables
2. **Validate all inputs** - use Pydantic models
3. **Use HTTPS** in production
4. **Implement rate limiting** for public APIs

---

## Need More Help?

- **API details**: See the [API Reference](reference.md)
- **Architecture questions**: Read the [Explanation](explanation.md)
- **Just starting**: Try the [Tutorial](tutorial.md)
- **Stuck?**: Open an issue on GitHub
