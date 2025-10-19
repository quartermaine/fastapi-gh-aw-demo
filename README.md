# FastAPI GitHub Actions Workflow Demo

A demonstration FastAPI application showcasing automated workflows, testing, and documentation practices.

## Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo

# Install dependencies
uv sync
```

### Running the Application

```bash
# Development mode with auto-reload
make run

# Or directly with uvicorn
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Testing

```bash
# Run tests
make test

# Run linting
make lint

# Format code
make format
```

## Project Structure

```
fastapi-gh-aw-demo/
├── app/
│   ├── api/          # API routes and endpoints
│   ├── core/         # Core functionality and configuration
│   └── main.py       # Application entry point
├── docs/             # Documentation
├── tests/            # Test suite
├── pyproject.toml    # Project configuration
└── Makefile          # Common tasks
```

## Documentation

Complete documentation is available in the [docs/](docs/) directory:

- [Getting Started Tutorial](docs/tutorial.md)
- [How-to Guides](docs/how-to/)
- [API Reference](docs/reference/)
- [Architecture Explanation](docs/explanation/)

## API Endpoints

### Root Endpoint
- **GET** `/` - Welcome message

### API Routes
- **GET** `/api/hello?name={name}` - Personalized greeting

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI) or `http://localhost:8000/redoc` for alternative documentation.

## Development

### Code Style

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting with the following configuration:

- Line length: 88 characters
- Target Python version: 3.11+
- Import sorting enabled

### Running Tests

Tests are written using pytest and the FastAPI TestClient:

```bash
pytest -v
```

### Environment Variables

Configure the application using environment variables:

- `ENV` - Environment name (default: "development")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please ensure:

1. Tests pass (`make test`)
2. Code is formatted (`make format`)
3. Linting passes (`make lint`)
4. Documentation is updated
