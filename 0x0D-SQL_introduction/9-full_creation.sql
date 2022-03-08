-- This script create a table
-- This script create a table with id, name and score
CREATE TABLE IF NOT EXISTS second_table (
    id INT DEFAULT NULL,

    name VARCHAR(256),

    score INT DEFAULT NULL
);
-- choose the table and the value to insert
INSERT INTO second_table(id, name, score)
-- Insert value
VALUES (1, 'John', 10);
INSERT INTO second_table(id, name, score)
VALUES (2, 'Alex', 3);
INSERT INTO second_table(id, name, score)
VALUES (3, 'Bob', 14);
INSERT INTO second_table(id, name, score)
VALUES (4, 'George', 8);
