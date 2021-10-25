
"""
    Managed commands
"""


import sqlite3
import data_handler as dh
import output_processing as out


def book_list(authors):
    related_item = 'author' if authors else None
    try:
        result_table = dh.list_all_items('book', related_item)
        out.table2console(result_table)
    except sqlite3.Error as err:
        print(f"Error: {err}")


def book_get(parameters, authors):
    related_item = 'author' if authors else None
    try:
        result = dh.get_item('book', parameters, related_item)
        if len(result) == 1:
            out.row2console(result[0])
        else:
            out.table2console(result)
    except sqlite3.Error as err:
        print(f"Error: {err}")


def author_list(books):
    related_item = 'book' if books else None
    try:
        result_table = dh.list_all_items('author', related_item)
        out.table2console(result_table)
    except sqlite3.Error as err:
        print(f"Error: {err}")


def author_get(parameters, books):
    related_item = 'book' if books else None
    try:
        result = dh.get_item('author', parameters, related_item)
        if len(result) == 1:
            out.row2console(result[0])
        else:
            out.table2console(result)
    except sqlite3.Error as err:
        print(f"Error: {err}")
