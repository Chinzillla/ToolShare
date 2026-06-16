import os

os.environ.setdefault("SERVICE_NAME", "search-service")
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("PORT", "8000")
os.environ.setdefault("LOG_LEVEL", "INFO")
os.environ.setdefault("OPENSEARCH_URL", "https://localhost:9200")
os.environ.setdefault("OPENSEARCH_USERNAME", "admin")
os.environ.setdefault("OPENSEARCH_PASSWORD", "ToolshareLocal123!")
os.environ.setdefault("OPENSEARCH_INDEX_EQUIPMENT_LISTINGS", "equipment-listings")
os.environ.setdefault("OPENSEARCH_VERIFY_CERTS", "false")