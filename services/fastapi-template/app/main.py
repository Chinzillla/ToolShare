import logging
import time

from fastapi import FastAPI, Request

from app.config import settings
from app.logging import configure_logging
from app.routes.health import router as health_router

configure_logging()

app = FastAPI(
    title=settings.service_name,
    version="0.0.1",
)

app.include_router(health_router)

logger = logging.getLogger("app.request")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    started_at = time.perf_counter()
    response = await call_next(request)
    duration_ms = round((time.perf_counter() - started_at) * 1000, 2)

    logger.info(
        "request completed",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )
    return response
