# Development Guide

This guide covers best practices, development workflow, and contribution guidelines for the FastAPI GH AW Demo project.

## Development Environment

### Setup

1. Fork and clone the repository
2. Install dependencies: `uv sync`
3. Create a feature branch: `git checkout -b feature/your-feature-name`

### Development Tools

This project uses modern Python development tools:

- **uv**: Fast Python package manager
- **Ruff**: Lightning-fast linter and formatter
- **pytest**: Testing framework
- **FastAPI**: Web framework with automatic API documentation

## Code Style

### Python Style Guide

Follow PEP 8 guidelines with these specific configurations:

- **Line length**: 88 characters (Black-compatible)
- **Quote style**: Double quotes
- **Indentation**: 4 spaces
- **Import sorting**: Enabled (alphabetical within groups)

### Automated Formatting

Format code automatically:

```bash
make format
```

This runs Ruff with auto-fix enabled.

### Linting

Check code quality:

```bash
make lint
```

Fix linting issues automatically when possible:

```bash
ruff check --fix app tests
```

### Ruff Configuration

The project's Ruff configuration is defined in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py312"
fix = true

[tool.ruff.lint]
extend-select = ["I"]  # Enables import sorting

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true
```

Key configuration details:

- **target-version**: Set to `"py312"` to match the project's Python requirement (3.12+)
  - This ensures Ruff's linting rules and type checking align with Python 3.12 features and syntax
  - Must be kept in sync with `requires-python` in `pyproject.toml` and `.python-version`
- **line-length**: 88 characters (Black-compatible standard)
- **fix**: Automatically fix issues when possible
- **Import sorting**: Enabled via `extend-select = ["I"]` for consistent import organization

## Project Structure

### Directory Organization

```
fastapi-gh-aw-demo/
├── app/                      # Main application package
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── api/                 # API routes and endpoints
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/                # Core functionality
│   │   ├── __init__.py
│   │   └── config.py        # Configuration management
│   ├── models/              # Data models (future)
│   ├── schemas/             # Pydantic schemas (future)
│   └── services/            # Business logic (future)
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_routes.py
├── docs/                    # Documentation
└── pyproject.toml          # Project configuration
```

### Module Organization

- **app/main.py**: FastAPI application initialization and configuration
- **app/api/**: API routes organized by domain
- **app/core/**: Core functionality like configuration, dependencies, security
- **app/models/**: Database models (when using ORM)
- **app/schemas/**: Request/response Pydantic models
- **app/services/**: Business logic layer

## Testing

### Writing Tests

Use pytest with FastAPI's TestClient:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoint():
    response = client.get("/api/endpoint")
    assert response.status_code == 200
    assert response.json() == {"expected": "value"}
```

### Test Organization

- Mirror the app structure in tests
- One test file per module
- Group related tests in classes
- Use descriptive test names

Example:
```python
class TestHelloEndpoint:
    def test_default_greeting(self):
        """Test hello endpoint with default parameter"""
        response = client.get("/api/hello")
        assert response.json() == {"message": "Hello, World!"}
    
    def test_custom_greeting(self):
        """Test hello endpoint with custom name"""
        response = client.get("/api/hello?name=Test")
        assert response.json() == {"message": "Hello, Test!"}
```

### Running Tests

Run all tests:
```bash
make test
```

Run specific test file:
```bash
pytest tests/test_routes.py -v
```

Run specific test:
```bash
pytest tests/test_routes.py::test_hello -v
```

Run with coverage:
```bash
pytest --cov=app --cov-report=html
```

## Making Changes

### Adding New Endpoints

1. **Define the route** in `app/api/routes.py` or a new router file:

```python
@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Example Item"}
```

2. **Add validation** using Pydantic models:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@router.post("/items")
def create_item(item: Item):
    return {"item": item}
```

3. **Write tests**:

```python
def test_get_item():
    response = client.get("/api/items/1")
    assert response.status_code == 200
    assert response.json()["item_id"] == 1

def test_create_item():
    item_data = {"name": "Test", "price": 10.99}
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 200
```

4. **Update documentation** if needed

### Adding Configuration

Add settings to `app/core/config.py`:

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

settings = Settings()
```

Use in your application:

```python
from app.core.config import settings

if settings.DEBUG:
    # Debug behavior
    pass
```

## Git Workflow

### Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(api): add user authentication endpoint

Implements JWT-based authentication with refresh tokens.

Closes #123
```

```
fix(routes): handle empty name parameter correctly

Previously returned error when name was empty string.
Now defaults to "World" as expected.
```

### Branch Naming

Use descriptive branch names:

- `feature/add-user-auth`
- `fix/empty-name-parameter`
- `docs/api-documentation`
- `refactor/config-module`

### Pull Request Process

1. **Create a branch** from `main`
2. **Make changes** with clear commits
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Run tests and linting**: `make test && make lint`
6. **Push branch** to your fork
7. **Open pull request** with clear description
8. **Address review feedback**

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
```

## Performance Best Practices

### Async/Await

Use async endpoints for I/O operations:

```python
@router.get("/data")
async def get_data():
    # Async database query
    data = await fetch_from_db()
    return data
```

### Response Models

Define response models for validation and documentation:

```python
from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    return {"id": item_id, "name": "Item", "price": 10.99}
```

### Background Tasks

Use background tasks for non-blocking operations:

```python
from fastapi import BackgroundTasks

def send_notification(email: str):
    # Send email
    pass

@router.post("/register")
def register(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_notification, email)
    return {"message": "Registered"}
```

## Debugging

### Development Server

Run with reload for automatic restart on changes:

```bash
uvicorn app.main:app --reload
```

Enable debug logging:

```bash
uvicorn app.main:app --reload --log-level debug
```

### Interactive Debugging

Use Python debugger (pdb):

```python
import pdb; pdb.set_trace()
```

Or use breakpoint() (Python 3.7+):

```python
breakpoint()
```

### Logging

Add logging to your application:

```python
import logging

logger = logging.getLogger(__name__)

@router.get("/endpoint")
def endpoint():
    logger.info("Endpoint called")
    return {"status": "ok"}
```

## Continuous Integration

Tests and linting run automatically on GitHub Actions for:
- Every push to main
- Every pull request
- Scheduled daily runs

Ensure local tests pass before pushing:

```bash
make test && make lint
```

## Common Issues

### Import Errors

Ensure you're running commands from project root and dependencies are installed:

```bash
uv sync
```

### Port Conflicts

If port 8000 is in use:

```bash
uvicorn app.main:app --reload --port 8001
```

### Test Failures

Ensure server is not running during tests. TestClient manages its own application instance.

## Additional Resources

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/best-practices/)
- [Python Testing with pytest](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Conventional Commits](https://www.conventionalcommits.org/)
