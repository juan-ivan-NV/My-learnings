SELECT fi.name, sum(fi.won) won, sum(fi.lost) lost 
FROM fighters as fi
LEFT JOIN winning_moves wi
ON wi.id = fi.move_id
WHERE move not in ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY name
ORDER BY won desc
LIMIT 6;