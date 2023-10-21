--  script that creates the table id_not_null on your MySQL server.

CREATE TABLE IF NOT EXISTS id_not_null (
	-- define the colunms of the table
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
