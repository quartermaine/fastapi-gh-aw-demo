# Getting Started Tutorial

This tutorial guides you through setting up the FastAPI GitHub Actions Workflow Demo and creating your first API endpoint.

## Prerequisites

Before you begin, ensure you have:

- Python 3.12 or higher installed
- Basic knowledge of Python and REST APIs
- A text editor or IDE (VS Code, PyCharm, etc.)

## Step 1: Install the Project

### Clone the Repository

```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

### Install Dependencies

This project uses `uv` as the package manager for faster dependency resolution:

```bash
# Install dependencies
uv sync
```

If you don't have `uv` installed, you can install it:

```bash
pip install uv
```

Alternatively, use pip:

```bash
pip install -r requirements.txt
```

## Step 2: Run the Application

Start the development server with auto-reload enabled:

```bash
make run
```

Or run directly:

```bash
uvicorn app.main:app --reload
```

You should see output similar to:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Step 3: Test the API

### Using Your Browser

Open your browser and navigate to:

- API Root: http://localhost:8000/
- Interactive Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

### Using curl

```bash
# Test the root endpoint
curl http://localhost:8000/

# Test the hello endpoint
curl http://localhost:8000/api/hello?name=Developer
```

Expected responses:

```json
{"message": "Welcome to the FastAPI GH AW Demo!"}
```

```json
{"message": "Hello, Developer!"}
```

## Step 4: Explore the Interactive Documentation

FastAPI automatically generates interactive API documentation:

1. Visit http://localhost:8000/docs
2. Expand the `/api/hello` endpoint
3. Click "Try it out"
4. Enter a name parameter
5. Click "Execute"
6. See the response

## Step 5: Create Your First Endpoint

Let's add a new endpoint that returns the current time.

### Create a New Route

Edit `app/api/routes.py`:

```python
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["demo"])


@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}


@router.get("/time")
def get_current_time():
    """Return the current server time."""
    return {
        "current_time": datetime.now().isoformat(),
        "timezone": "UTC"
    }
```

### Test Your New Endpoint

The server auto-reloads, so visit:

```bash
curl http://localhost:8000/api/time
```

Response:

```json
{
  "current_time": "2025-10-19T09:00:00.000000",
  "timezone": "UTC"
}
```

## Step 6: Write Tests

Create a test for your new endpoint in `tests/test_routes.py`:

```python
def test_current_time():
    response = client.get("/api/time")
    assert response.status_code == 200
    assert "current_time" in response.json()
    assert "timezone" in response.json()
```

Run the tests:

```bash
make test
```

Expected output:

```
tests/test_routes.py::test_root PASSED
tests/test_routes.py::test_hello PASSED
tests/test_routes.py::test_current_time PASSED

====== 3 passed in 0.12s ======
```

## Step 7: Code Quality Checks

### Lint Your Code

```bash
make lint
```

### Format Your Code

```bash
make format
```

## Next Steps

Congratulations! You've successfully:

- Set up the development environment
- Run the application
- Explored the API documentation
- Created a new endpoint
- Written tests

Continue learning with:

- [How to Add Authentication](how-to/add-authentication.md)
- [How to Configure Environment Variables](how-to/configure-env.md)
- [Application Architecture](explanation/architecture.md)
- [API Reference](reference/endpoints.md)

## Troubleshooting

### Port Already in Use

If port 8000 is already in use:

```bash
uvicorn app.main:app --reload --port 8001
```

### Import Errors

Ensure you're in the project root directory and dependencies are installed:

```bash
uv sync
```

### Tests Failing

Verify the application runs correctly first:

```bash
make run
```

Then run tests in a separate terminal:

```bash
make test
```
