-- This script count the number of time when a score is the same
-- Create a column numer for the result of score
SELECT score, COUNT(score) AS 'number'
FROM second_table GROUP BY score
ORDER BY score DESC;
