import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.integration
def test_search_health_route_returns_cluster_health():
    response = client.get("/search/health")
    data = response.json()

    assert response.status_code == 200
    assert "cluster_name" in data
    assert data["status"] in ["green", "yellow", "red"]
    assert isinstance(data["number_of_nodes"], int)


@pytest.mark.integration
def test_search_post_returns_method_not_allowed():
    response = client.post("/search/health")

    assert response.status_code == 405
