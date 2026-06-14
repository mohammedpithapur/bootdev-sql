-- We need to be able to calculate the current balance for a given user because we don't (yet) store the running balance on each individual transaction record.

-- Write a query that returns the SUM aggregation of the amounts for all of Bob's successful transactions (user_id is 9). Check the file 001_up.sql for more details about the table.

SELECT SUM(amount) FROM transactions
WHERE user_id=9 AND was_successful=TRUE;