from unittest.mock import Mock, patch

from app.config import Settings
from app.search.client import create_opensearch_client, get_cluster_health


def make_settings() -> Settings:
    return Settings(
        SERVICE_NAME="search-service",
        ENVIRONMENT="test",
        PORT=8000,
        LOG_LEVEL="INFO",
        OPENSEARCH_URL="https://localhost:9200",
        OPENSEARCH_USERNAME="admin",
        OPENSEARCH_PASSWORD="ToolshareLocal123!",
        OPENSEARCH_INDEX_EQUIPMENT_LISTINGS="equipment-listings",
        OPENSEARCH_VERIFY_CERTS=False,
    )


def test_create_opensearch_client_uses_settings():
    settings = make_settings()

    with patch("app.search.client.OpenSearch") as opensearch:
        create_opensearch_client(settings)

    opensearch.assert_called_once_with(
        hosts=[{"host": "localhost", "port": 9200}],
        http_auth=("admin", "ToolshareLocal123!"),
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )


def test_get_cluster_health_returns_opensearch_response():
    settings = make_settings()
    expected_health = {
        "cluster_name": "toolshare-local",
        "status": "green",
    }

    cluster = Mock()
    cluster.health.return_value = expected_health

    client = Mock()
    client.cluster = cluster

    with patch("app.search.client.create_opensearch_client", return_value=client):
        result = get_cluster_health(settings)

    assert result == expected_health
    cluster.health.assert_called_once_with()
