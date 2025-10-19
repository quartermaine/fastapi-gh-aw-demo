# Application Architecture

This document explains the architectural design and structure of the FastAPI GitHub Actions Workflow Demo application.

## Architecture Overview

The application follows a **layered architecture** pattern with clear separation of concerns:

```
┌─────────────────────────────────────┐
│        Presentation Layer           │
│    (FastAPI Routes & Endpoints)     │
├─────────────────────────────────────┤
│         Business Layer              │
│      (Future: Services/Logic)       │
├─────────────────────────────────────┤
│          Data Layer                 │
│     (Future: Models/Database)       │
├─────────────────────────────────────┤
│          Core Layer                 │
│    (Configuration & Utilities)      │
└─────────────────────────────────────┘
```

## Core Principles

### 1. Separation of Concerns

Each component has a single, well-defined responsibility:
- **Routes** handle HTTP requests and responses
- **Core** manages configuration and shared utilities
- **Tests** verify behavior without coupling to implementation

### 2. Dependency Injection

FastAPI's dependency injection system enables:
- Testable code
- Reusable components
- Clear dependencies

### 3. Progressive Enhancement

The application starts simple and can grow:
- Add database layer when needed
- Implement business logic as required
- Extend with middleware, authentication, etc.

## Layer Details

### Presentation Layer (API)

**Location**: `app/api/`

**Responsibilities**:
- Define HTTP endpoints
- Validate request data
- Serialize responses
- Handle HTTP-specific concerns

**Current Structure**:
```python
# app/api/routes.py
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["demo"])

@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
```

**Design Decisions**:
- Use `APIRouter` for modularity
- Group related endpoints together
- Keep route handlers thin (delegate to services)

### Business Layer

**Location**: `app/services/` (future)

**Responsibilities**:
- Implement business logic
- Coordinate between layers
- Handle complex operations

**Future Example**:
```python
# app/services/user_service.py
class UserService:
    def __init__(self, db: Database):
        self.db = db
    
    def create_user(self, username: str) -> User:
        # Business logic here
        pass
```

### Data Layer

**Location**: `app/models/` and `app/database/` (future)

**Responsibilities**:
- Define data models
- Database operations
- Data validation

**Future Example**:
```python
# app/models/user.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
```

### Core Layer

**Location**: `app/core/`

**Responsibilities**:
- Application configuration
- Shared utilities
- Common dependencies

**Current Structure**:
```python
# app/core/config.py
class Settings:
    APP_NAME: str = "FastAPI GH-AW Demo"
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
```

## Request Flow

### Simple Request Flow

```
1. HTTP Request → 2. FastAPI Router → 3. Route Handler → 4. Response
```

Example:
```
GET /api/hello?name=Agent
    ↓
router.get("/hello")
    ↓
hello(name="Agent")
    ↓
{"message": "Hello, Agent!"}
```

### Future Complex Request Flow

```
1. HTTP Request
    ↓
2. Middleware (CORS, Auth, etc.)
    ↓
3. Route Handler
    ↓
4. Service Layer (Business Logic)
    ↓
5. Repository/Database
    ↓
6. Response Serialization
    ↓
7. HTTP Response
```

## Component Interaction

### Current Architecture

```
┌──────────────┐
│   main.py    │ ← Application Entry Point
└──────┬───────┘
       │
       ├──> routes.py ← API Endpoints
       │
       └──> config.py ← Configuration
```

### Future Architecture

```
┌──────────────┐
│   main.py    │
└──────┬───────┘
       │
       ├──> api/
       │    ├── routes.py
       │    └── dependencies.py
       │
       ├──> services/
       │    ├── user_service.py
       │    └── auth_service.py
       │
       ├──> models/
       │    ├── user.py
       │    └── base.py
       │
       ├──> database/
       │    ├── session.py
       │    └── repository.py
       │
       └──> core/
            ├── config.py
            ├── security.py
            └── exceptions.py
```

## Design Patterns

### 1. Router Pattern

Organize endpoints using APIRouter:

```python
# app/api/user_routes.py
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users(): ...

@router.post("/")
def create_user(): ...

@router.get("/{user_id}")
def get_user(user_id: int): ...
```

Register in main app:
```python
# app/main.py
from app.api.user_routes import router as user_router

app.include_router(user_router)
```

### 2. Dependency Injection

Share resources and configuration:

```python
from fastapi import Depends
from app.core.config import settings

def get_settings():
    return settings

@router.get("/info")
def info(config: Settings = Depends(get_settings)):
    return {"env": config.ENV}
```

### 3. Repository Pattern (Future)

Abstract data access:

```python
# app/database/repository.py
class UserRepository:
    def get_by_id(self, user_id: int) -> User:
        # Database query
        pass
    
    def create(self, user: UserCreate) -> User:
        # Database insert
        pass
```

### 4. Service Pattern (Future)

Encapsulate business logic:

```python
# app/services/user_service.py
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def register_user(self, username: str, email: str) -> User:
        # Validation, business rules
        return self.repository.create(User(username=username, email=email))
```

## Configuration Management

### Current Approach

Simple environment-based configuration:

```python
class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI GH-AW Demo")
    ENV: str = os.getenv("ENV", "development")
```

### Recommended Approach

Use Pydantic BaseSettings for type safety:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"
```

## Error Handling

### Current Approach

FastAPI's automatic error handling:
- 404 for missing routes
- 422 for validation errors

### Future Error Handling

Custom exception handlers:

```python
# app/core/exceptions.py
class UserNotFoundError(Exception):
    pass

# app/main.py
@app.exception_handler(UserNotFoundError)
async def user_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "User not found"}
    )
```

## Testing Strategy

### Test Pyramid

```
        ┌─────────┐
        │  E2E    │  ← Few
        ├─────────┤
        │ Integr. │  ← Some
        ├─────────┤
        │  Unit   │  ← Many
        └─────────┘
```

### Current Testing

Integration tests using TestClient:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_hello():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
```

### Future Testing

Unit tests for services and repositories:

```python
def test_user_service_create():
    service = UserService(mock_repository)
    user = service.create_user("test")
    assert user.username == "test"
```

## Scalability Considerations

### Horizontal Scaling

The stateless architecture supports horizontal scaling:
- Deploy multiple instances
- Use load balancer
- Share session state (Redis, database)

### Vertical Scaling

Optimize for single-instance performance:
- Use async/await for I/O operations
- Connection pooling for databases
- Caching for expensive operations

### Database Scaling

Future considerations:
- Read replicas for queries
- Connection pooling
- Query optimization
- Caching layer

## Security Architecture

### Current Security

- No authentication (development only)
- FastAPI's built-in validation

### Future Security

```
Request
   ↓
Middleware (Rate Limiting)
   ↓
Authentication (JWT)
   ↓
Authorization (Permissions)
   ↓
Route Handler
   ↓
Response
```

## Performance Considerations

### Current Performance

FastAPI is inherently fast:
- Async support
- Automatic validation
- Efficient serialization

### Optimization Strategies

1. **Async Operations**: Use `async def` for I/O-bound operations
2. **Caching**: Cache expensive computations
3. **Database Indexing**: Index frequently queried fields
4. **Connection Pooling**: Reuse database connections
5. **Response Compression**: Enable gzip compression

## Monitoring and Observability

### Future Additions

```python
# Logging
import logging
logger = logging.getLogger(__name__)

# Metrics
from prometheus_client import Counter
request_counter = Counter('requests_total', 'Total requests')

# Tracing
from opentelemetry import trace
tracer = trace.get_tracer(__name__)
```

## Extension Points

The architecture is designed to grow:

1. **Add Middleware**: CORS, authentication, logging
2. **Add Database**: SQLAlchemy, async databases
3. **Add Caching**: Redis, in-memory cache
4. **Add Background Tasks**: Celery, FastAPI BackgroundTasks
5. **Add WebSockets**: Real-time features
6. **Add GraphQL**: Alternative API layer

## Technology Stack

### Current Stack

- **Framework**: FastAPI 0.119+
- **Server**: Uvicorn
- **Testing**: pytest
- **Linting**: Ruff

### Future Additions

- **Database**: PostgreSQL, SQLAlchemy
- **Cache**: Redis
- **Task Queue**: Celery
- **Monitoring**: Prometheus, Grafana
- **Logging**: Structlog

## Deployment Architecture

### Development

```
Developer → Local Server (Uvicorn) → Application
```

### Production

```
Internet → Load Balancer → Application Instances → Database
                          ↓
                      Cache (Redis)
                          ↓
                      Task Queue
```

## See Also

- [Design Decisions](design-decisions.md)
- [Development Workflow](workflow.md)
- [Project Structure](../reference/project-structure.md)
- [Configuration Reference](../reference/configuration.md)
