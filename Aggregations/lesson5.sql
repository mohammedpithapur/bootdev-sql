-- Let's get the balance of each user with successful transactions, all in a single query!

-- Use the SUM aggregation with the GROUP BY clause.
-- The row for each user should contain the user_id and their balance – a sum of the amounts of their successful transactions.

SELECT user_id, SUM(amount) AS balance FROM transactions
where was_successful = TRUE
GROUP BY user_id;