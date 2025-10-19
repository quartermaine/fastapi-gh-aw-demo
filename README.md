# FastAPI GH-AW Demo

A demonstration FastAPI application showcasing best practices for API development with automated testing and GitHub Actions workflows.

## Overview

This project demonstrates a production-ready FastAPI application structure with:

- Clean project architecture
- API routing and endpoints
- Configuration management
- Automated testing with pytest
- Code quality with Ruff
- Development workflow automation

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
   
   Or with pip:
   ```bash
   pip install -r pyproject.toml
   ```

### Running the Application

Start the development server:

```bash
make run
```

Or directly with uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once running, visit:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## Development

### Running Tests

```bash
make test
```

### Code Quality

Check code with Ruff:
```bash
make lint
```

Auto-fix issues:
```bash
make format
```

## Project Structure

```
fastapi-gh-aw-demo/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and root endpoint
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py        # API route definitions
│   └── core/
│       ├── __init__.py
│       └── config.py        # Application configuration
├── tests/
│   ├── __init__.py
│   └── test_routes.py       # API endpoint tests
├── docs/                    # Documentation
├── main.py                  # CLI entry point
├── pyproject.toml           # Project metadata and dependencies
├── Makefile                 # Development commands
└── README.md               # This file
```

## Available Endpoints

### Root Endpoint
- **GET** `/` - Welcome message

### API Endpoints
- **GET** `/api/hello` - Greeting endpoint with optional name parameter
  - Query parameter: `name` (optional, default: "World")

## Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

- [Getting Started Tutorial](docs/tutorial.md) - Step-by-step guide for new users
- [How-To Guides](docs/how-to.md) - Common tasks and recipes
- [API Reference](docs/reference.md) - Complete API documentation
- [Architecture Explanation](docs/explanation.md) - Design decisions and concepts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
