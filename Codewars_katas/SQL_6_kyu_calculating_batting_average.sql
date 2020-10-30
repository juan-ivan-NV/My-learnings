select player_name,
games,
cast(round(yankees.hits*1.00/yankees.at_bats,3) as varchar(100) ) as batting_average
from yankees
where yankees.at_bats > 100
order by batting_average desc;