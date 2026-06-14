select DISTINCT users.id,users.name,users.age,users.username,countries.name as country_name, sum(transactions.amount) as balance
from users
LEFT JOIN transactions
on transactions.user_id = users.id
LEFT JOIN countries
on counteries.country_code = users.country_code
where users.id = 6
GROUP BY users.id;