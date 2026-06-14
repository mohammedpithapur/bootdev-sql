-- We want to know which of our users are from the United States, Canada, or Mexico.

-- Write a SELECT statement that returns the name, age, and country_code fields for every user within the US, CA, or MX.

SELECT name, age, country_code FROM users
WHERE country_code IN ('US', 'CA', 'MX');