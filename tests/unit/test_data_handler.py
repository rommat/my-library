
import data_handler as dh
from unittest.mock import patch


@patch('data_handler.db')
def test_get_column_names(mock_db):
    mock_db.execute_select.return_value = [
        {'name': 'id'}, {'name': 'title'}, {'name': 'description'}, {'name': 'isbn'},
        {'name': 'original_language'}, {'name': 'release_date'}
    ]
    column_names = dh.get_column_names('connection', 'sql_statement')
    expected_names = ['id', 'title', 'description', 'isbn', 'original_language', 'release_date']
    assert column_names == expected_names


def test_get_items_info():

    assert 1


def test_get_related_info():

    assert 1


def test_add_column():

    assert 1


def test_list_all_items():

    assert 1


def test_get_item():

    assert 1
