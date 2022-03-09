-- This script create a new table if it didn't already exists
-- Create the table unique_id and set the default id to 1
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
