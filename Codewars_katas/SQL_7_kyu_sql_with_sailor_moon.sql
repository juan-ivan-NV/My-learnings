--your code here--
SELECT s.senshi_name sailor_senshi, 
       s.real_name_jpn real_name,  
       c.name cat,
       sc.school school
FROM sailorsenshi s
LEFT JOIN cats c ON c.id = s.cat_id
LEFT JOIN schools sc ON sc.id = s.school_id