from datetime import datetime
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings

client = TestClient(app)

def test_health_route_returns_ok_response():
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "ok"
    assert body["service"] == settings.service_name
    assert isinstance(body["uptime"], float)
    assert body["uptime"] >= 0

    datetime.fromisoformat(body["timestamp"])
    
def test_health_route_is_in_openapi_schema():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/health" in response.json()["paths"]