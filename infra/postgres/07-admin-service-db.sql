\set ON_ERROR_STOP on

CREATE ROLE toolshare_admin_service
WITH LOGIN PASSWORD 'toolshare-admin-local';

CREATE DATABASE toolshare_admin_db
OWNER toolshare_admin_service;

REVOKE CONNECT ON DATABASE toolshare_admin_db FROM PUBLIC;
