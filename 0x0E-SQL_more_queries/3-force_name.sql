-- This script create a new tabe called force_name
-- Create the table if it didn't already exist with id and name attributs inside
CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) DEFAULT 1
);
