SELECT * from transactions
where user_id = (
    SELECT id from users
    where name='David'
);