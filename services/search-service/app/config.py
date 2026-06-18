from typing import Literal

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = Field(alias="SERVICE_NAME")
    environment: Literal["development", "test", "production"] = Field(alias="ENVIRONMENT")
    port: int = Field(alias="PORT", ge=1, le=65535)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(alias="LOG_LEVEL")
    opensearch_url: str = Field(alias="OPENSEARCH_URL")
    opensearch_username: str = Field(alias="OPENSEARCH_USERNAME")
    opensearch_password: str = Field(alias="OPENSEARCH_PASSWORD")
    opensearch_index_equipment_listings: str = Field(alias="OPENSEARCH_INDEX_EQUIPMENT_LISTINGS")
    opensearch_verify_certs: bool = Field(alias="OPENSEARCH_VERIFY_CERTS")

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
