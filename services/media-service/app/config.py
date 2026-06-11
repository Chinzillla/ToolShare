from typing import Literal

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = Field(alias="SERVICE_NAME")
    environment: Literal["development", "test", "production"] = Field(alias="ENVIRONMENT")
    port: int = Field(alias="PORT", ge=1, le=65535)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(alias="LOG_LEVEL")

    minio_endpoint: str = Field(alias="MINIO_ENDPOINT")
    minio_access_key: str = Field(alias="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(alias="MINIO_SECRET_KEY")
    minio_use_ssl: bool = Field(alias="MINIO_USE_SSL")

    minio_equipment_photos_bucket: str = Field(alias="MINIO_EQUIPMENT_PHOTOS_BUCKET")
    minio_pickup_photos_bucket: str = Field(alias="MINIO_PICKUP_PHOTOS_BUCKET")
    minio_return_photos_bucket: str = Field(alias="MINIO_RETURN_PHOTOS_BUCKET")
    minio_dispute_evidence_bucket: str = Field(alias="MINIO_DISPUTE_EVIDENCE_BUCKET")

    # Signed url expiry 1 to 60 minutes
    minio_signed_url_expiry_seconds: int = Field(
        alias="MINIO_SIGNED_URL_EXPIRY_SECONDS",
        ge=60,
        le=3600,
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


def load_settings(*, env_file: str | None = ".env") -> Settings:
    try:
        return Settings(_env_file=env_file)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid service configuration: {exc}") from exc


settings = load_settings()
