-- HR has been able to narrow down their query further! 
-- They want a report of all user data for users whose names start with Al and are exactly 5 characters long.
SELECT * FROM users
WHERE name LIKE "Al___";