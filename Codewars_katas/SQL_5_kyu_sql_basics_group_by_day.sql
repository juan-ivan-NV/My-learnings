-- Replace with your SQL Query
select DATE(created_at) as day, description, 

count (id) from events 

where name in ('trained') 
  
group by day, description;