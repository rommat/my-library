
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


def execute_select(db_conn: sqlite3.Connection, sql_query: str) -> list:
    """
    Execute an SQL SELECT statement
    """
    sql_query = textwrap.dedent(sql_query)
    db_conn.row_factory = sqlite3.Row
    query_result = db_conn.execute(sql_query)
    field_names = [desc[0] for desc in query_result.description]
    result_table = [
        {field: row[field] for field in field_names}
        for row in query_result
    ]
    return result_table
