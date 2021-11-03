
import pytest
from pathlib import Path
import sqlite3
import textwrap

import db_init.create_db as cr


def pytest_addoption(parser):
    parser.addoption('--integration', action='store_true')


@pytest.fixture
def is_integration(pytestconfig):
    yield pytestconfig.getoption("integration")


@pytest.fixture(scope='module')
def temp_db_file():
    opened_files = []

    def _temp_db_file(file_path: Path):
        opened_files.append(file_path)
        if file_path.is_file():
            file_path.unlink()
        return file_path

    yield _temp_db_file

    for file in opened_files:
        if file.is_file():
            file.unlink()


@pytest.fixture
def db_connection():
    opened_connection = []

    def _db_connection(db_file: Path) -> sqlite3.Connection:
        connection = sqlite3.connect(db_file)
        opened_connection.append(connection)
        return connection

    yield _db_connection

    for conn in opened_connection:
        conn.close()


@pytest.fixture
def execute_script():
    """
    Execute an SQL script
    """
    def _execute_script(db_connection: sqlite3.Connection, sql_script: str) -> sqlite3.Cursor:
        sql_script = textwrap.dedent(sql_script)
        return db_connection.executescript(sql_script)

    yield _execute_script


@pytest.fixture
def read_txt_file():
    """
    Return content of a text file
    """
    opened_files = []

    def _read_txt_file(file_path: Path) -> str:
        file_obj = open(Path(file_path))
        opened_files.append(file_obj)
        return file_obj.read().rstrip()

    yield _read_txt_file

    for file in opened_files:
        file.close()


@pytest.fixture()
def setup_db(read_txt_file, execute_script):

    def _setup_db(db_connection: sqlite3.Connection, populate_tables_file: Path) -> sqlite3.Cursor:
        create_tables_file = Path(__file__).parents[1] / 'db_init/create_tables.sql'
        sql_script = read_txt_file(create_tables_file)
        sql_script += read_txt_file(populate_tables_file)
        return execute_script(db_connection, sql_script)

    yield _setup_db
