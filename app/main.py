# app/main.py
from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="FastAPI GH-AW Demo", version="0.1.0")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI GH AW Demo!"}
