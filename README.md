# FastAPI GH AW Demo

A demonstration FastAPI application showcasing GitHub Actions workflow automation.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Modular Architecture**: Clean separation of concerns with organized project structure
- **Automated Documentation**: AI-powered workflow keeps documentation synchronized with code
- **Testing**: Comprehensive test suite using pytest
- **Code Quality**: Automated linting and formatting with Ruff
- **Development Tools**: Quick development commands via Makefile

## Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
```

2. Install dependencies:
```bash
uv sync
```

### Running the Application

Start the development server:
```bash
make run
```

The API will be available at `http://localhost:8000`.

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Running Tests

Execute the test suite:
```bash
make test
```

### Code Quality

Check code with linting:
```bash
make lint
```

Auto-fix code issues:
```bash
make format
```

## Project Structure

```
fastapi-gh-aw-demo/
├── app/                    # Application package
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── api/               # API routes
│   │   ├── __init__.py
│   │   └── routes.py      # API endpoint definitions
│   └── core/              # Core functionality
│       ├── __init__.py
│       └── config.py      # Application configuration
├── tests/                 # Test suite
│   ├── __init__.py
│   └── test_routes.py     # API endpoint tests
├── docs/                  # Documentation
├── pyproject.toml         # Project metadata and dependencies
├── Makefile              # Development commands
└── README.md             # This file
```

## API Endpoints

### Root Endpoint
- **GET** `/` - Welcome message

### Demo API
- **GET** `/api/hello?name={name}` - Personalized greeting

## Documentation

For detailed documentation, see the [docs](./docs) directory:
- [Getting Started Tutorial](./docs/tutorial.md) - Step-by-step introduction
- [API Reference](./docs/api-reference.md) - Complete endpoint specifications
- [Development Guide](./docs/development.md) - Contribution guidelines and workflow
- [Configuration Guide](./docs/configuration.md) - Environment setup and deployment
- [Automation Guide](./docs/automation.md) - Understanding GitHub Actions workflows

## Development

This project uses:
- **FastAPI**: Web framework
- **uvicorn**: ASGI server
- **pytest**: Testing framework
- **Ruff**: Linting and formatting
- **httpx**: HTTP client for testing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
