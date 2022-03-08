-- This script create an average of temperature from temperatures.sql
-- Create an average of temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
