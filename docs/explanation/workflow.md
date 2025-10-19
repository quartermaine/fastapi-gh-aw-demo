# Development Workflow

This document describes the development workflow for contributing to the FastAPI GitHub Actions Workflow Demo project.

## Overview

The project follows a **trunk-based development** workflow with feature branches and pull requests for all changes.

```
main ──┬──> feature/add-endpoint ──> PR ──> merge ──> main
       └──> docs/update-readme ──> PR ──> merge ──> main
```

## Daily Development Cycle

### 1. Start Your Work

```bash
# Update main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Edit code following the project conventions:

```bash
# Edit files
vim app/api/routes.py

# Run the application to test
make run
```

### 3. Write Tests

Always write tests for new features:

```bash
# Edit test file
vim tests/test_routes.py

# Run tests
make test
```

### 4. Format and Lint

Ensure code quality:

```bash
# Format code
make format

# Check linting
make lint
```

### 5. Commit Changes

Write clear commit messages:

```bash
# Stage changes
git add app/api/routes.py tests/test_routes.py

# Commit with descriptive message
git commit -m "Add new endpoint for user management"
```

### 6. Push and Create PR

```bash
# Push to remote
git push origin feature/your-feature-name

# Create pull request on GitHub
gh pr create --title "Add user management endpoint" \
  --body "Adds GET /api/users endpoint with pagination"
```

### 7. Address Review Comments

```bash
# Make requested changes
vim app/api/routes.py

# Commit changes
git add app/api/routes.py
git commit -m "Address review comments"

# Push updates
git push origin feature/your-feature-name
```

### 8. Merge

Once approved, merge the PR:
- Use "Squash and merge" for clean history
- Delete branch after merge

## Branch Naming Conventions

Use descriptive branch names with prefixes:

### Feature Branches
```
feature/add-user-authentication
feature/implement-caching
feature/database-integration
```

### Bug Fixes
```
fix/handle-empty-response
fix/validation-error
fix/memory-leak
```

### Documentation
```
docs/update-api-reference
docs/add-tutorial
docs/fix-typos
```

### Refactoring
```
refactor/simplify-routes
refactor/extract-service-layer
refactor/improve-error-handling
```

### Tests
```
test/add-integration-tests
test/improve-coverage
test/add-edge-cases
```

## Commit Message Guidelines

Follow the **Conventional Commits** specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat(api): add user registration endpoint"

# Bug fix
git commit -m "fix(routes): handle missing query parameters"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Refactoring
git commit -m "refactor(config): use Pydantic settings"

# Tests
git commit -m "test(routes): add tests for error cases"
```

### Multi-line Commits

```bash
git commit -m "feat(api): add user authentication

Implements JWT-based authentication for API endpoints.

- Add login endpoint
- Add token generation
- Add protected route decorator

Closes #123"
```

## Pull Request Process

### 1. Create PR

Include in your PR:
- **Clear title**: Describe what the PR does
- **Description**: Why the change is needed
- **Testing**: How you tested the changes
- **Screenshots**: For UI changes (if applicable)

Example PR description:
```markdown
## Description
Adds user authentication using JWT tokens.

## Changes
- New `/api/login` endpoint
- JWT token generation
- Protected route decorator

## Testing
- Added unit tests for auth functions
- Manual testing with Postman
- All existing tests pass

## Checklist
- [x] Tests added
- [x] Documentation updated
- [x] Linting passes
- [x] No breaking changes
```

### 2. Automated Checks

PRs trigger automated checks:
- **Tests**: All tests must pass
- **Linting**: Code must pass linting
- **Documentation**: Docs are built successfully

### 3. Code Review

At least one approval required:
- Reviewer checks code quality
- Suggests improvements
- Approves or requests changes

### 4. Address Feedback

```bash
# Make requested changes
vim app/api/routes.py

# Commit
git commit -m "Address review feedback"

# Push
git push
```

### 5. Merge

After approval:
- Use **Squash and merge** for clean history
- Delete branch automatically
- PR closes linked issues

## Local Development Setup

### Initial Setup

```bash
# Clone repository
git clone https://github.com/quartermaine/fastapi-gh-aw-demo.git
cd fastapi-gh-aw-demo

# Install dependencies
uv sync

# Create .env file
cp .env.example .env

# Run tests
make test

# Start development server
make run
```

### Development Environment

Recommended tools:
- **Python 3.12+**: Latest Python version
- **uv**: Fast package manager
- **VS Code**: With Python extension
- **Git**: Version control
- **make**: Task automation

### IDE Configuration

#### VS Code Settings

Create `.vscode/settings.json`:

```json
{
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "none",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false
}
```

## Testing Workflow

### Before Committing

```bash
# Run all tests
make test

# Run specific test
pytest tests/test_routes.py::test_hello -v

# Run with coverage
pytest --cov=app --cov-report=html
```

### Writing Tests

Follow the AAA pattern:

```python
def test_create_user():
    # Arrange
    user_data = {"username": "test"}
    
    # Act
    response = client.post("/api/users", json=user_data)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["username"] == "test"
```

### Test Coverage

Aim for >80% coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

## Code Quality Workflow

### Linting

```bash
# Check for issues
make lint

# Auto-fix issues
make format

# Check specific file
ruff check app/api/routes.py
```

### Type Checking (Future)

```bash
# Install mypy
uv add --dev mypy

# Run type checking
mypy app/
```

## Documentation Workflow

### When to Update Docs

Update documentation when:
- Adding new features
- Changing APIs
- Fixing bugs that affect usage
- Adding configuration options

### Documentation Types

Follow Diátaxis:
- **Tutorial**: For new features that change getting started
- **How-to**: For new procedures or tasks
- **Reference**: For API changes
- **Explanation**: For architectural changes

### Documentation Review

Documentation PRs should include:
- Clear explanations
- Code examples
- Updated navigation
- Spell-checked content

## Release Workflow

### Version Numbering

Follow **Semantic Versioning**:

- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features (1.0.0 → 1.1.0)
- **PATCH**: Bug fixes (1.0.0 → 1.0.1)

### Release Process

```bash
# Update version in pyproject.toml
vim pyproject.toml

# Commit version bump
git commit -m "chore: bump version to 1.1.0"

# Create tag
git tag -a v1.1.0 -m "Release version 1.1.0"

# Push tag
git push origin v1.1.0

# Create GitHub release
gh release create v1.1.0 --title "Version 1.1.0" \
  --notes "Release notes here"
```

## Continuous Integration

### GitHub Actions Workflows

Workflows run automatically:

1. **Test**: On every push and PR
2. **Lint**: On every push and PR
3. **Documentation**: On pushes to main
4. **Release**: On version tags

### Workflow Files

Located in `.github/workflows/`:
- `test.yml`: Run tests
- `lint.yml`: Check code quality
- `update-docs.yml`: Update documentation

## Troubleshooting

### Tests Failing Locally

```bash
# Clean Python cache
find . -type d -name __pycache__ -exec rm -rf {} +

# Reinstall dependencies
uv sync --force

# Run tests with verbose output
pytest -vv
```

### Import Errors

```bash
# Ensure correct Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Verify Python version
python --version
```

### Git Issues

```bash
# Sync with main
git checkout main
git pull origin main
git checkout your-branch
git rebase main

# Resolve conflicts
git status
# Edit conflicted files
git add .
git rebase --continue
```

## Best Practices

### Code

1. **Keep changes small**: Easier to review
2. **One concern per commit**: Easier to understand
3. **Write tests first**: Test-driven development
4. **Use type hints**: Better IDE support
5. **Follow conventions**: Consistency matters

### Commits

1. **Atomic commits**: One logical change per commit
2. **Clear messages**: Describe what and why
3. **Reference issues**: Link to issue numbers
4. **Test before commit**: Ensure tests pass

### PRs

1. **Small PRs**: Easier to review
2. **Good description**: Context for reviewers
3. **Update docs**: Keep docs current
4. **Respond to feedback**: Engage with reviewers

### Documentation

1. **Update with code**: Don't let docs lag
2. **Examples**: Include code examples
3. **Clear language**: Write for your audience
4. **Review**: Check for accuracy

## Collaboration

### Communication

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **PRs**: For code review
- **Commits**: For change documentation

### Getting Help

1. Check existing documentation
2. Search issues and discussions
3. Ask in GitHub Discussions
4. Create an issue if needed

## See Also

- [Architecture](architecture.md)
- [Design Decisions](design-decisions.md)
- [How to Run Tests](../how-to/run-tests.md)
- [How to Add Endpoints](../how-to/add-endpoint.md)
