SELECT prod.name,
  COUNT (CASE WHEN det.detail = 'good' THEN 1 END) good,
  COUNT (CASE WHEN det.detail = 'ok' THEN 1 END) ok,
  COUNT (CASE WHEN det.detail = 'bad' THEN 1 END) bad
  FROM products AS prod
    JOIN details AS det ON prod.id = det.product_id
GROUP BY 1
ORDER BY 1