# Write your MySQL query statement below


select s.name 
from salesperson s
where s.sales_id not in (select o.sales_id 
from orders o 
where com_id = (select c.com_id 
from company c 
where c.name = 'RED'))

