# FastAPI GH-AW Demo

A demonstration FastAPI application showcasing API development with automated workflows.

## Quick Start

### Prerequisites

- Python 3.12 or higher
- `uv` package manager (recommended) or `pip`

### Installation

```bash
# Clone the repository
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo

# Install dependencies
uv sync
# or with pip
pip install -e .
```

### Running the Application

```bash
# Start the development server
make run
# or
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Features

- FastAPI web framework for high-performance APIs
- Automatic interactive API documentation
- Type hints and validation with Pydantic
- Test suite with pytest
- Code quality tools (ruff for linting and formatting)

## Project Structure

```
fastapi-gh-aw-demo/
├── app/                  # Application code
│   ├── api/             # API routes and endpoints
│   ├── core/            # Core configuration
│   └── main.py          # Application entry point
├── tests/               # Test suite
├── docs/                # Documentation
├── pyproject.toml       # Project dependencies and configuration
└── Makefile             # Common development tasks
```

## Available Commands

```bash
make run      # Start the development server
make test     # Run the test suite
make lint     # Check code quality
make format   # Format code automatically
```

## Documentation

For detailed documentation, see the [docs/](docs/) directory:

- [Getting Started Tutorial](docs/tutorial.md)
- [API Reference](docs/reference.md)
- [How-To Guides](docs/how-to.md)
- [Architecture Explanation](docs/explanation.md)

## Development

### Running Tests

```bash
make test
# or
pytest -v
```

### Code Quality

```bash
# Check code style
make lint

# Auto-format code
make format
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
