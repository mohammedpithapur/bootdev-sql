-- Our marketing team is trying to determine the best marketing channels 
-- to advertise through, but they need more information about our current users. They want 
-- to know the average age of users in the United States.

SELECT AVG(age) from users
where country_code = 'US';