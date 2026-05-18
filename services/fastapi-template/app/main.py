from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="FastAPI Service Template",
    version="0.0.1",
)