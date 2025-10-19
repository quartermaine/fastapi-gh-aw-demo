# How to Configure Environment Variables

This guide explains how to configure the application using environment variables.

## Quick Start

Create a `.env` file in the project root:

```bash
# .env
ENV=production
APP_NAME="My FastAPI App"
```

Load environment variables before running:

```bash
export $(cat .env | xargs)
uvicorn app.main:app
```

## Current Configuration Settings

The application supports the following environment variables (defined in `app/core/config.py`):

### APP_NAME
- **Description**: Application name
- **Default**: `"FastAPI GH-AW Demo"`
- **Example**: `APP_NAME="Production API"`

### ENV
- **Description**: Environment name (development, staging, production)
- **Default**: `"development"`
- **Example**: `ENV=production`

## Creating a .env File

### Step 1: Create the File

Create a `.env` file in the project root:

```bash
touch .env
```

### Step 2: Add Variables

Edit `.env` and add your configuration:

```bash
# Application settings
ENV=development
APP_NAME="FastAPI GH-AW Demo"

# Server settings (future use)
HOST=0.0.0.0
PORT=8000

# Database settings (future use)
DATABASE_URL=sqlite:///./app.db
```

### Step 3: Load Variables

#### Option 1: Using python-dotenv

Install python-dotenv:

```bash
uv add python-dotenv
```

Update `app/core/config.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI GH-AW Demo")
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

#### Option 2: Manual Export

```bash
export $(cat .env | xargs)
uvicorn app.main:app
```

#### Option 3: Using direnv

Install direnv and create `.envrc`:

```bash
# .envrc
export ENV=development
export APP_NAME="FastAPI GH-AW Demo"
```

Allow the directory:

```bash
direnv allow
```

## Different Environments

### Development

Create `.env.development`:

```bash
ENV=development
APP_NAME="FastAPI GH-AW Demo (Dev)"
DEBUG=true
LOG_LEVEL=debug
```

### Production

Create `.env.production`:

```bash
ENV=production
APP_NAME="FastAPI GH-AW Demo"
DEBUG=false
LOG_LEVEL=info
```

### Load Specific Environment

```bash
# Load development
export $(cat .env.development | xargs)

# Load production
export $(cat .env.production | xargs)
```

## Using Pydantic Settings

For more robust configuration management, use Pydantic's BaseSettings:

### Step 1: Install pydantic-settings

```bash
uv add pydantic-settings
```

### Step 2: Update Configuration

Update `app/core/config.py`:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = "development"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: Optional[str] = None
    
    # Logging
    LOG_LEVEL: str = "info"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

### Step 3: Access Settings

```python
from app.core.config import settings

print(settings.APP_NAME)
print(settings.ENV)
```

## Environment-Specific Settings

Use Pydantic's env_file parameter for different environments:

```python
import os

env = os.getenv("ENV", "development")
env_file = f".env.{env}"

class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    
    class Config:
        env_file = env_file
        
settings = Settings()
```

## Secret Management

### Never Commit Secrets

Add to `.gitignore`:

```gitignore
# Environment files
.env
.env.*
!.env.example

# Secrets
secrets/
*.key
*.pem
```

### Create .env.example

Create a template for other developers:

```bash
# .env.example
ENV=development
APP_NAME="FastAPI GH-AW Demo"

# Add your database URL
DATABASE_URL=

# Add your API keys
API_KEY=
SECRET_KEY=
```

### Using GitHub Secrets

For GitHub Actions workflows:

1. Go to repository Settings > Secrets and variables > Actions
2. Add secrets (e.g., `DATABASE_URL`, `API_KEY`)
3. Reference in workflows:

```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}
```

## Validation

Validate required environment variables on startup:

```python
from pydantic_settings import BaseSettings
from pydantic import Field, validator

class Settings(BaseSettings):
    APP_NAME: str = Field(..., min_length=1)
    ENV: str = Field(..., regex="^(development|staging|production)$")
    DATABASE_URL: str = Field(..., min_length=1)
    
    @validator("ENV")
    def validate_env(cls, v):
        allowed = ["development", "staging", "production"]
        if v not in allowed:
            raise ValueError(f"ENV must be one of {allowed}")
        return v
    
    class Config:
        env_file = ".env"

settings = Settings()
```

## Common Patterns

### Database Configuration

```bash
# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# SQLite
DATABASE_URL=sqlite:///./app.db

# MySQL
DATABASE_URL=mysql://user:password@localhost:3306/dbname
```

### API Keys

```bash
OPENAI_API_KEY=sk-...
STRIPE_API_KEY=sk_test_...
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
```

### Feature Flags

```bash
ENABLE_CACHING=true
ENABLE_ANALYTICS=false
FEATURE_NEW_UI=true
```

## Testing with Environment Variables

### In Tests

```python
import os
import pytest

def test_with_env_var():
    os.environ["ENV"] = "test"
    # Test code
    assert os.getenv("ENV") == "test"

@pytest.fixture
def test_settings():
    os.environ["ENV"] = "test"
    os.environ["APP_NAME"] = "Test App"
    yield
    # Cleanup
    del os.environ["ENV"]
    del os.environ["APP_NAME"]
```

### Using pytest-env

Install:

```bash
uv add --dev pytest-env
```

Configure in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
env = [
    "ENV=test",
    "APP_NAME=Test App",
]
```

## Troubleshooting

### Variables Not Loading

1. Check file location (should be in project root)
2. Verify file name (`.env`, not `env` or `.env.txt`)
3. Check for syntax errors (no spaces around `=`)
4. Ensure python-dotenv is installed

### Wrong Values

1. Check for duplicate definitions
2. Verify environment variable precedence
3. Check for typos in variable names

### Security Issues

1. Never commit `.env` files
2. Use `.env.example` templates
3. Rotate secrets regularly
4. Use GitHub Secrets for CI/CD

## See Also

- [Configuration Reference](../reference/configuration.md)
- [Deployment Guide](deploy.md)
- [Architecture Explanation](../explanation/architecture.md)
