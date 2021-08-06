WITH t1 AS (SELECT created_at::date AS date FROM posts)
SELECT date, count(date), 
SUM(count(date)) OVER (ORDER BY date)::int AS total
FROM t1
GROUP BY 1;