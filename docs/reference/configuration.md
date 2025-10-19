# Configuration Reference

Complete reference for all configuration options in the FastAPI GitHub Actions Workflow Demo.

## Overview

Configuration is managed through environment variables and the `Settings` class in `app/core/config.py`.

## Environment Variables

### Application Settings

#### APP_NAME

- **Type**: `string`
- **Default**: `"FastAPI GH-AW Demo"`
- **Description**: Name of the application
- **Example**: `APP_NAME="Production API"`

#### ENV

- **Type**: `string`
- **Default**: `"development"`
- **Valid Values**: `development`, `staging`, `production`, `test`
- **Description**: Current environment name
- **Example**: `ENV=production`

## Configuration Files

### pyproject.toml

Project configuration following Python packaging standards.

#### [project]

```toml
[project]
name = "fastapi-gh-aw-demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.119.0",
    "httpx>=0.28.1",
    "pytest>=8.4.2",
    "ruff>=0.14.1",
    "uvicorn>=0.38.0",
]
```

**Fields**:
- `name`: Package name
- `version`: Current version (follows SemVer)
- `description`: Short project description
- `readme`: README file path
- `requires-python`: Minimum Python version
- `dependencies`: Required packages

#### [tool.ruff]

Ruff linter and formatter configuration:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"
fix = true
```

**Options**:
- `line-length`: Maximum line length (88 characters)
- `target-version`: Target Python version for linting
- `fix`: Automatically fix issues when possible

#### [tool.ruff.lint]

Linting rules configuration:

```toml
[tool.ruff.lint]
extend-select = ["I"]  # Enables import sorting
```

**Rules**:
- `I`: Import sorting (isort-compatible)

#### [tool.ruff.format]

Code formatting configuration:

```toml
[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true
```

**Options**:
- `quote-style`: Use double quotes
- `indent-style`: Use spaces for indentation
- `docstring-code-format`: Format code in docstrings

### .env File

Environment-specific configuration (create this file locally):

```bash
# .env
ENV=development
APP_NAME="FastAPI GH-AW Demo"
```

**Important**: 
- Never commit `.env` files to version control
- Use `.env.example` for templates
- Store sensitive data in GitHub Secrets for CI/CD

## Settings Class

### Location

`app/core/config.py`

### Current Implementation

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

### Usage

```python
from app.core.config import settings

print(settings.APP_NAME)  # "FastAPI GH-AW Demo"
print(settings.ENV)       # "development"
```

## FastAPI Application Configuration

### Location

`app/main.py`

### Configuration

```python
app = FastAPI(
    title="FastAPI GH-AW Demo",
    version="0.1.0"
)
```

### Available Options

```python
app = FastAPI(
    title="API Title",                    # API title
    description="API Description",        # API description
    version="0.1.0",                      # API version
    openapi_url="/openapi.json",          # OpenAPI schema path
    docs_url="/docs",                     # Swagger UI path
    redoc_url="/redoc",                   # ReDoc path
    debug=False,                          # Debug mode
)
```

## Server Configuration

### Development Server

Using Uvicorn (configured via command line):

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Options**:
- `--reload`: Enable auto-reload on code changes
- `--host`: Bind host (default: 127.0.0.1)
- `--port`: Bind port (default: 8000)
- `--workers`: Number of worker processes
- `--log-level`: Logging level (debug, info, warning, error, critical)

### Production Server

For production, use Gunicorn with Uvicorn workers:

```bash
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

## Test Configuration

### pytest Configuration

In `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
```

**Options**:
- `testpaths`: Directories to search for tests
- `python_files`: Test file naming pattern
- `python_classes`: Test class naming pattern
- `python_functions`: Test function naming pattern
- `addopts`: Default command-line options

## Environment-Specific Configuration

### Development

```bash
# .env.development
ENV=development
APP_NAME="FastAPI GH-AW Demo (Dev)"
DEBUG=true
LOG_LEVEL=debug
RELOAD=true
```

### Staging

```bash
# .env.staging
ENV=staging
APP_NAME="FastAPI GH-AW Demo (Staging)"
DEBUG=false
LOG_LEVEL=info
RELOAD=false
```

### Production

```bash
# .env.production
ENV=production
APP_NAME="FastAPI GH-AW Demo"
DEBUG=false
LOG_LEVEL=warning
RELOAD=false
```

## Future Configuration Options

The following settings may be added in future versions:

### Database

```python
DATABASE_URL: str = "sqlite:///./app.db"
DATABASE_POOL_SIZE: int = 5
DATABASE_MAX_OVERFLOW: int = 10
```

### Security

```python
SECRET_KEY: str = "your-secret-key"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
```

### CORS

```python
CORS_ORIGINS: list[str] = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS: bool = True
CORS_ALLOW_METHODS: list[str] = ["*"]
CORS_ALLOW_HEADERS: list[str] = ["*"]
```

### Rate Limiting

```python
RATE_LIMIT_PER_MINUTE: int = 60
RATE_LIMIT_ENABLED: bool = True
```

### Caching

```python
CACHE_ENABLED: bool = True
CACHE_TTL: int = 300  # seconds
REDIS_URL: str = "redis://localhost:6379"
```

### Logging

```python
LOG_LEVEL: str = "info"
LOG_FORMAT: str = "json"  # or "text"
LOG_FILE: Optional[str] = None
```

## Configuration Best Practices

1. **Use environment variables** for environment-specific settings
2. **Provide sensible defaults** for all configuration options
3. **Validate configuration** on application startup
4. **Document all options** with type hints and descriptions
5. **Never commit secrets** to version control
6. **Use .env.example** as a template
7. **Separate concerns** (app config, server config, external services)

## Using Pydantic Settings

For more robust configuration, consider using `pydantic-settings`:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = "development"
    DEBUG: bool = False
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

**Benefits**:
- Automatic type validation
- .env file loading
- Environment variable parsing
- Type hints and IDE support

## Configuration Validation

Example validation with Pydantic:

```python
from pydantic import Field, validator

class Settings(BaseSettings):
    ENV: str = Field(..., regex="^(development|staging|production)$")
    PORT: int = Field(default=8000, ge=1, le=65535)
    
    @validator("DATABASE_URL")
    def validate_database_url(cls, v):
        if not v or not v.startswith(("sqlite://", "postgresql://")):
            raise ValueError("Invalid database URL")
        return v
```

## Accessing Configuration

### In Route Handlers

```python
from app.core.config import settings

@router.get("/config")
def get_config():
    return {
        "app_name": settings.APP_NAME,
        "environment": settings.ENV
    }
```

### In Dependencies

```python
from fastapi import Depends
from app.core.config import settings

def get_settings():
    return settings

@router.get("/info")
def info(settings: Settings = Depends(get_settings)):
    return {"env": settings.ENV}
```

## See Also

- [How to Configure Environment Variables](../how-to/configure-env.md)
- [Project Structure](project-structure.md)
- [Architecture Explanation](../explanation/architecture.md)
