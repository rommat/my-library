
"""
    Manage data
"""


import db_connection as db
import sqlite3
from db_init.create_db import DB_FILE


# DB_FILE = Path(__file__).parent / 'db_file' / 'mylibrary.db'


def get_column_names(db_conn: sqlite3.Connection, table_name: str) -> list:

    get_column_names_sql = f"""
        SELECT name FROM pragma_table_info('{table_name}');
    """
    column_names = db.execute_select(db_conn, get_column_names_sql)

    return [column['name'] for column in column_names]


def list_all_items(table_name: str, related_item=None) -> list:

    try:
        conn = db.create_connection(DB_FILE)
    except sqlite3.Error as err:
        print(f"Error: {err}")
        exit(1)

    # ------GET ALL ITEMs

    column_names = get_column_names(conn, table_name)

    get_all_items_sql = f"""
        SELECT {','.join(column_names)} FROM {table_name};
    """
    result_table = db.execute_select(conn, get_all_items_sql)

    # ------GET RELATED INFO

    if related_item:
        select_clause = {
            'book': "b.title book",
            'author': "a.first_name || ' ' || a.last_name author"
        }
        get_authors_books_sql = f"""
            SELECT ba.{table_name}_id id, {select_clause[related_item]}
            FROM book b, author a  
            INNER JOIN book_author ba 
                ON a.id = ba.author_id AND b.id = ba.book_id;
        """
        additional_table = db.execute_select(conn, get_authors_books_sql)
        related_info = {}
        for row in additional_table:
            try:
                related_info[row['id']].append(row[related_item])
            except KeyError:
                related_info[row['id']] = [row[related_item]]

        # --Add an extra column to the result
        for row in result_table:
            try:
                row[related_item] = related_info[row['id']]
            except KeyError:
                row[related_item] = None

    conn.close()

    return result_table
