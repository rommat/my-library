
"""
    Manage output
"""


from prettytable import PrettyTable
import textwrap


MAX_COLUMN_WIDTH = 40
MAX_ROW_HEIGHT = 8


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
        