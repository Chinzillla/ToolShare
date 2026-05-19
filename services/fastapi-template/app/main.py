from fastapi import FastAPI
from app.config import settings
from app.routes.health import router as health_router

app = FastAPI(
    title=settings.service_name,
    version="0.0.1",
)

app.include_router(health_router)