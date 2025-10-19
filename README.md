# FastAPI GH AW Demo

A demonstration FastAPI application showcasing GitHub Actions workflow automation.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Modular Architecture**: Clean separation of concerns with organized project structure
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
gh auth login --web -h github.com
````

### 2️⃣ Install the GitHub Agentic Workflows extension

```bash
gh extension install githubnext/gh-aw
```

### 3️⃣ Add a sample workflow

```bash
gh aw add githubnext/agentics/update-docs
```

### 4️⃣ Compile the workflow

```bash
gh aw compile
```

### 5️⃣ Run the workflow (and auto-merge PRs)

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
- [Getting Started Tutorial](./docs/tutorial.md)
- [API Reference](./docs/api-reference.md)
- [Development Guide](./docs/development.md)
- [Configuration Guide](./docs/configuration.md)

## Development

This project uses:
- **FastAPI**: Web framework
- **uvicorn**: ASGI server
- **pytest**: Testing framework
- **Ruff**: Linting and formatting
- **httpx**: HTTP client for testing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
