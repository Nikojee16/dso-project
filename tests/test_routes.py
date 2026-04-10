import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_greet(client):
    response = client.get("/greet/Nikojee16")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Nikojee16!"}

def test_greet_missing_name(client):
    response = client.get("/greet/")
    assert response.status_code == 404