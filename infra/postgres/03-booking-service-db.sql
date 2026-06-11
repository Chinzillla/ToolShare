\set ON_ERROR_STOP on

CREATE ROLE toolshare_booking_service
WITH LOGIN PASSWORD 'toolshare-booking-local';

CREATE DATABASE toolshare_booking_db
OWNER toolshare_booking_service;

REVOKE CONNECT ON DATABASE toolshare_booking_db FROM PUBLIC;
