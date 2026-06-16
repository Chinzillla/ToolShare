import pytest

from app.config import load_settings

def set_required_config(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "search-service")
    monkeypatch.setenv("ENVIRONMENT", "development")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    monkeypatch.setenv("OPENSEARCH_URL", "https://localhost:9200")
    monkeypatch.setenv("OPENSEARCH_USERNAME", "admin")
    monkeypatch.setenv("OPENSEARCH_PASSWORD", "ToolshareLocal123!")
    monkeypatch.setenv("OPENSEARCH_INDEX_EQUIPMENT_LISTINGS", "equipment-listings")
    monkeypatch.setenv("OPENSEARCH_VERIFY_CERTS", "false")

def test_default_config_loads(monkeypatch):
    set_required_config(monkeypatch)

    settings = load_settings(env_file=None)

    assert settings.service_name == "search-service"
    assert settings.environment == "development"
    assert settings.port == 8000
    assert settings.log_level == "INFO"
    assert settings.opensearch_url == "https://localhost:9200"
    assert settings.opensearch_username == "admin"
    assert settings.opensearch_password == "ToolshareLocal123!"
    assert settings.opensearch_index_equipment_listings == "equipment-listings"
    assert settings.opensearch_verify_certs is False


def test_invalid_port_fails(monkeypatch):
    set_required_config(monkeypatch)
    monkeypatch.setenv("PORT", "not-a-number")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()


def test_invalid_environment_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "search-service")
    monkeypatch.setenv("ENVIRONMENT", "staging")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    monkeypatch.delenv("OPENSEARCH_URL", raising=False)
    monkeypatch.delenv("OPENSEARCH_USERNAME", raising=False)
    monkeypatch.delenv("OPENSEARCH_PASSWORD", raising=False)
    monkeypatch.delenv("OPENSEARCH_INDEX_EQUIPMENT_LISTINGS", raising=False)
    monkeypatch.delenv("OPENSEARCH_VERIFY_CERTS", raising=False)

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()


def test_missing_config_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "search-service")
    monkeypatch.setenv("ENVIRONMENT", "staging")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    monkeypatch.delenv("OPENSEARCH_URL", raising=False)
    monkeypatch.delenv("OPENSEARCH_USERNAME", raising=False)
    monkeypatch.delenv("OPENSEARCH_PASSWORD", raising=False)
    monkeypatch.delenv("OPENSEARCH_INDEX_EQUIPMENT_LISTINGS", raising=False)
    monkeypatch.delenv("OPENSEARCH_VERIFY_CERTS", raising=False)

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()
