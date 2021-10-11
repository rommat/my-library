
--enable foreign key support
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS book (
    id integer PRIMARY KEY,
    title text NOT NULL,
    description text,
    isbn text,
    original_language text CHECK(original_language IN ('EN', 'RU', 'UA')),
    release_date text
);
CREATE TABLE IF NOT EXISTS author (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    birthday text,
    death_date text
);
CREATE TABLE IF NOT EXISTS book_author (
    book_id integer NOT NULL,
    author_id integer NOT NULL,
    PRIMARY KEY (book_id, author_id)
    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);
