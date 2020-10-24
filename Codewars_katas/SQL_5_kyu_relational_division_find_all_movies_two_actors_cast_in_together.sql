select a.title
from film a
join film_actor b on a.film_id = b.film_id
join film_actor b1 on a.film_id = b1.film_id 
where b.actor_id = 105 and b1.actor_id = 122
order by a.title;