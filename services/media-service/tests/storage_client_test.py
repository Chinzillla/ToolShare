from datetime import timedelta
from unittest.mock import Mock

import pytest

from app.config import load_settings
from app.storage.client import StorageClient


@pytest.fixture
def storage_client(monkeypatch):
    settings = load_settings(env_file=None)
    minio_sdk = Mock()
    minio_factory = Mock(return_value=minio_sdk)

    monkeypatch.setattr("app.storage.client.Minio", minio_factory)

    client = StorageClient(settings)

    return client, minio_sdk, minio_factory, settings


def test_storage_client_uses_configured_connection(storage_client):
    _, _, minio_factory, settings = storage_client

    minio_factory.assert_called_once_with(
        endpoint=settings.minio_endpoint,
        access_key=settings.minio_access_key,
        secret_key=settings.minio_secret_key,
        secure=settings.minio_use_ssl,
    )


def test_create_upload_url(storage_client):
    client, minio_sdk, _, _ = storage_client
    minio_sdk.presigned_put_object.return_value = "https://signed-upload-url"

    result = client.create_upload_url(
        bucket_name="equipment-photos",
        object_name="equipment/123/photo.jpg",
    )

    assert result == "https://signed-upload-url"
    minio_sdk.presigned_put_object.assert_called_once_with(
        bucket_name="equipment-photos",
        object_name="equipment/123/photo.jpg",
        expires=timedelta(seconds=900),
    )


def test_create_download_url(storage_client):
    client, minio_sdk, _, _ = storage_client
    minio_sdk.presigned_get_object.return_value = "https://signed-download-url"

    result = client.create_download_url(
        bucket_name="dispute-evidence",
        object_name="disputes/456/evidence.jpg",
    )

    assert result == "https://signed-download-url"
    minio_sdk.presigned_get_object.assert_called_once_with(
        bucket_name="dispute-evidence",
        object_name="disputes/456/evidence.jpg",
        expires=timedelta(seconds=900),
    )
