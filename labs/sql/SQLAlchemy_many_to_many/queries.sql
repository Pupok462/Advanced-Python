SELECT users.username, authors.name, users.id, authors.user_id from users join authors on users.id = authors.user_id

SELECT authors.name, posts.name, authors.id, posts.author_id from authors left outer join posts  on authors.id = posts.author_id

SELECT tags.name AS tags_name
FROM tags;
SELECT posts.name AS posts_name
FROM posts;


SELECT users.username AS users_username, authors.name AS authors_name, posts.name AS posts_name, tags.name AS tags_name
FROM users JOIN authors ON users.id = authors.user_id JOIN posts ON authors.id = posts.author_id JOIN posts_tags_table AS posts_tags_table_1 ON posts.id = posts_tags_table_1.post_id JOIN tags ON tags.id
 = posts_tags_table_1.tag_id
WHERE users.username = 'Jack'


