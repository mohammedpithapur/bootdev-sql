-- The laws have changed again! Now we need to see how many affected users meet these criteria:

-- Users who are from the United States or Canada, and are under 18

-- Write a query that retrieves the count of all users (aliased to junior_count) who match the conditions above.

SELECT COUNT(id) FROM users
WHERE (country_code = 'US' OR country_code = 'CA') AND
age < 18;