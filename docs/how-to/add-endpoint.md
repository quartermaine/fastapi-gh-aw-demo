# How to Add a New Endpoint

This guide shows you how to add a new API endpoint to the FastAPI application.

## Quick Steps

1. Define the route in `app/api/routes.py`
2. Write tests in `tests/test_routes.py`
3. Run tests and linting
4. Update API documentation if needed

## Detailed Guide

### Step 1: Define Your Endpoint

Open `app/api/routes.py` and add your new endpoint:

```python
@router.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Retrieve a user by ID.
    
    Args:
        user_id: The unique identifier for the user
        
    Returns:
        User information
    """
    return {
        "user_id": user_id,
        "username": f"user_{user_id}",
        "active": True
    }
```

### Step 2: Add Request/Response Models (Optional)

For better type safety and documentation, use Pydantic models:

```python
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    active: bool = True

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    """Retrieve a user by ID."""
    return User(
        user_id=user_id,
        username=f"user_{user_id}"
    )
```

### Step 3: Write Tests

Add tests in `tests/test_routes.py`:

```python
def test_get_user():
    response = client.get("/api/users/123")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 123
    assert data["username"] == "user_123"
    assert data["active"] is True
```

### Step 4: Run Tests

```bash
make test
```

### Step 5: Verify in Interactive Docs

1. Start the server: `make run`
2. Visit http://localhost:8000/docs
3. Find your new endpoint
4. Test it using the "Try it out" button

## Different HTTP Methods

### POST Endpoint

```python
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    email: str

@router.post("/users")
def create_user(user: CreateUserRequest):
    """Create a new user."""
    return {
        "user_id": 1,
        "username": user.username,
        "email": user.email
    }
```

### PUT Endpoint

```python
@router.put("/users/{user_id}")
def update_user(user_id: int, user: CreateUserRequest):
    """Update an existing user."""
    return {
        "user_id": user_id,
        "username": user.username,
        "email": user.email,
        "updated": True
    }
```

### DELETE Endpoint

```python
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete a user."""
    return {"deleted": True, "user_id": user_id}
```

## Adding Query Parameters

```python
from typing import Optional

@router.get("/users")
def list_users(
    skip: int = 0,
    limit: int = 10,
    active: Optional[bool] = None
):
    """
    List users with pagination and filtering.
    
    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        active: Filter by active status (optional)
    """
    return {
        "skip": skip,
        "limit": limit,
        "active": active,
        "users": []
    }
```

## Adding Headers

```python
from fastapi import Header

@router.get("/secure-data")
def get_secure_data(authorization: str = Header(...)):
    """Endpoint that requires authorization header."""
    return {
        "data": "sensitive information",
        "auth": authorization
    }
```

## Best Practices

1. **Use Pydantic models** for request and response validation
2. **Add docstrings** to describe endpoint behavior
3. **Write tests** for each endpoint
4. **Use appropriate HTTP status codes** (200, 201, 404, etc.)
5. **Add type hints** to all parameters
6. **Keep routes organized** - group related endpoints together
7. **Use descriptive names** for functions and parameters

## Example: Complete CRUD Endpoint

```python
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException, status

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

# In-memory storage (use a database in production)
items_db = {}

@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """Create a new item."""
    if item.id in items_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item already exists"
        )
    items_db[item.id] = item
    return item

@router.get("/items", response_model=List[Item])
def list_items():
    """List all items."""
    return list(items_db.values())

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Get a specific item."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return items_db[item_id]

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    items_db[item_id] = item
    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    del items_db[item_id]
    return {"deleted": True}
```

## See Also

- [API Reference - Endpoints](../reference/endpoints.md)
- [Testing Guide](run-tests.md)
- [Architecture Explanation](../explanation/architecture.md)
