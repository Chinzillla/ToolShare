import pytest

from app.config import load_settings


def test_default_config_loads(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "development")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    settings = load_settings()

    assert settings.service_name == "media-service"
    assert settings.environment == "development"
    assert settings.port == 8000
    assert settings.log_level == "INFO"


def test_invalid_port_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "development")
    monkeypatch.setenv("PORT", "not-a-number")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()


def test_invalid_environment_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "staging")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()


def test_missing_config_fails(monkeypatch):
    monkeypatch.delenv("SERVICE_NAME", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("PORT", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()
