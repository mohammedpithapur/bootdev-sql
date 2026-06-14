-- Write a query that returns every user from the users table, including all columns, plus an additional column named discount_percent.

-- The discount_percent column should have an integer value of 10 or 0, depending on whether the user matches any discount condition listed above.

SELECT *, IIF(country_code = 'CA' OR age>55, 10, 0) AS discount_percent
FROM users