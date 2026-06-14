select users.name as name, SUM(transactions.amount) as transaction_sum, COUNT(transactions.amount) as transactions_count
from users
LEFT JOIN transactions
on transactions.user_id = users.id
GROUP BY users.id
ORDER BY transaction_sum DESC;