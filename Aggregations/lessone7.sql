-- A new page in the CashPal app allows users to see how much money 
-- they've spent on a specific kind of transaction, and alerts them if that amount is fairly large. 
-- Let's write a query that returns the total amount spent by each user on lunch when that 
-- balance is greater than 20.

SELECT sender_id, SUM(amount) as balance FROM transactions
WHERE sender_id IS NOT NULL and was_sucssesful = TRUE AND note like "%lunch%"
GROUP BY sender_id
HAVING SUM(amount) > 20
ORDER BY balance;