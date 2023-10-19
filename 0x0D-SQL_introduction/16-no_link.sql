-- script to list all records in the second_table of the hbtn_0c_0 database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
