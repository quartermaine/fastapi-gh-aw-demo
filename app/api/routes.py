# app/api/routes.py
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["demo"])


@router.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
