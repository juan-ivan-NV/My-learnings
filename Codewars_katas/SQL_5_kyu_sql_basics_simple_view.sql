--CREATE VIEW members_approved_for_voucher AS
WITH t1 AS (SELECT d.id, d.name, SUM(p.price) dpt_total
    FROM sales s JOIN departments d 
    ON s.department_id = d.id
    JOIN products p ON s.product_id = p.id
GROUP BY 1
    HAVING SUM(p.price) > 10000)

SELECT m.id as id, m.name as name, m.email as email , SUM(p.price) total_spending
FROM sales s
    JOIN departments d ON s.department_id = d.id
    JOIN products p ON s.product_id = p.id
    JOIN members  m ON s.member_id = m.id
    JOIN t1 ON t1.id = s.department_id
GROUP BY 1
    HAVING SUM(p.price) > 1000 
ORDER BY 1 