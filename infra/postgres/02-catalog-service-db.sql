\set ON_ERROR_STOP on

CREATE ROLE toolshare_catalog_service
WITH LOGIN PASSWORD 'toolshare-catalog-local';

CREATE DATABASE toolshare_catalog_db
OWNER toolshare_catalog_service;

REVOKE CONNECT ON DATABASE toolshare_catalog_db FROM PUBLIC;