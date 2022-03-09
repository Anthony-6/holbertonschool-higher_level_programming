-- This script select the id and the name from the city table
-- Select the id and the name from city, then order it by ID
SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY id;