-- script that creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
	-- define ther column contents
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
