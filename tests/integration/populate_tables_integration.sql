
--enable foreign key support
PRAGMA foreign_keys = ON;


INSERT INTO book (title, description, isbn, original_language, release_date) VALUES (
    'Database Systems: The Complete Book, 2nd Edition',
    'Database Systems: The Complete Book is ideal for Database Systems and Database Design and Application courses offered at the junior, senior and graduate levels in Computer Science departments. A basic understanding of algebraic expressions and laws, logic, basic data structure, OOP concepts, and programming environments is implied. Written by well-known computer scientists, this introduction  to database systems offers a comprehensive approach, focusing on database design, database use, and implementation of database applications and database management systems.',
    '978-0131873254',
    'EN',
    '2008-06-05'
);
INSERT INTO book (title, description, isbn, original_language, release_date) VALUES (
    'A First Course in Database Systems, 3rd Edition',
    'Written by well-known computer scientists, this accessible and succinct introduction to database systems focuses on database design and use. It provides in-depth coverage of databases from the point of view of the database designer, user, and application programmer. The authors provide an overview of important programming systems (e.g., SQL, JDBC, PSM, CLI, PHP, XQuery, etc.) and the intellectual framework to put them into context. For software engineers, database engineers, and programmers.',
    '978-0136006374',
    'EN',
    '2007-09-26'
);

INSERT INTO author (first_name, last_name, birthday, death_date) VALUES (
    'Jeffrey', 'Ullman', '1942-11-22', NULL
);
INSERT INTO author (first_name, last_name, birthday, death_date) VALUES (
    'Jennifer', 'Widom', NULL, NULL
);
INSERT INTO author (first_name, last_name, birthday, death_date) VALUES (
    'Hector', 'Garcia-Molina', '1954-11-15', '2019-11-25'
);

INSERT INTO book_author (book_id, author_id)
SELECT b.id, a.id 
FROM book b, author a 
WHERE b.title = 'Database Systems: The Complete Book, 2nd Edition' 
    AND a.first_name = 'Hector' 
    AND a.last_name = 'Garcia-Molina';

INSERT INTO book_author (book_id, author_id)
SELECT b.id, a.id 
FROM book b, author a 
WHERE b.title = 'Database Systems: The Complete Book, 2nd Edition' 
    AND a.first_name = 'Jeffrey' 
    AND a.last_name = 'Ullman';

INSERT INTO book_author (book_id, author_id)
SELECT b.id, a.id 
FROM book b, author a 
WHERE b.title = 'Database Systems: The Complete Book, 2nd Edition' 
    AND a.first_name = 'Jennifer' 
    AND a.last_name = 'Widom';

INSERT INTO book_author (book_id, author_id)
SELECT b.id, a.id 
FROM book b, author a 
WHERE b.title = 'A First Course in Database Systems, 3rd Edition' 
    AND a.first_name = 'Jeffrey' 
    AND a.last_name = 'Ullman';

INSERT INTO book_author (book_id, author_id)
SELECT b.id, a.id 
FROM book b, author a 
WHERE b.title = 'A First Course in Database Systems, 3rd Edition' 
    AND a.first_name = 'Jennifer' 
    AND a.last_name = 'Widom';
