# Getting Started Tutorial

Welcome! This tutorial will guide you through setting up and building your first API with FastAPI GH-AW Demo.

## What You'll Learn

By the end of this tutorial, you'll be able to:
- Set up your development environment
- Run the FastAPI application
- Make API requests
- Add a new endpoint
- Write and run tests

**Time Required**: Approximately 20 minutes

## Prerequisites

Before starting, ensure you have:
- Python 3.12 or higher installed
- Basic familiarity with Python
- A terminal or command prompt
- A text editor or IDE

## Step 1: Set Up Your Environment

### Clone the Repository

First, get a copy of the project:

```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

### Install Dependencies

The project uses `uv` as its package manager. If you don't have it installed:

```bash
pip install uv
```

Now install the project dependencies:

```bash
uv sync
```

This creates a virtual environment and installs all required packages.

## Step 2: Start the Development Server

Start the application in development mode:

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

The server is now running and will automatically reload when you make code changes!

## Step 3: Explore the API

### Test the Root Endpoint

Open a new terminal window (keep the server running in the first one) and make a request:

```bash
curl http://localhost:8000/
```

You should receive:

```json
{"message": "Welcome to the FastAPI GH AW Demo!"}
```

### Try the Hello Endpoint

Test the API endpoint with the default name:

```bash
curl http://localhost:8000/api/hello
```

Response:

```json
{"message": "Hello, World!"}
```

Now try with a custom name:

```bash
curl "http://localhost:8000/api/hello?name=Developer"
```

Response:

```json
{"message": "Hello, Developer!"}
```

### Explore the Interactive Documentation

FastAPI automatically generates interactive API documentation. Open your browser and visit:

**http://localhost:8000/docs**

This is the Swagger UI interface where you can:
- See all available endpoints
- View request/response schemas
- Test endpoints directly from the browser

Try it now:
1. Click on the **GET /api/hello** endpoint
2. Click "Try it out"
3. Enter your name in the `name` parameter
4. Click "Execute"
5. See the response below

## Step 4: Add Your Own Endpoint

Let's create a new endpoint that returns information about a user.

### Edit the Routes File

Open `app/api/routes.py` in your text editor and add this new endpoint:

```python
@router.get("/user/{user_id}")
def get_user(user_id: int):
    """Get user information by ID."""
    return {
        "user_id": user_id,
        "username": f"user_{user_id}",
        "active": True
    }
```

Save the file. The server will automatically reload!

### Test Your New Endpoint

```bash
curl http://localhost:8000/api/user/123
```

Response:

```json
{
  "user_id": 123,
  "username": "user_123",
  "active": true
}
```

Check the interactive docs again at **http://localhost:8000/docs** - your new endpoint is automatically documented!

## Step 5: Write a Test

Good code includes tests. Let's write a test for your new endpoint.

### Create the Test

Open `tests/test_routes.py` and add this test function:

```python
def test_get_user():
    response = client.get("/api/user/42")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 42
    assert data["username"] == "user_42"
    assert data["active"] is True
```

### Run the Tests

Stop the development server (Ctrl+C) and run:

```bash
make test
```

You should see all tests passing:

```
tests/test_routes.py::test_root PASSED
tests/test_routes.py::test_hello PASSED
tests/test_routes.py::test_get_user PASSED
```

## Step 6: Check Code Quality

The project uses Ruff for code quality checks. Run:

```bash
make lint
```

If there are any issues, auto-fix them with:

```bash
make format
```

## What You've Accomplished

Congratulations! You've:

✅ Set up a FastAPI development environment  
✅ Started and interacted with the API server  
✅ Explored the interactive API documentation  
✅ Created a new API endpoint  
✅ Written and run tests  
✅ Checked code quality

## Next Steps

Now that you're familiar with the basics, you can:

- **Learn specific tasks**: Check out the [How-To Guides](how-to.md)
- **Explore the API**: Review the [API Reference](reference.md)
- **Understand the architecture**: Read the [Explanation](explanation.md)
- **Build something**: Try adding more complex endpoints with request validation, database integration, or authentication

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, start the server on a different port:

```bash
uvicorn app.main:app --reload --port 8001
```

### Import Errors

If you see import errors, ensure your virtual environment is activated and dependencies are installed:

```bash
uv sync
```

### Tests Failing

Make sure the development server is stopped before running tests to avoid port conflicts.

## Getting Help

- Review the [How-To Guides](how-to.md) for common tasks
- Check the [API Reference](reference.md) for detailed documentation
- Open an issue on GitHub for bugs or questions
