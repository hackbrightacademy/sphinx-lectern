from pytest import Session

import os

import pytest
from sphinx.testing.path import path
from sphinx.testing import comparer

pytest_plugins = 'sphinx.testing.fixtures'
collect_ignore = ['roots']


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'examples'

    
def pytest_assertrepr_compare(op, left, right):
    comparer.pytest_assertrepr_compare(op, left, right)

    
def _initialize_test_directory(session: Session):
    if 'SPHINX_TEST_TEMPDIR' in os.environ:
        tempdir = os.path.abspath(os.getenv('SPHINX_TEST_TEMPDIR'))
        print('Temporary files will be placed in %s.' % tempdir)

        if os.path.exists(tempdir):
            shutil.rmtree(tempdir)

        os.makedirs(tempdir)


def pytest_sessionstart(session: Session):
    _initialize_test_directory(session)