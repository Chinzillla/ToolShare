from datetime import timedelta

from minio import Minio

from app.config import Settings


class StorageClient:
    def __init__(self, settings: Settings) -> None:
        self._client = Minio(
            endpoint=settings.minio_endpoint,
            access_key=settings.minio_access_key,
            secret_key=settings.minio_secret_key,
            secure=settings.minio_use_ssl,
        )
        self._expiry = timedelta(seconds=settings.minio_signed_url_expiry_seconds)

    def create_upload_url(
        self,
        bucket_name: str,
        object_name: str,
    ) -> str:
        return self._client.presigned_put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            expires=self._expiry,
        )

    def create_download_url(
        self,
        bucket_name: str,
        object_name: str,
    ) -> str:
        return self._client.presigned_get_object(
            bucket_name=bucket_name,
            object_name=object_name,
            expires=self._expiry,
        )
