-- This script create a new table if it didn't already exists
-- Create the table id_not_null and set the default value of the id to 1
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
