import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, CI/CD + Docker!"


def test_index_content_type(client):
    response = client.get("/")
    assert response.content_type == "application/json"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_not_found_route(client):
    response = client.get("/rota-que-nao-existe")
    assert response.status_code == 404


def test_method_not_allowed(client):
    response = client.post("/")
    assert response.status_code == 405
