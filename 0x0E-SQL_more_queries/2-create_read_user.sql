-- This script create a database and a user with only select(read) permission if they didn't exists
-- Create a database if not exists then the user, then the select access is granted to the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
