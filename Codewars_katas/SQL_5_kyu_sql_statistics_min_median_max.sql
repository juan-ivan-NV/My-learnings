SELECT MIN(score) AS min,
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY score):: float AS median,
MAX(score) AS max
FROM result;