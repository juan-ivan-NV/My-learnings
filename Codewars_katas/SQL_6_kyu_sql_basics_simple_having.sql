-- Create your SELECT statement here
SELECT p.age, count(age) AS total_people
FROM people AS p
GROUP BY (age)
HAVING count(age) >= 10;