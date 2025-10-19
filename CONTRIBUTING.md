# Contributing to FastAPI GH AW Demo

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions. We value diverse perspectives and welcome contributors of all backgrounds and experience levels.

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check existing issues to avoid duplicates
2. Verify the bug exists in the latest version
3. Collect relevant information (OS, Python version, error messages)

Create a bug report with:
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Error messages and logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Include:
- Clear description of the proposed feature
- Use cases and benefits
- Potential implementation approach
- Alternatives considered

### Pull Requests

1. **Fork the repository** and create a branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Ensure tests pass** and code is formatted
6. **Submit the pull request** with a clear description

## Development Setup

See the [Development Guide](./docs/development.md) for detailed setup instructions.

Quick start:
```bash
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo
uv sync
make test
```

## Coding Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Maximum line length: 88 characters
- Use double quotes for strings
- Format code with Ruff: `make format`

### Documentation
- Update documentation for API changes
- Include docstrings for public functions
- Add code examples where helpful
- Follow the [Documentation Style Guide](./docs/README.md#documentation-style-guide)

### Testing
- Write tests for new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow existing test patterns

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(api): add user authentication endpoint

Implements JWT-based authentication with access and refresh tokens.
Includes middleware for protected routes.

Closes #42
```

## Pull Request Process

1. **Update documentation** if you've changed APIs or added features
2. **Update the README** if needed
3. **Add tests** and ensure all tests pass
4. **Run linting**: `make lint`
5. **Format code**: `make format`
6. **Write clear PR description** explaining changes and motivation
7. **Link related issues** using "Closes #issue-number"
8. **Request review** from maintainers
9. **Address feedback** promptly and respectfully

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No linting errors

## Project Structure

```
fastapi-gh-aw-demo/
├── app/                  # Application code
│   ├── api/             # API routes
│   ├── core/            # Core functionality
│   ├── models/          # Data models
│   ├── schemas/         # Pydantic schemas
│   └── services/        # Business logic
├── tests/               # Test suite
├── docs/                # Documentation
├── .github/             # GitHub workflows
└── pyproject.toml       # Project configuration
```

## Testing

Run tests:
```bash
make test
```

Run with coverage:
```bash
pytest --cov=app --cov-report=html
```

## Documentation

All documentation is in Markdown format in the `docs/` directory, following the [Diátaxis framework](https://diataxis.fr/):

- **Tutorials**: Learning-oriented, hands-on guides
- **How-to guides**: Problem-oriented, practical steps
- **Reference**: Information-oriented, technical details
- **Explanation**: Understanding-oriented, clarification

**Automated Documentation**: The project uses an automated workflow that monitors code changes and creates pull requests for documentation updates. When you make code changes, the workflow may automatically suggest documentation improvements. See the [Automation Guide](./docs/automation.md) for details.

See the [Documentation README](./docs/README.md) for more details.

## Review Process

### What We Look For

- **Correctness**: Code works as intended
- **Tests**: Adequate test coverage
- **Documentation**: Clear and complete
- **Style**: Follows project conventions
- **Performance**: No unnecessary performance impact
- **Security**: No security vulnerabilities

### Timeline

- Initial review: Within 1 week
- Follow-up reviews: Within 3 days
- Merging: After approval from maintainers

## Getting Help

- **Questions**: Open a [discussion](https://github.com/quartermaine/fastapi-gh-aw-demo/discussions)
- **Bugs**: Create an [issue](https://github.com/quartermaine/fastapi-gh-aw-demo/issues)
- **Unclear documentation**: Suggest improvements via PR or issue

## Recognition

Contributors are recognized in:
- GitHub contributor graph
- Release notes for significant contributions
- Project README (for major contributions)

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

## Questions?

Don't hesitate to ask questions! We're here to help:
- Open a [discussion](https://github.com/quartermaine/fastapi-gh-aw-demo/discussions)
- Comment on relevant issues
- Reach out to maintainers

Thank you for contributing to FastAPI GH AW Demo! 🎉
