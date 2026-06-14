-- The legal restrictions in Canada have changed! The way we have to handle Canadian minors' CashPal transactions is more tightly regulated. We need to find all of those users, so we can see how many this change affects!

-- Write a query that retrieves all columns for users in the users table who are from Canada (CA) and under the age of 18.

SELECT * FROM users
WHERE country_code = 'CA' AND
age < 18;