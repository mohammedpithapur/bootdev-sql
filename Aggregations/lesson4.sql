-- Use a MIN aggregation to find only the age of our youngest CashPal user in the United States in the users table. The country_code of the United States is US.
-- Alias the returned column so that it's just named age.

SELECT MIN(age) AS age from users
where country_code = 'US';