-- Using a subquery, write an SQL statement that retrieves full user records for every user who:

-- Matches the sender_id in a transaction with "invoice" or "tax" mentioned anywhere in the transaction note.
-- And is not an admin.

SELECT * from users
WHERE id IN (
    select sender_id from transactions
    WHERE note like "%invoice%" or note like "%tax%"
) and is_admin = FALSE;