# Write your MySQL query statement below
select Employee.name, Bonus.bonus 
from Employee LEFT JOIN Bonus
on Employee.empId = Bonus.empId 
where Bonus.bonus<1000 or Bonus.bonus IS NULL

# select Employee.name, COALESCE(Bonus.bonus, 0) as bonus
#from Employee LEFT JOIN Bonus
#on Employee.empId = Bonus.empId
#where coalesce(Bonus.bonus,0)<1000