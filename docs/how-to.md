# How-To Guides

Practical guides for common tasks in the FastAPI GH-AW Demo project.

## Table of Contents

- [Add a New API Endpoint](#add-a-new-api-endpoint)
- [Add Query Parameters](#add-query-parameters)
- [Add Request Body Validation](#add-request-body-validation)
- [Write Tests](#write-tests)
- [Configure Environment Variables](#configure-environment-variables)
- [Run in Production](#run-in-production)
- [Add CORS Support](#add-cors-support)
- [Debug the Application](#debug-the-application)

---

## Add a New API Endpoint

**Goal**: Create a new API endpoint in your application.

### Steps

1. Open `app/api/routes.py`

2. Add your new endpoint:

```python
@router.get("/greet/{name}")
def greet_user(name: str):
    """Greet a user by name from the path."""
    return {"message": f"Greetings, {name}!"}
```

3. Start the server:

```bash
make run
```

4. Test your endpoint:

```bash
curl http://localhost:8000/api/greet/Alice
```

Expected response:
```json
{"message": "Greetings, Alice!"}
```

5. Check the documentation at http://localhost:8000/docs to see your new endpoint.

---

## Add Query Parameters

**Goal**: Accept and validate query parameters.

### Steps

1. Define parameters with type hints:

```python
@router.get("/search")
def search(
    query: str,
    limit: int = 10,
    offset: int = 0
):
    """Search with pagination."""
    return {
        "query": query,
        "limit": limit,
        "offset": offset,
        "results": []  # Your search logic here
    }
```

2. Test with multiple parameters:

```bash
curl "http://localhost:8000/api/search?query=fastapi&limit=5&offset=0"
```

### Optional vs Required Parameters

- **Required**: No default value
```python
def search(query: str):  # Required
```

- **Optional**: Has a default value
```python
def search(query: str = ""):  # Optional with default
```

- **Using Optional type**:
```python
from typing import Optional

def search(query: Optional[str] = None):  # Explicitly optional
```

---

## Add Request Body Validation

**Goal**: Accept and validate JSON request bodies.

### Steps

1. Create a Pydantic model in `app/api/routes.py` or a new `models.py`:

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)
    quantity: int = Field(default=1, ge=1)
```

2. Use it in your endpoint:

```python
@router.post("/items")
def create_item(item: Item):
    """Create a new item."""
    return {
        "message": "Item created successfully",
        "item": item.model_dump()
    }
```

3. Test with curl:

```bash
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Widget",
    "description": "A useful widget",
    "price": 19.99,
    "quantity": 5
  }'
```

---

## Write Tests

**Goal**: Add tests for your new endpoints.

### Steps

1. Open `tests/test_routes.py`

2. Import the test client:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
```

3. Write your test function:

```python
def test_greet_user():
    response = client.get("/api/greet/Bob")
    assert response.status_code == 200
    assert response.json() == {"message": "Greetings, Bob!"}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "price": 9.99,
        "quantity": 2
    }
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "Test Item"
```

4. Run tests:

```bash
make test
```

### Test Patterns

**Testing query parameters**:
```python
response = client.get("/api/search?query=test&limit=5")
# or
response = client.get("/api/search", params={"query": "test", "limit": 5})
```

**Testing with headers**:
```python
response = client.get("/api/endpoint", headers={"Authorization": "Bearer token"})
```

**Testing error cases**:
```python
def test_invalid_item():
    response = client.post("/api/items", json={"name": ""})
    assert response.status_code == 422  # Validation error
```

---

## Configure Environment Variables

**Goal**: Use environment-specific configuration.

### Steps

1. Open `app/core/config.py`

2. Add new settings:

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")

settings = Settings()
```

3. Create a `.env` file in the project root:

```env
ENV=production
DEBUG=false
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

4. Use settings in your code:

```python
from app.core.config import settings

if settings.DEBUG:
    print("Debug mode is enabled")
```

5. Install python-dotenv (optional, for automatic `.env` loading):

```bash
uv add python-dotenv
```

Then in `app/core/config.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Run in Production

**Goal**: Deploy the application for production use.

### Steps

1. Set production environment variables:

```bash
export ENV=production
export DEBUG=false
```

2. Run with production settings:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Gunicorn (Recommended)

1. Install Gunicorn:

```bash
uv add gunicorn
```

2. Run with Gunicorn:

```bash
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo
```

---

## Add CORS Support

**Goal**: Enable Cross-Origin Resource Sharing for frontend applications.

### Steps

1. Open `app/main.py`

2. Add CORS middleware:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(title="FastAPI GH-AW Demo", version="0.1.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
```

3. For development, allow all origins:

```python
allow_origins=["*"],  # Allow all origins (use only in development)
```

---

## Debug the Application

**Goal**: Troubleshoot issues in your application.

### Using Print Statements

Add debug output:

```python
@router.get("/debug")
def debug_endpoint(value: str):
    print(f"Received value: {value}")  # Shows in console
    return {"value": value}
```

### Using Python Debugger

1. Add breakpoint in your code:

```python
@router.get("/debug")
def debug_endpoint(value: str):
    import pdb; pdb.set_trace()  # Execution pauses here
    return {"value": value}
```

2. Make a request and interact with the debugger in your terminal.

### Using Logging

1. Configure logging in `app/main.py`:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

2. Use in your routes:

```python
import logging
logger = logging.getLogger(__name__)

@router.get("/items")
def get_items():
    logger.debug("Fetching items")
    logger.info("Items retrieved successfully")
    return {"items": []}
```

### View Request Details

Log all requests:

```python
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    response = await call_next(request)
    return response
```

---

## Additional Resources

For more advanced topics, see:

- [Architecture Explanation](explanation.md) - Understanding the project structure
- [API Reference](reference.md) - Complete endpoint documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Official FastAPI docs
