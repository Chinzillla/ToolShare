\set ON_ERROR_STOP on

CREATE ROLE toolshare_user_service
WITH LOGIN PASSWORD 'toolshare-user-local';

CREATE DATABASE toolshare_user_db
OWNER toolshare_user_service;

REVOKE CONNECT ON DATABASE toolshare_user_db FROM PUBLIC;