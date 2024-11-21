from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_profile():
    response = client.post("/create-profile", json={
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "password": "Password@123"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_create_profile_password_validation():
    response = client.post("/create-profile", json={
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "phone": "1234567890",
        "password": "password"
    })
    assert response.status_code == 400
    assert "Password must be at least 8 characters long" in response.json()["detail"]