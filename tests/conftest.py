
import pytest


def pytest_addoption(parser):
    parser.addoption('--integration', action='store_true')


@pytest.fixture
def is_integration(pytestconfig):
    yield pytestconfig.getoption("integration")
