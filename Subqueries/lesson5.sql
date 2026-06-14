-- Finance has found that people who have lived longer than 40 years need to start thinking about retirement. Write a query that returns all columns for all users who are more than 40 years old.

-- Unfortunately, this table awkwardly stores age in days in the age_in_days field! Use a subquery to convert 40 years → days and filter on that. Assume every year has 365 days.

select * from users
where age_in_days > (
    SELECT 40 * 365
);