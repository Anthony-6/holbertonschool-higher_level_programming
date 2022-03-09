-- This script create a database hbtn_0d_usa it it not exists
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- This script create a new table based on the hbtn_0d_usa database if it didn't already exists
-- Create the table state and set the default id to 1
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id)
);
