
"""
    Manage output
"""


import prettytable
from prettytable import PrettyTable, ALL, NONE
import textwrap


MAX_COLUMN_WIDTH = 40
MAX_ROW_HEIGHT = 5
MAX_ROW_WIDTH = 70


def table2console(table: list):
    """
    Format table and print it to console
    """
    output_table = PrettyTable()

    if not table:
        print("No data")
    else:
        column_names = table[0].keys()
        output_table.field_names = column_names
        for row in table:
            new_row = []
            for column in column_names:
                column_value = row[column]
                if isinstance(column_value, list):
                    column_value = ', \n'.join(column_value)
                    output_table.align[column] = 'l'
                column_value_str = str(column_value)
                if len(column_value_str) > MAX_COLUMN_WIDTH:
                    column_value = textwrap.fill(column_value_str, MAX_COLUMN_WIDTH, max_lines=MAX_ROW_HEIGHT)
                    output_table.align[column] = 'l'
                new_row.append(column_value)
            output_table.add_row(new_row)

        print(output_table.get_string())


def row2console(row: dict):
    """
    Format 1-row table and print it to console
    """
    output_table = PrettyTable()

    if not row:
        print("No data")
    else:
        output_table.add_column('name', list(row.keys()))
        value_column = []
        for item in row.values():
            if isinstance(item, list):
                item = ', \n'.join(item)
            if len(str(item)) > MAX_ROW_WIDTH:
                item = textwrap.fill(item, MAX_ROW_WIDTH)
            value_column.append(item)
        output_table.add_column('value', value_column)
        output_table.align['name'] = 'r'
        output_table.align['value'] = 'l'
        output_table.header = False
        output_table.hrules = prettytable.ALL
        output_table.vrules = prettytable.NONE

        print(output_table.get_string())
