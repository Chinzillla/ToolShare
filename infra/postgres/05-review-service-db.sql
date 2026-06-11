\set ON_ERROR_STOP on

CREATE ROLE toolshare_review_service
WITH LOGIN PASSWORD 'toolshare-review-local';

CREATE DATABASE toolshare_review_db
OWNER toolshare_review_service;

REVOKE CONNECT ON DATABASE toolshare_review_db FROM PUBLIC;
