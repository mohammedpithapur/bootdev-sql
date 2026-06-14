-- We need to see how many young adults are using CashPal!

-- Query our users table to return the name and age fields of all users BETWEEN the ages of 18 and 30.

SELECT name, age FROM users
WHERE age BETWEEN 18 AND 30;