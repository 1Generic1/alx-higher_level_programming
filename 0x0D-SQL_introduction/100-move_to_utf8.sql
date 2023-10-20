-- convert the hbtn_0c_0 database, the first_table table, and
-- the name field in the first_table to UTF-8
-- (utf8mb4 with collation utf8mb4_unicode_ci)
USE hbtn_0c_0;
-- Modify the table first_table to use the utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the name column in first_table to use the utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
