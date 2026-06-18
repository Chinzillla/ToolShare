from typing import Any
from urllib.parse import urlparse

from opensearchpy import OpenSearch

from app.config import Settings


def create_opensearch_client(settings: Settings) -> OpenSearch:
    parsed_url = urlparse(settings.opensearch_url)

    return OpenSearch(
        hosts=[
            {
                "host": parsed_url.hostname,
                "port": parsed_url.port,
            }
        ],
        http_auth=(settings.opensearch_username, settings.opensearch_password),
        use_ssl=parsed_url.scheme == "https",
        verify_certs=settings.opensearch_verify_certs,
        ssl_assert_hostname=settings.opensearch_verify_certs,
        ssl_show_warn=settings.opensearch_verify_certs,
    )


def get_cluster_health(settings: Settings) -> dict[str, Any]:
    client = create_opensearch_client(settings)
    return client.cluster.health()
