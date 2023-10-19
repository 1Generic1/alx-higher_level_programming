-- List records with a score >= 10 from second_table, ordering by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
