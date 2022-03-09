-- This script a list of all city that are in the database
-- Select id, name and states names from the cities table and join it
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id;
