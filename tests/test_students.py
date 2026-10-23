from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students/",
        json={
            "name": "Test Student",
            "date_of_birth": "2005-01-01",
            "email": "test_student_unique@example.com",
            "phone": "9000000000",
            "course": "B.Tech CSE",
            "address": "Bangalore",
            "enrollment_date": "2026-07-01",
        },
    )
    assert response.status_code in (201, 409)


def test_list_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
