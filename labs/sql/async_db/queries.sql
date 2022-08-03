SELECT authors.id, authors.created_at, authors.name, authors.user_id, authors.books
FROM authors JOIN users ON users.id = authors.user_id
WHERE users.username = 'Sam'
