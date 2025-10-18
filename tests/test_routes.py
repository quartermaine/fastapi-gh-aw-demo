from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_hello():
    response = client.get("/api/hello?name=Agent")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Agent!"}
