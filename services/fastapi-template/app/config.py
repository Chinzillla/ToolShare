import os
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

class Settings(BaseModel):
    service_name: str = Field(default="fastapi-template")
    environment: Literal["development", "test", "production"] = "development"
    port: int = Field(default=8000, ge=1, le=65535)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

def load_settings() -> Settings:
    try:
        return Settings(
            service_name=os.getenv("SERVICE_NAME", "fastapi-template"),
            environment=os.getenv("ENVIRONMENT", "development"),
            port=int(os.getenv("PORT", "8000")),
            log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        )

    except ValidationError as exc:
        raise RuntimeError(f"Invalid service configuration: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError("Invalid numeric environment variable") from exc

settings = load_settings()