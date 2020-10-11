/*  SQL  */
select 
t.id as id,
t.heads as heads,
t.arms as arms,
h.legs as legs,
h.tails as tails,
case
when t.heads > t.arms then 'BEAST'
when h.tails > h.legs then 'BEAST'
else 'WEIRDO'
end as species
from top_half as t
inner join bottom_half h on t.id = h.id
order by species;