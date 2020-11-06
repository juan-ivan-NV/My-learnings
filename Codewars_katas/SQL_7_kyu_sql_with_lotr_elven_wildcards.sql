SELECT 
CONCAT ( 
CONCAT (UPPER (SUBSTRING (firstname, 1, 1 ) ), SUBSTRING (firstname, 2) ), ' ', 
CONCAT (UPPER (SUBSTRING (lastname, 1, 1) ), SUBSTRING (lastname, 2) ) )  shortlist
FROM Elves
WHERE firstname ~* 'tegil' or lastname ~* 'astar' 