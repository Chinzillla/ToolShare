import pytest
from textwrap import dedent

from app.config import load_settings

CONFIG_ENV_KEYS = (
    "SERVICE_NAME",
    "ENVIRONMENT",
    "PORT",
    "LOG_LEVEL",
    "MINIO_ENDPOINT",
    "MINIO_ACCESS_KEY",
    "MINIO_SECRET_KEY",
    "MINIO_USE_SSL",
    "MINIO_EQUIPMENT_PHOTOS_BUCKET",
    "MINIO_PICKUP_PHOTOS_BUCKET",
    "MINIO_RETURN_PHOTOS_BUCKET",
    "MINIO_DISPUTE_EVIDENCE_BUCKET",
    "MINIO_SIGNED_URL_EXPIRY_SECONDS",
)


def test_default_config_loads(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "development")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    settings = load_settings(env_file=None)

    assert settings.service_name == "media-service"
    assert settings.environment == "development"
    assert settings.port == 8000
    assert settings.log_level == "INFO"


def test_config_loads_from_env_file(monkeypatch, tmp_path):
    for key in CONFIG_ENV_KEYS:
        monkeypatch.delenv(key, raising=False)

    env_file = tmp_path / ".env"
    env_file.write_text(
        dedent(
            """\
            SERVICE_NAME=media-service
            ENVIRONMENT=development
            PORT=8000
            LOG_LEVEL=INFO
            MINIO_ENDPOINT=localhost:9000
            MINIO_ACCESS_KEY=toolshare
            MINIO_SECRET_KEY=toolshare-local-minio
            MINIO_USE_SSL=false
            MINIO_EQUIPMENT_PHOTOS_BUCKET=equipment-photos
            MINIO_PICKUP_PHOTOS_BUCKET=pickup-photos
            MINIO_RETURN_PHOTOS_BUCKET=return-photos
            MINIO_DISPUTE_EVIDENCE_BUCKET=dispute-evidence
            MINIO_SIGNED_URL_EXPIRY_SECONDS=900
            """
        ),
        encoding="utf-8",
    )

    settings = load_settings(env_file=str(env_file))

    assert settings.service_name == "media-service"
    assert settings.minio_endpoint == "localhost:9000"
    assert settings.minio_use_ssl is False
    assert settings.minio_equipment_photos_bucket == "equipment-photos"


def test_invalid_port_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "development")
    monkeypatch.setenv("PORT", "not-a-number")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings(env_file=None)


def test_invalid_environment_fails(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "media-service")
    monkeypatch.setenv("ENVIRONMENT", "staging")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings(env_file=None)


def test_missing_config_fails(monkeypatch):
    monkeypatch.delenv("SERVICE_NAME", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("PORT", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings(env_file=None)


def test_minio_config_loads():
    settings = load_settings(env_file=None)

    assert settings.minio_endpoint == "localhost:9000"
    assert settings.minio_use_ssl is False
    assert settings.minio_equipment_photos_bucket == "equipment-photos"
    assert settings.minio_pickup_photos_bucket == "pickup-photos"
    assert settings.minio_return_photos_bucket == "return-photos"
    assert settings.minio_dispute_evidence_bucket == "dispute-evidence"
    assert settings.minio_signed_url_expiry_seconds == 900


def test_missing_bucket_config_fails(monkeypatch):
    monkeypatch.delenv("MINIO_EQUIPMENT_PHOTOS_BUCKET")

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings(env_file=None)


@pytest.mark.parametrize("expiry", ["59", "3601"])
def test_invalid_signed_url_expiry_fails(monkeypatch, expiry):
    monkeypatch.setenv("MINIO_SIGNED_URL_EXPIRY_SECONDS", expiry)

    with pytest.raises(RuntimeError, match="Invalid service configuration"):
        load_settings(env_file=None)
