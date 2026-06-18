\set ON_ERROR_STOP on

CREATE ROLE toolshare_notification_service
WITH LOGIN PASSWORD 'toolshare-notification-local';

CREATE DATABASE toolshare_notification_db
OWNER toolshare_notification_service;

REVOKE CONNECT ON DATABASE toolshare_notification_db FROM PUBLIC;
