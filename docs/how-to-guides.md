# How-To Guides

Practical guides for common tasks and workflows.

## Table of Contents

- [Adding New API Endpoints](#adding-new-api-endpoints)
- [Writing Tests](#writing-tests)
- [Working with Configuration](#working-with-configuration)
- [Code Quality and Formatting](#code-quality-and-formatting)
- [Running the Application](#running-the-application)
- [Debugging](#debugging)
- [Working with GitHub Actions](#working-with-github-actions)
- [Troubleshooting](#troubleshooting)

---

## Adding New API Endpoints

### Create a Simple GET Endpoint

1. Open `app/api/routes.py`
2. Add your endpoint function:

```python
@router.get("/status")
def get_status():
    return {
        "status": "operational",
        "version": "0.1.0"
    }
```

3. Test it:

```bash
curl http://localhost:8000/api/status
```

### Create a POST Endpoint with Request Body

1. Define a Pydantic model in `app/api/routes.py`:

```python
from pydantic import BaseModel

class Message(BaseModel):
    text: str
    author: str = "Anonymous"

@router.post("/messages")
def create_message(message: Message):
    return {
        "received": message.text,
        "from": message.author
    }
```

2. Test it:

```bash
curl -X POST http://localhost:8000/api/messages \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello", "author": "Developer"}'
```

### Add Path Parameters

```python
@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}"
    }
```

### Add Query Parameters with Validation

```python
from typing import Optional

@router.get("/search")
def search(q: str, limit: int = 10, offset: int = 0):
    return {
        "query": q,
        "limit": limit,
        "offset": offset,
        "results": []
    }
```

---

## Writing Tests

### Test a GET Endpoint

```python
def test_status():
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"
```

### Test a POST Endpoint

```python
def test_create_message():
    payload = {
        "text": "Test message",
        "author": "Tester"
    }
    response = client.post("/api/messages", json=payload)
    assert response.status_code == 200
    assert response.json()["received"] == "Test message"
```

### Test with Path Parameters

```python
def test_get_user():
    response = client.get("/api/users/42")
    assert response.status_code == 200
    assert response.json()["user_id"] == 42
```

### Test Error Cases

```python
def test_missing_parameter():
    response = client.get("/api/search")  # Missing required 'q' param
    assert response.status_code == 422  # Validation error
```

### Run Specific Tests

```bash
# Run a single test file
pytest tests/test_routes.py -v

# Run a specific test function
pytest tests/test_routes.py::test_root -v

# Run tests matching a pattern
pytest -k "test_hello" -v
```

---

## Working with Configuration

### Add Environment Variables

1. Update `app/core/config.py`:

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    API_KEY: str = os.getenv("API_KEY", "")

settings = Settings()
```

2. Create a `.env` file (add to `.gitignore`):

```bash
ENV=production
DEBUG=false
API_KEY=your-secret-key
```

3. Use in your application:

```python
from app.core.config import settings

@router.get("/config")
def get_config():
    return {
        "app_name": settings.APP_NAME,
        "environment": settings.ENV
    }
```

### Use Pydantic Settings (Recommended)

1. Install `pydantic-settings`:

```bash
pip install pydantic-settings
```

2. Update `app/core/config.py`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = "development"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

---

## Code Quality and Formatting

### Check Code Style

```bash
make lint
```

Or manually:

```bash
ruff check app tests
```

### Auto-Fix Issues

```bash
make format
```

Or manually:

```bash
ruff check --fix app tests
```

### Format Code

```bash
ruff format app tests
```

### Check Specific Files

```bash
ruff check app/api/routes.py
```

---

## Running the Application

### Development Mode (Auto-Reload)

```bash
make run
```

Or:

```bash
uvicorn app.main:app --reload
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Custom Host and Port

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload
```

### With Environment Variables

```bash
ENV=production uvicorn app.main:app
```

---

## Debugging

### Enable Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

### Use Python Debugger

Add breakpoints in your code:

```python
@router.get("/debug")
def debug_endpoint():
    import pdb; pdb.set_trace()  # Breakpoint
    return {"debug": "mode"}
```

### Debug with VS Code

Create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "app.main:app",
                "--reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

### View Request Details

```python
from fastapi import Request

@router.get("/inspect")
async def inspect_request(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host
    }
```

---

## Working with GitHub Actions

### Trigger Documentation Update

Documentation updates are automated. The workflow runs when:

- Code is pushed to the main branch
- Pull requests are opened or updated

### Check Workflow Status

```bash
gh run list --workflow=update-docs.lock.yml
```

### View Workflow Logs

```bash
gh run view --log
```

### Manually Trigger Workflow

If configured with `workflow_dispatch`:

```bash
gh workflow run update-docs.lock.yml
```

---

## Troubleshooting

### Problem: Import Errors

**Symptoms**: `ModuleNotFoundError` when running the app

**Solution**:

```bash
# Ensure you're in the project root
pwd

# Install in editable mode
pip install -e .
```

### Problem: Port Already in Use

**Symptoms**: `OSError: [Errno 48] Address already in use`

**Solutions**:

```bash
# Option 1: Use a different port
uvicorn app.main:app --port 8001

# Option 2: Find and kill the process
lsof -ti:8000 | xargs kill -9
```

### Problem: Tests Failing

**Symptoms**: Tests that worked before now fail

**Solutions**:

```bash
# Clear pytest cache
rm -rf .pytest_cache __pycache__

# Reinstall dependencies
pip install -e . --force-reinstall

# Run tests with verbose output
pytest -vv
```

### Problem: Auto-Reload Not Working

**Symptoms**: Changes don't reflect after saving files

**Solutions**:

```bash
# Restart the server
# Make sure you're using --reload flag
uvicorn app.main:app --reload

# Check file permissions
ls -la app/
```

### Problem: 422 Validation Error

**Symptoms**: API returns 422 for valid requests

**Solutions**:

1. Check the request matches the Pydantic model
2. Review the `/docs` endpoint for expected schema
3. Verify Content-Type header for POST requests:

```bash
curl -X POST http://localhost:8000/api/messages \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello"}'
```

### Problem: CORS Errors in Browser

**Symptoms**: Browser blocks API requests

**Solution**: Add CORS middleware in `app/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Getting More Help

- Check the [API Reference](./reference.md) for detailed specifications
- Review [FastAPI documentation](https://fastapi.tiangolo.com/)
- Search [GitHub issues](https://github.com/quartermaine/fastapi-gh-aw-demo/issues)
- Read the [Architecture Explanation](./explanation.md) for design context
