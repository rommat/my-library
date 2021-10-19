
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


def get_items_info(db_conn: sqlite3.Connection, table_name: str, column_names: list, parameters=None) -> list:

    where_clause = ""
    if parameters:
        where_clause = "WHERE " + " AND ".join(
            [f"{name}={parameters[name]}" if name == 'id' else
             f"{name}='{parameters[name]}'" for name in parameters]
        )
    get_items_sql = f"""
        SELECT {','.join(column_names)} FROM {table_name} {where_clause};
    """

    return db.execute_select(db_conn, get_items_sql)


def get_related_info(db_conn: sqlite3.Connection, table_name: str, related_item: str, item_id=None) -> dict:

    select_clause = {
        'book': "b.title book",
        'author': "a.first_name || ' ' || a.last_name author"
    }
    where_clause = ""
    if item_id:
        where_clause += f"WHERE ba.{table_name}_id = {item_id}"

    get_authors_books_sql = f"""
        SELECT ba.{table_name}_id id, {select_clause[related_item]}
        FROM book b, author a  
        INNER JOIN book_author ba 
            ON a.id = ba.author_id AND b.id = ba.book_id
        {where_clause};
    """
    additional_table = db.execute_select(db_conn, get_authors_books_sql)
    related_info = {}
    for row in additional_table:
        try:
            related_info[row['id']].append(row[related_item])
        except KeyError:
            related_info[row['id']] = [row[related_item]]

    return related_info


def list_all_items(table_name: str, related_item: str):

    try:
        conn = db.create_connection(DB_FILE)
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return False

    column_names = get_column_names(conn, table_name)

    result_table = get_items_info(conn, table_name, column_names)

    if related_item:
        related_info = get_related_info(conn, table_name, related_item)
        # --Add an extra column to the result
        for row in result_table:
            try:
                row[related_item] = related_info[row['id']]
            except KeyError:
                row[related_item] = None

    conn.close()

    return result_table


def get_item(table_name: str, parameters: dict, related_item: str):

    try:
        conn = db.create_connection(DB_FILE)
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return False

    column_names = get_column_names(conn, table_name)

    result = get_items_info(conn, table_name, column_names, parameters)[0]

    if related_item:
        item_id = result['id']
        related_info = get_related_info(conn, table_name, related_item, item_id)
        # --Add an extra column to the result
        try:
            result[related_item] = related_info[item_id]
        except KeyError:
            result[related_item] = None

    conn.close()

    return result
