SELECT COALESCE(po.category_id,ca.id ) as category_id, ca.category, po.title, po.views, po.id as post_id
FROM categories ca LEFT JOIN LATERAL  (
SELECT * FROM posts as po 
WHERE po.category_id = ca.id  
ORDER BY ca.category, po.views desc limit 2 ) po on TRUE
ORDER BY category, views desc, post_id;