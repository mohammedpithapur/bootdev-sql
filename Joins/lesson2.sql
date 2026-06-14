SELECT users.name, users.age, countries.name as country_name
FROM users
INNER JOIN countries ON countries.country_code = users.country_code
ORDER BY country_name;
