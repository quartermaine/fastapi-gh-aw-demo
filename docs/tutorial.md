# Getting Started Tutorial

Welcome! This tutorial will guide you through setting up and running the FastAPI GH AW Demo project.

## Prerequisites

Before you begin, ensure you have:

- Python 3.12 or higher installed
- Git installed
- A terminal or command prompt
- A code editor (VS Code, PyCharm, etc.)

## Step 1: Clone the Repository

```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

## Step 2: Set Up Python Environment

We recommend using a virtual environment to isolate project dependencies.

### Using venv (built-in)

```bash
# Create virtual environment
python -m venv .venv

# Activate on Linux/macOS
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

### Using uv (recommended for faster installs)

```bash
# Install uv if you don't have it
pip install uv

# uv will automatically manage the virtual environment
```

## Step 3: Install Dependencies

```bash
# Using pip
pip install -e .

# Or using uv (faster)
uv pip install -e .
```

This installs:
- FastAPI - The web framework
- Uvicorn - The ASGI server
- pytest - Testing framework
- httpx - HTTP client for tests
- Ruff - Code formatter and linter

## Step 4: Verify Installation

Check that everything is installed correctly:

```bash
python -c "import fastapi; print(f'FastAPI {fastapi.__version__} installed')"
```

You should see output like: `FastAPI 0.119.0 installed`

## Step 5: Run the Application

Start the development server:

```bash
make run
```

Or manually:

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

## Step 6: Test the API

Open your browser and navigate to:

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Test Endpoints Manually

**Welcome Endpoint:**

```bash
curl http://localhost:8000/
```

Response:
```json
{"message": "Welcome to the FastAPI GH AW Demo!"}
```

**Hello Endpoint:**

```bash
curl http://localhost:8000/api/hello?name=Developer
```

Response:
```json
{"message": "Hello, Developer!"}
```

## Step 7: Run Tests

Verify everything works by running the test suite:

```bash
make test
```

You should see:

```
============================== test session starts ==============================
collected 2 items

tests/test_routes.py::test_root PASSED                                    [ 50%]
tests/test_routes.py::test_hello PASSED                                   [100%]

=============================== 2 passed in 0.12s ===============================
```

## Step 8: Explore the Code

Now that everything is running, explore the code structure:

### Main Application (`app/main.py`)

```python
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="FastAPI GH-AW Demo", version="0.1.0")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI GH AW Demo!"}
```

This is the application entry point that:
- Creates the FastAPI app instance
- Includes the API router
- Defines the root endpoint

### API Routes (`app/api/routes.py`)

```python
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["demo"])

@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
```

Routes are organized in separate modules for better organization.

### Configuration (`app/core/config.py`)

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

Configuration management using a Settings class.

## Step 9: Make Your First Change

Let's add a new endpoint!

1. Open `app/api/routes.py`
2. Add a new endpoint:

```python
@router.get("/goodbye")
def goodbye(name: str = "World"):
    return {"message": f"Goodbye, {name}!"}
```

3. Save the file
4. The server will automatically reload (watch for the reload message)
5. Test your new endpoint:

```bash
curl http://localhost:8000/api/goodbye?name=Tutorial
```

Expected response:
```json
{"message": "Goodbye, Tutorial!"}
```

6. Check the interactive docs at http://localhost:8000/docs - your new endpoint appears automatically!

## Step 10: Write a Test

Now let's write a test for our new endpoint.

1. Open `tests/test_routes.py`
2. Add a new test:

```python
def test_goodbye():
    response = client.get("/api/goodbye?name=Tester")
    assert response.status_code == 200
    assert response.json() == {"message": "Goodbye, Tester!"}
```

3. Run the tests:

```bash
make test
```

All tests should pass, including your new one!

## Next Steps

Congratulations! You've successfully:

- ✅ Set up the development environment
- ✅ Run the FastAPI application
- ✅ Tested API endpoints
- ✅ Explored the code structure
- ✅ Made your first code change
- ✅ Written your first test

### Continue Learning

- **[How-To Guides](./how-to-guides.md)** - Learn how to accomplish specific tasks
- **[API Reference](./reference.md)** - Detailed API documentation
- **[Architecture Explanation](./explanation.md)** - Understand the project design

## Troubleshooting

### Port Already in Use

If port 8000 is already in use:

```bash
uvicorn app.main:app --reload --port 8001
```

### Import Errors

Ensure you're in the virtual environment and dependencies are installed:

```bash
pip list | grep fastapi
```

### Tests Failing

Try reinstalling dependencies:

```bash
pip install -e . --force-reinstall
```

## Getting Help

- Check the [How-To Guides](./how-to-guides.md) for common issues
- Review [FastAPI documentation](https://fastapi.tiangolo.com/)
- Open an issue on [GitHub](https://github.com/quartermaine/fastapi-gh-aw-demo/issues)
