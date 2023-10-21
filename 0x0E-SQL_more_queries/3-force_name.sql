--  script that creates the table force_name on your MySQL server.

CREATE TABLE IF NOT EXISTS force_name (
	-- define each column content
	id INT,
	name VARCHAR(256) NOT NULL
	);
