-- This script display score and name in descending order
-- Select score and name from the second_table table then sort it by descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
