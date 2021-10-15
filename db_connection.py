
"""
    Manages Database Connection
"""


from pathlib import Path
import sqlite3
import textwrap


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
