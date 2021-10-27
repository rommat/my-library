
import pytest
from pathlib import Path
import db_init.create_db as cr
import sqlite3


@pytest.fixture(scope='module')
def db_file():
    tmp_db_file = Path('test_sql.db')
    yield tmp_db_file
    tmp_db_file.unlink()


@pytest.fixture(autouse=True, scope='module')
def setup_db(db_file):
    cr.main(db_file, cr.CREATE_TABLES_SQL)


@pytest.fixture
def db_connection(db_file):
    connection = sqlite3.connect(db_file)
    yield connection
    connection.close()


@pytest.mark.sql
@pytest.mark.parametrize('table, column_names', [
    ('book', ['id', 'title', 'description', 'isbn', 'original_language', 'release_date']),
    ('author', ['id', 'first_name', 'last_name', 'birthday', 'death_date']),
    ('book_author', ['id', 'book_id', 'author_id'])
], ids=['book', 'author', 'book_author'])
def test_get_column_names_sql(table, column_names, db_connection):

    get_column_names_sql = """
        SELECT name FROM pragma_table_info(?);
    """
    result = db_connection.execute(get_column_names_sql, (table,))
    result = [row[0] for row in result]

    assert result == column_names



