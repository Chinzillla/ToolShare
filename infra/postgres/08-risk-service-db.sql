\set ON_ERROR_STOP on

CREATE ROLE toolshare_risk_service
WITH LOGIN PASSWORD 'toolshare-risk-local';

CREATE DATABASE toolshare_risk_db
OWNER toolshare_risk_service;

REVOKE CONNECT ON DATABASE toolshare_risk_db FROM PUBLIC;
