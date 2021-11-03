
import pytest
from pathlib import Path
from unittest.mock import patch
import data_handler as dh


HERE = Path(__file__).resolve().parent


# ------SETUP TEST DB FOR SQL TESTING

@pytest.fixture()
def sql_db_connection(temp_db_file, db_connection):
    test_db = temp_db_file(HERE / 'test_sql.bd')
    yield db_connection(test_db)


@pytest.fixture(autouse=True)
def setup_test_db(sql_db_connection, setup_db):
    setup_sql = HERE / 'populate_tables_sql.sql'
    setup_db(sql_db_connection, setup_sql)


@pytest.mark.sql
@pytest.mark.parametrize(('table_name', 'expected_names'), [
    ('book', ['id', 'title', 'description', 'isbn', 'original_language', 'release_date']),
    ('author', ['id', 'first_name', 'last_name', 'birthday', 'death_date']),
    ('book_author', ['id', 'book_id', 'author_id'])
], ids=['book', 'author', 'book_author'])
def test_get_column_names(table_name, expected_names, sql_db_connection):
    column_names = dh.get_column_names(sql_db_connection, table_name)
    assert column_names == expected_names


@pytest.mark.sql
def test_get_items_info():
    assert 1


@pytest.mark.sql
def test_get_related_info():
    assert 1


def test_add_column():
    assert 1


@patch('data_handler.get_related_info', return_value={
    101: ['Romeo and Juliet'],
    102: ['Dandelion Wine', 'Farewell Summer']
})
@patch('data_handler.get_items_info', return_value=[
    {'id': 101, 'first_name': 'William', 'last_name': 'Shakespeare'},
    {'id': 102, 'first_name': 'Ray', 'last_name': 'Bradbury'}
])
@patch('data_handler.get_column_names', return_value=['id', 'first_name', 'last_name'])
def test_list_all_items(mock_column_names, mock_items_info, mock_related_info):
    result = dh.list_all_items('author', 'book')

    assert result == [{'id': 101, 'first_name': 'William', 'last_name': 'Shakespeare',
                       'book': ['Romeo and Juliet']},
                      {'id': 102, 'first_name': 'Ray', 'last_name': 'Bradbury',
                       'book': ['Dandelion Wine', 'Farewell Summer']}]


def test_get_item():
    assert 1


@pytest.mark.skip(reason="the test is for debugging")
@pytest.mark.parametrize('table', ['book', 'author', 'book_author'])
def test_if_db_created(table, temp_db_file, sql_db_connection):
    stmt = ("""
        SELECT * FROM {table} ;
    """).format(table=table)
    result = sql_db_connection.execute(stmt)
    print()
    for row in result:
        print(row)

    assert 1
