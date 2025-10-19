# FastAPI GitHub Actions Workflow Demo

A demonstration project showcasing FastAPI integration with GitHub Actions workflows for automated documentation updates.

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run the development server
make run

# Run tests
make test

# Lint code
make lint
```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/docs`.

## Project Overview

This project demonstrates a modern FastAPI application structure with:

- RESTful API endpoints
- Automated testing with pytest
- Code quality tools (Ruff)
- GitHub Actions integration
- Automated documentation workflows

## Documentation

Comprehensive documentation is available in the [`docs/`](./docs) directory:

- [Getting Started Tutorial](./docs/tutorial.md) - Step-by-step guide for new users
- [How-To Guides](./docs/how-to-guides.md) - Practical guides for common tasks
- [API Reference](./docs/reference.md) - Complete API documentation
- [Architecture Explanation](./docs/explanation.md) - Understanding the project design

## Project Structure

```
fastapi-gh-aw-demo/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── api/
│   │   └── routes.py    # API route definitions
│   └── core/
│       └── config.py    # Application configuration
├── tests/
│   └── test_routes.py   # API endpoint tests
├── docs/                # Documentation
├── main.py              # CLI entry point
├── Makefile             # Development commands
└── pyproject.toml       # Project dependencies and configuration
```

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Type Hints**: Full Python type hint support for better IDE integration
- **Automatic Documentation**: Interactive API docs via Swagger UI and ReDoc
- **Testing**: Comprehensive test suite with pytest
- **Code Quality**: Automated formatting and linting with Ruff
- **GitHub Actions**: Automated workflows for documentation updates

## Requirements

- Python 3.12 or higher
- Dependencies managed via `pyproject.toml`

## Development

### Running the Application

```bash
# Development mode with auto-reload
make run
```

### Running Tests

```bash
# Run all tests with verbose output
make test
```

### Code Quality

```bash
# Check code style
make lint

# Auto-fix formatting issues
make format
```

## API Endpoints

- `GET /` - Welcome message
- `GET /api/hello?name={name}` - Personalized greeting
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Contributing

Contributions are welcome! Please ensure:

1. All tests pass (`make test`)
2. Code follows style guidelines (`make lint`)
3. Documentation is updated for new features
4. Commit messages are clear and descriptive

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
