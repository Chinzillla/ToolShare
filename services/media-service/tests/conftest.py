import os

os.environ.setdefault("MINIO_ENDPOINT", "http://localhost:9000")
os.environ.setdefault("MINIO_ACCESS_KEY", "test-access-key")
os.environ.setdefault("MINIO_SECRET_KEY", "test-secret-key")
os.environ.setdefault("MINIO_USE_SSL", "false")

os.environ.setdefault(
    "MINIO_EQUIPMENT_PHOTOS_BUCKET",
    "equipment-photos",
)
os.environ.setdefault(
    "MINIO_PICKUP_PHOTOS_BUCKET",
    "pickup-photos",
)
os.environ.setdefault(
    "MINIO_RETURN_PHOTOS_BUCKET",
    "return-photos",
)
os.environ.setdefault(
    "MINIO_DISPUTE_EVIDENCE_BUCKET",
    "dispute-evidence",
)

os.environ.setdefault("MINIO_SIGNED_URL_EXPIRY_SECONDS", "900")