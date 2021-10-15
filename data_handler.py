
"""
    Manage data
"""


import db_connection as db
import sqlite3
from db_init.create_db import DB_FILE


# DB_FILE = Path(__file__).parent / 'db_file' / 'mylibrary.db'


def list_all_items(table_name: str) -> list:

    conn = db.create_connection(DB_FILE)

    get_column_names_sql = f"""
        SELECT name FROM pragma_table_info('{table_name}');
    """
    column_names = db.execute_select(conn, get_column_names_sql)
    column_names = [column['name'] for column in column_names]

    get_all_items_sql = f"""
        SELECT {','.join(column_names)} FROM {table_name};
    """
    result_table = db.execute_select(conn, get_all_items_sql)

    conn.close()

    return result_table
