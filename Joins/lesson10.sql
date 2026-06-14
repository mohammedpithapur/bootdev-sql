SELECT users.name, users.username, count(support_tickets.id) as support_ticket_count from users
INNER JOIN support_tickets
on support_tickets.user_id = users.id
WHERE issue_type != "Account Access" 
GROUP BY users.id
HAVING support_ticket_count >1
ORDER BY support_ticket_count DESC;