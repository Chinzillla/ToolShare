\set ON_ERROR_STOP on

CREATE ROLE toolshare_payment_service
WITH LOGIN PASSWORD 'toolshare-payment-local';

CREATE DATABASE toolshare_payment_db
OWNER toolshare_payment_service;

REVOKE CONNECT ON DATABASE toolshare_payment_db FROM PUBLIC;
