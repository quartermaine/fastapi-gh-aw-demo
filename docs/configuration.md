# Configuration Guide

This guide explains how to configure the FastAPI GH AW Demo application for different environments and use cases.

## Configuration Overview

The application uses environment variables and a settings class for configuration management, following the [12-factor app methodology](https://12factor.net/).

## Settings Module

Configuration is centralized in `app/core/config.py`:

```python
import os

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

## Environment Variables

### Available Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `ENV` | string | `"development"` | Application environment (development, staging, production) |

### Setting Environment Variables

#### Linux/macOS

Temporary (current shell session):
```bash
export ENV=production
```

Permanent (add to `~/.bashrc` or `~/.zshrc`):
```bash
echo 'export ENV=production' >> ~/.bashrc
source ~/.bashrc
```

#### Windows

Temporary (current command prompt):
```cmd
set ENV=production
```

Permanent (via System Properties or):
```powershell
[System.Environment]::SetEnvironmentVariable('ENV', 'production', 'User')
```

#### Using .env Files

Create a `.env` file in the project root:

```env
ENV=production
DEBUG=false
```

**Important**: Never commit `.env` files to version control. They're already in `.gitignore`.

To load `.env` files automatically, install python-dotenv:

```bash
uv add python-dotenv
```

Update `app/core/config.py`:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

## Environment-Specific Configuration

### Development Environment

Default configuration suitable for local development:

```python
class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    RELOAD: bool = True
```

Run with:
```bash
make run
```

### Production Environment

Recommended production configuration:

```env
ENV=production
DEBUG=false
LOG_LEVEL=INFO
RELOAD=false
```

Run with:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing Environment

Configuration for running tests:

```python
class TestSettings(Settings):
    ENV: str = "testing"
    DEBUG: bool = False
```

## Advanced Configuration

### Using Pydantic Settings

For more robust configuration with validation, use Pydantic's `BaseSettings`:

Install pydantic-settings:
```bash
uv add pydantic-settings
```

Update `app/core/config.py`:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    
    app_name: str = "FastAPI GH-AW Demo"
    env: str = "development"
    debug: bool = False
    log_level: str = "INFO"
    
    # API Configuration
    api_prefix: str = "/api"
    api_version: str = "v1"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False
    workers: int = 1

settings = Settings()
```

### Type Validation

Pydantic automatically validates types:

```python
class Settings(BaseSettings):
    port: int = 8000  # Must be integer
    debug: bool = False  # Converts "true"/"false" strings
    timeout: float = 30.0  # Must be numeric
    allowed_hosts: list[str] = ["localhost"]  # Validates list
```

### Secrets Management

For sensitive data, use environment variables or secret management services:

```python
class Settings(BaseSettings):
    # Database
    database_url: str = ""
    
    # API Keys
    api_key: str = ""
    secret_key: str = ""
    
    # Never set defaults for secrets!
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )
```

**Security Best Practices**:
1. Never commit secrets to version control
2. Use different secrets per environment
3. Rotate secrets regularly
4. Use secret management services (AWS Secrets Manager, HashiCorp Vault, etc.)

## Application Startup Configuration

### FastAPI App Configuration

Configure FastAPI in `app/main.py`:

```python
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="FastAPI GH AW Demo Application",
    docs_url="/docs" if settings.debug else None,  # Disable docs in production
    redoc_url="/redoc" if settings.debug else None,
    openapi_url="/openapi.json" if settings.debug else None,
)
```

### CORS Configuration

Enable Cross-Origin Resource Sharing:

```python
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Development: Allow all origins
if settings.env == "development":
    origins = ["*"]
else:
    # Production: Specify allowed origins
    origins = [
        "https://yourdomain.com",
        "https://app.yourdomain.com",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Logging Configuration

Configure logging based on environment:

```python
import logging
from app.core.config import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
```

## Server Configuration

### Uvicorn Options

Common uvicorn configuration options:

```bash
# Development
uvicorn app.main:app \
  --reload \
  --host 127.0.0.1 \
  --port 8000 \
  --log-level debug

# Production
uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4 \
  --log-level info \
  --access-log \
  --proxy-headers \
  --forwarded-allow-ips='*'
```

### Gunicorn with Uvicorn Workers

For production, use Gunicorn with Uvicorn workers:

```bash
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile - \
  --error-logfile -
```

## Docker Configuration

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=production
      - DEBUG=false
      - LOG_LEVEL=info
    volumes:
      - ./app:/app/app
    restart: unless-stopped
```

## Configuration Validation

### Startup Checks

Add validation in `app/main.py`:

```python
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

@app.on_event("startup")
def validate_config():
    """Validate configuration on startup"""
    logger.info(f"Starting application in {settings.env} mode")
    
    if settings.env == "production":
        if settings.debug:
            raise ValueError("DEBUG should be False in production")
        if not settings.secret_key:
            raise ValueError("SECRET_KEY must be set in production")
    
    logger.info("Configuration validated successfully")
```

## Configuration Examples

### Local Development

`.env.development`:
```env
ENV=development
DEBUG=true
LOG_LEVEL=DEBUG
RELOAD=true
HOST=127.0.0.1
PORT=8000
```

### Staging Environment

`.env.staging`:
```env
ENV=staging
DEBUG=false
LOG_LEVEL=INFO
RELOAD=false
HOST=0.0.0.0
PORT=8000
```

### Production Environment

`.env.production`:
```env
ENV=production
DEBUG=false
LOG_LEVEL=WARNING
RELOAD=false
HOST=0.0.0.0
PORT=8000
WORKERS=4
```

## Best Practices

1. **Never commit secrets**: Use environment variables or secret management
2. **Use type validation**: Leverage Pydantic for configuration validation
3. **Environment-specific configs**: Maintain separate configurations per environment
4. **Document all settings**: Keep this guide updated with new configuration options
5. **Fail fast**: Validate critical settings on startup
6. **Use sensible defaults**: Provide defaults for non-sensitive settings
7. **Follow 12-factor principles**: Configuration in environment, not code

## Troubleshooting

### Environment Variables Not Loading

1. Check `.env` file exists and is in project root
2. Verify python-dotenv is installed
3. Ensure `.env` is loaded before Settings initialization
4. Check for typos in variable names

### Type Validation Errors

When using Pydantic Settings, ensure types match:
```python
# Wrong
ENV=8000  # Should be string like "development"

# Correct
PORT=8000  # Numeric value for port
ENV=development  # String value for env
```

### Configuration Not Applied

1. Restart the application after changing configuration
2. Check environment variable precedence
3. Verify settings are imported correctly in application code

## Additional Resources

- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [FastAPI Configuration](https://fastapi.tiangolo.com/advanced/settings/)
- [12-Factor App](https://12factor.net/)
- [Uvicorn Deployment](https://www.uvicorn.org/deployment/)
