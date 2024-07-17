# Write your MySQL query statement below
select 
round(
    count(distinct firstlogins.player_id) / (select count(distinct player_id) from Activity),
    2
) as fraction
from
(
    select player_id, min(event_date) as firstlogin
    from Activity
    group by player_id
) as firstlogins
join
Activity a on firstlogins.player_id = a.player_id
and datediff(a.event_date, firstlogins.firstlogin) = 1
