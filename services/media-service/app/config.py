from typing import Literal

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = Field(alias="SERVICE_NAME")
    environment: Literal["development", "test", "production"] = Field(alias="ENVIRONMENT")
    port: int = Field(alias="PORT", ge=1, le=65535)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


def load_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as exc:
        raise RuntimeError(f"Invalid service configuration: {exc}") from exc


settings = load_settings()
