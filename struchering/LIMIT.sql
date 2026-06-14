-- A lot of our users have been using CashPal to pay other users for lunch. Let's take a look at a sample of that data.

-- Write a query that returns all rows and fields from the transactions table, with the following conditions:

-- Any record where the note field has the word lunch in it.
-- The query should return at most 5 records.

SELECT * FROM transactions
where note LIKE '%lunch%'
LIMIT 5;