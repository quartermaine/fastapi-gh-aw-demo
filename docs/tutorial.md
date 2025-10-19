# Getting Started Tutorial

Welcome to the FastAPI GH AW Demo tutorial! This guide will walk you through setting up and using this FastAPI application step by step.

## What You'll Learn

By the end of this tutorial, you'll know how to:
- Set up the development environment
- Run the application locally
- Make your first API request
- Run tests to verify functionality
- Understand the project structure

## Step 1: Environment Setup

### Install Python

Ensure you have Python 3.12 or higher installed:

```bash
python --version
```

If you need to install Python, visit [python.org](https://www.python.org/downloads/).

### Install uv Package Manager

We recommend using `uv` for fast, reliable dependency management:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatively, you can use pip:
```bash
pip install uv
```

## Step 2: Clone and Setup

Clone the repository:

```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

Install dependencies:

```bash
uv sync
```

This command creates a virtual environment and installs all required packages.

## Step 3: Start the Application

Run the development server:

```bash
make run
```

You should see output similar to:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Step 4: Explore the API

### Using Your Browser

Open your browser and navigate to:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These interactive documentation pages let you explore and test the API directly.

### Using curl

Try the root endpoint:

```bash
curl http://localhost:8000/
```

Response:
```json
{"message": "Welcome to the FastAPI GH AW Demo!"}
```

Try the hello endpoint:

```bash
curl http://localhost:8000/api/hello
```

Response:
```json
{"message": "Hello, World!"}
```

With a custom name:

```bash
curl "http://localhost:8000/api/hello?name=Developer"
```

Response:
```json
{"message": "Hello, Developer!"}
```

### Using Python

Create a test script `test_api.py`:

```python
import httpx

# Test root endpoint
response = httpx.get("http://localhost:8000/")
print(response.json())

# Test hello endpoint
response = httpx.get("http://localhost:8000/api/hello?name=Python")
print(response.json())
```

Run it:
```bash
python test_api.py
```

## Step 5: Run Tests

Verify everything works by running the test suite:

```bash
make test
```

You should see all tests passing:

```
tests/test_routes.py::test_root PASSED
tests/test_routes.py::test_hello PASSED

====== 2 passed in 0.XX s ======
```

## Step 6: Understand the Code

### Application Entry Point

The main application is defined in `app/main.py`:

```python
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="FastAPI GH-AW Demo", version="0.1.0")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI GH AW Demo!"}
```

### API Routes

Routes are organized in `app/api/routes.py`:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["demo"])

@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
```

### Configuration

Application settings are in `app/core/config.py`:

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

## Step 7: Make Your First Change

Let's add a new endpoint! Open `app/api/routes.py` and add:

```python
@router.get("/status")
def status():
    return {
        "status": "healthy",
        "version": "0.1.0"
    }
```

Save the file. Thanks to auto-reload, the server will restart automatically.

Test your new endpoint:

```bash
curl http://localhost:8000/api/status
```

## Next Steps

Now that you've completed the tutorial, explore:

- **[API Reference](./api-reference.md)**: Complete API endpoint documentation
- **[Development Guide](./development.md)**: Best practices for contributing
- **[Configuration Guide](./configuration.md)**: Customize application settings

## Troubleshooting

### Port Already in Use

If port 8000 is busy, run uvicorn on a different port:

```bash
uvicorn app.main:app --reload --port 8001
```

### Module Not Found Errors

Ensure you've installed dependencies:

```bash
uv sync
```

And you're running commands from the project root directory.

### Tests Failing

Make sure the server is not running when executing tests, as they start their own test client.

## Getting Help

- Check existing [issues](https://github.com/quartermaine/fastapi-gh-aw-demo/issues)
- Review [FastAPI documentation](https://fastapi.tiangolo.com/)
- Create a new issue for bugs or questions
