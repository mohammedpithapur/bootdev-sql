-- Use a MAX aggregation to return the age of our oldest CashPal user who is also an admin.
-- Alias the returned column so that it's just named age.

SELECT MAX(age) AS age FROM users
where is_admin=TRUE;