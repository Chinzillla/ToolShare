import pytest

from app.config import load_settings


def test_default_config_loads(monkeypatch):
    monkeypatch.delenv("SERVICE_NAME", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("PORT", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    settings = load_settings()

    assert settings.service_name == "fastapi-template"
    assert settings.environment == "development"
    assert settings.port == 8000
    assert settings.log_level == "INFO"


def test_invalid_port_fails(monkeypatch):
    monkeypatch.setenv("PORT", "not-a-number")

    with pytest.raises(RuntimeError, match="Invalid numeric environment variable"):
        load_settings()


def test_invalid_environment_fails(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "staging")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings()