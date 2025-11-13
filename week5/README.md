# Week 5 – MySQL

## Task 2
```sql
CREATE DATABASE website;
USE website;
CREATE TABLE member(
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  follower_count INT UNSIGNED NOT NULL DEFAULT 0,
  `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
## Task 3
```sql
INSERT INTO member(name,email,password) VALUES ('test','test@test.com','test');
INSERT INTO member(name,email,password) VALUES ('test11','test11@test11.com','test11');
INSERT INTO member(name,email,password) VALUES ('test22','test22@test22.com','test22');
INSERT INTO member(name,email,password) VALUES ('test33','test33@test33.com','test33');
INSERT INTO member(name,email,password) VALUES ('test44','test44@test44.com','test44');
SELECT * FROM member;
SELECT * FROM member ORDER BY `time` DESC;
SELECT * FROM member ORDER BY `time` DESC LIMIT 3 OFFSET 1;
SELECT * FROM member WHERE email = 'test@test.com';
SELECT * FROM member WHERE name LIKE '%es%';
SELECT * FROM member WHERE email ='test@test.com' AND password = 'test';
UPDATE member SET name = 'test2' WHERE email = 'test@test.com';
```
## Task 4
```sql
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;
SELECT AVG(follower_count) AS avg_followers FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC
    LIMIT 2
) AS top_two;
```
## Task 5
```sql
CREATE TABLE message (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
member_id  INT UNSIGNED NOT NULL,
content TEXT NOT NULL,
like_count INT UNSIGNED NOT NULL DEFAULT 0,
`time` DATETIME DEFAULT CURRENT_TIMESTAMP  NOT NULL,
FOREIGN KEY (member_id) REFERENCES member (id)
);
SELECT member.name, message.content, message.time FROM member
INNER JOIN message ON member.id = message.member_id;
SELECT member.name, member.email, message.content, message.time
FROM member
INNER JOIN message ON member.id = message.member_id
WHERE member.email = 'test@test.com';
SELECT member.email, AVG(message.like_count) AS avg_like
FROM message
INNER JOIN member ON message.member_id = member.id
WHERE member.email = 'test@test.com';
SELECT member.email, AVG(message.like_count) AS avg_like
FROM message
INNER JOIN member ON message.member_id = member.id
GROUP BY member.email;
```