SELECT data ->> 'first_name' AS first_name,
       data ->> 'last_name' AS last_name,
       CAST (EXTRACT(YEAR FROM AGE(TO_DATE(data ->> 'date_of_birth', 'YYYY/MM/DD'))) AS INTEGER) AS age,
       CASE WHEN data ->> 'private' = 'true' THEN 'Hidden' 
            WHEN data #>> '{email_addresses,0}' IS NULL THEN 'None' 
            ELSE data #>> '{email_addresses,0}' END AS email_address
FROM users
ORDER BY 1, 2;