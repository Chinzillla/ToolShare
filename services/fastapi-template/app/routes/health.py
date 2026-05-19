import time
from datetime import datetime, timezone

from fastapi import APIRouter

from app.config import settings

router = APIRouter()

_started_at = time.monotonic()

@router.get("/health")
def get_health() -> dict[str, object]:
    return {
        "status": "ok",
        "service": settings.service_name,
        "uptime": time.monotonic() - _started_at,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }