
"""
    Initial DB and tables creation
"""


from pathlib import Path
import sqlite3
# from sqlite3 import Error


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


if __name__ == '__main__':
    # create a database connection
    conn = create_connection(DB_FILE)

    if isinstance(conn, sqlite3.Error):
        print("DB was NOT created.")
        print(conn)

    if isinstance(conn, sqlite3.Connection):
        print("DB was created successfully.")
