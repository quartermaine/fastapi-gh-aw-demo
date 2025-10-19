# Getting Started Tutorial

This tutorial guides you through setting up and using the FastAPI GH-AW Demo application. By the end, you'll have a working API server and understand the basic concepts.

## What You'll Learn

- How to install and set up the project
- How to run the development server
- How to make your first API request
- How to run tests

## Prerequisites

Before starting, ensure you have:

- **Python 3.12 or higher** installed
- **Git** for cloning the repository
- A code editor (VS Code, PyCharm, or your preference)
- Basic familiarity with command line tools

## Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

## Step 2: Set Up Python Environment

This project uses `uv` for fast dependency management, but `pip` works too.

### Option A: Using uv (Recommended)

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync
```

### Option B: Using pip

```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Step 3: Verify Installation

Check that everything is installed correctly:

```bash
# Run the test suite
make test
```

You should see output showing all tests passing:

```
tests/test_routes.py::test_root PASSED
tests/test_routes.py::test_hello PASSED

====== 2 passed in 0.12s ======
```

## Step 4: Start the Development Server

Run the server:

```bash
make run
```

You'll see output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

The server is now running! Keep this terminal open.

## Step 5: Make Your First API Request

Open a new terminal and try the root endpoint:

```bash
curl http://localhost:8000/
```

Expected response:

```json
{"message": "Welcome to the FastAPI GH AW Demo!"}
```

Try the hello endpoint with a name parameter:

```bash
curl "http://localhost:8000/api/hello?name=Developer"
```

Expected response:

```json
{"message": "Hello, Developer!"}
```

## Step 6: Explore Interactive Documentation

FastAPI automatically generates interactive API documentation. Open your browser and visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

In Swagger UI, you can:

1. Click on an endpoint to expand it
2. Click "Try it out"
3. Enter parameters
4. Click "Execute" to make a request
5. See the response

## Step 7: Make Changes and See Live Updates

The development server automatically reloads when you save code changes.

1. Open `app/api/routes.py` in your editor
2. Modify the hello endpoint message
3. Save the file
4. Make a request again - you'll see your changes!

## Step 8: Run Code Quality Checks

Before committing changes, check code quality:

```bash
# Check for issues
make lint

# Auto-format code
make format
```

## What's Next?

Now that you have the basics working:

- Read the [How-To Guides](how-to.md) to learn specific tasks
- Check the [API Reference](reference.md) for detailed endpoint documentation
- Explore the [Architecture Explanation](explanation.md) to understand the project structure

## Troubleshooting

### Port Already in Use

If port 8000 is already in use:

```bash
uvicorn app.main:app --reload --port 8001
```

### Import Errors

Ensure you're in the project root directory and dependencies are installed:

```bash
pwd  # Should show .../fastapi-gh-aw-demo
uv sync  # or pip install -e .
```

### Tests Failing

If tests fail, ensure the application structure matches the imports. All `__init__.py` files should exist in:
- `app/`
- `app/api/`
- `app/core/`
- `tests/`

## Summary

You've successfully:

- ✅ Installed the project and dependencies
- ✅ Started the development server
- ✅ Made API requests
- ✅ Explored interactive documentation
- ✅ Run tests and quality checks

Continue learning with the [How-To Guides](how-to.md) for specific tasks.
