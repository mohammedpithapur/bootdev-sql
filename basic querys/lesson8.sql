-- Our HR team is dealing with a ticket from one of our users, but they're having trouble pulling up their record in the database. They are pretty sure the user's name starts with Al.

-- Write a query that returns all fields for records where the user's name starts with Al.

SELECT * FROM users
WHERE name LIKE 'Al%';