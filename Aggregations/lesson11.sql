-- Write an SQL statement that returns two columns, the country_code and 
-- the average age of users for records with that country_code. The 
-- marketing team has asked that we round the average to the 
-- nearest whole number and rename the column that contains the average age to average_age.

SELECT country_code , ROUND(AVG(age)) as average_age FROM users
GROUP BY country_code;