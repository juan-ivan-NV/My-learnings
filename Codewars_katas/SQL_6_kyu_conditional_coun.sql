WITH t1 AS (SELECT DATE_PART('month', payment_date) AS Month, 
              SUM(amount) mike_amount, 
              COUNT(*) as mike_count
           FROM payment 
           WHERE staff_id = 1
           GROUP BY Month),
     
     t2 AS (SELECT DATE_PART('month', payment_date) AS Month, 
              SUM(amount) jon_amount, 
              COUNT(*) as jon_count
           FROM payment 
           WHERE staff_id = 2
           GROUP BY Month)

SELECT t1.month, 
  (t1.mike_count + t2.jon_count) AS total_count,
  (t1.mike_amount + t2.jon_amount) AS total_amount,
  t1.mike_count, t1.mike_amount,
  t2.jon_count, t2.jon_amount
FROM t1 
JOIN t2 ON t1.month = t2.month
ORDER BY month 