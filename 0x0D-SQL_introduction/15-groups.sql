-- Select the 'score' column and count the number of records for each score
-- while giving the count an alias 'number'.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
