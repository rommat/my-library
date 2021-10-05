
"""
    Initial DB and tables creation
"""


from pathlib import Path
import sqlite3


DB_FILE = Path(__file__).parents[1] / 'db_file' / 'mylibrary.db'


def create_connection(db_file):
    """
    Create a database connection to a SQLite database specified by db_file
    """
    try:
        db_conn = sqlite3.connect(db_file)
        return db_conn
    except sqlite3.Error as err:
        return err


def create_table(db_conn, sql_stmt):
    """
    Create a table from the SQL statement
    :param db_conn: Connection object
    :param sql_stmt: a CREATE TABLE statement
    """
    try:
        cursor = db_conn.cursor()
        cursor.execute(sql_stmt)
    except sqlite3.Error as err:
        return err


if __name__ == '__main__':
    # create a database connection
    conn = create_connection(DB_FILE)

    if isinstance(conn, sqlite3.Error):
        print("DB was NOT created.")
        print(conn)

    elif isinstance(conn, sqlite3.Connection):
        print("DB was created successfully.")

        # create tables
        cr_tab_stmts = {
            'books': """
                CREATE TABLE IF NOT EXISTS books (
                    book_id integer PRIMARY KEY,
                    title text NOT NULL,
                    description text,
                    isbn text, 
                    original_language text,
                    release_date text
                );
            """,
            'authors': """
                CREATE TABLE IF NOT EXISTS authors (
                    author_id integer PRIMARY KEY,
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    birthday text,
                    death_date text 
                );
            """,
            'writtenby': """
                CREATE TABLE IF NOT EXISTS writtenby (
                    record_id integer PRIMARY KEY,
                    author_id integer NOT NULL,
                    book_id integer NOT NULL
                );
            """
        }
        errors = {}
        for tab in cr_tab_stmts:
            msg = create_table(conn, cr_tab_stmts[tab])
            if msg:
                errors[tab] = msg

        # close the database connection
        conn.close()

        if errors:
            print(f"{len(errors)} tables were NOT created.")
            for tab in errors:
                print(f"{tab}: {errors[tab]}")
        else:
            print("All tables were created successfully.")
