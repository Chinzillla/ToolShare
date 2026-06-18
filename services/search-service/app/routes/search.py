from fastapi import APIRouter

from app.config import settings
from app.search.client import get_cluster_health

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/health")
def get_search_health():
    return get_cluster_health(settings)
