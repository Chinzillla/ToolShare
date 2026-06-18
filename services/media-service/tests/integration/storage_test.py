from io import BytesIO
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen
from uuid import uuid4

import pytest
from minio import Minio

from app.config import load_settings
from app.storage.client import StorageClient


@pytest.mark.integration
def test_private_object_requires_signed_url():
    settings = load_settings(env_file=None)
    minio_client = Minio(
        endpoint=settings.minio_endpoint,
        access_key=settings.minio_access_key,
        secret_key=settings.minio_secret_key,
        secure=settings.minio_use_ssl,
    )
    storage_client = StorageClient(settings)

    bucket_name = settings.minio_equipment_photos_bucket
    object_name = f"integration/{uuid4()}.txt"
    content = b"private media test"

    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=BytesIO(content),
        length=len(content),
        content_type="text/plain",
    )

    try:
        scheme = "https" if settings.minio_use_ssl else "http"
        anonymous_url = (
            f"{scheme}://{settings.minio_endpoint}/{bucket_name}/{quote(object_name, safe='/')}"
        )

        with pytest.raises(HTTPError) as error:
            urlopen(anonymous_url, timeout=5)

        assert error.value.code == 403

        signed_url = storage_client.create_download_url(
            bucket_name,
            object_name,
        )

        with urlopen(signed_url, timeout=5) as signed_response:
            assert signed_response.status == 200
            assert signed_response.read() == content
    finally:
        minio_client.remove_object(
            bucket_name,
            object_name,
        )
