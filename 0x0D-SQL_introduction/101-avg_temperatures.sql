-- This script create an average of temperature from temperatures.sql
-- Create an average of temperature
SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
