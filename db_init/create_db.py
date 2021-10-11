
"""
    Initial DB and tables creation
"""


from pathlib import Path
import sqlite3
import textwrap


DB_FILE = Path(__file__).parents[1] / 'db_file' / 'mylibrary.db'
CREATE_TABLES_SQL = Path(__file__).parent / 'create_tables.sql'


def create_connection(db_file: Path) -> sqlite3.Connection:
    """
    Create a database connection to a SQLite database specified by db_file
    """
    return sqlite3.connect(db_file)


def execute_script(db_conn: sqlite3.Connection, sql_script: str) -> sqlite3.Cursor:
    """
    Execute an SQL script
    """
    sql_script = textwrap.dedent(sql_script)
    return db_conn.executescript(sql_script)


def main(db_file: Path, sql_script: Path):

    # create connection to the database
    try:
        conn = create_connection(db_file)
        print("DB was created successfully.")
    except sqlite3.Error as err:
        print("DB was NOT created.")
        print(f"Error: {err}")
        exit()

    # extract sql script from the file
    try:
        with open(sql_script) as file_obj:
            create_tables_script = file_obj.read().rstrip()
    except FileNotFoundError as err:
        print(f"File {sql_script} was not found")
        print(f"Error: {err}")
        exit()

    # create tables
    try:
        execute_script(conn, create_tables_script)
        print("All tables were created successfully.")
    except sqlite3.Error as err:
        print("Tables were NOT created")
        print(f"Error: {err}")
        exit()

    conn.close()


if __name__ == '__main__':
    main(DB_FILE, CREATE_TABLES_SQL)
