-- This script display the max temparature from every state
-- get the max value from state then goup it and order it
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
