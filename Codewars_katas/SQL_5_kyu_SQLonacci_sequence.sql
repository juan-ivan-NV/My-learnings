-- sql goes here :)
WITH RECURSIVE r(number, b) AS (
  SELECT 0::bigint, 1::bigint
  UNION ALL
  SELECT b, number + b FROM r WHERE b <= 1779979416004714189
)                                  
SELECT number FROM r;