-- Create your SELECT statement here
select people.id, people.name, count(sales.sale) as sale_count,
rank() over(order by count(sales.sale) desc) sale_rank
from people
join sales on people.id = sales.people_id
group by people.id