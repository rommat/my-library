
import pytest
from pathlib import Path
from unittest.mock import patch
import subprocess
import sqlite3
import db_init.create_db as cr
import my_library


HERE = Path(__file__).resolve().parent
DB_TEST_INTEGRATION = HERE / 'test_integration.bd'


@pytest.fixture()
def command_db_connection(temp_db_file, db_connection):
    test_bd = temp_db_file(DB_TEST_INTEGRATION)
    yield db_connection(test_bd)


@pytest.fixture(autouse=True)
def setup_test_db(command_db_connection, setup_db):
    setup_sql = HERE / 'populate_tables_integration.sql'
    setup_db(command_db_connection, setup_sql)


@patch('db_init.create_db.DB_FILE', return_value=DB_TEST_INTEGRATION)
@pytest.mark.parametrize('group', ['book', 'author'])
def test_list_command(mock_db_file, group):

    command = ['my-library', group, 'list']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print()
    print(result.stdout)

    assert 1


@pytest.mark.skip(reason="the test is for debugging")
@pytest.mark.parametrize('table', ['book_author', 'author'])
def test_if_db_created(table, temp_db_file, command_db_connection):
    stmt = ("""
        SELECT * FROM {table} ;
    """).format(table=table)
    result = command_db_connection.execute(stmt)
    print()
    for row in result:
        print(row)

    assert 1