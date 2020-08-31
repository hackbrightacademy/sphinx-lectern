from pytest import Session

import os
import shutil

import pytest
from bs4 import BeautifulSoup
from sphinx.cmd.build import build_main
from sphinx.testing.path import path
from sphinx.testing import comparer

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


def pytest_configure(config):
    config.addinivalue_line("markers", "builder(name): mark test on specific builder")


@pytest.fixture
def build_contents(request):
    marker = request.node.get_closest_marker("builder")

    if marker is None:
        return None
    else:
        builder = marker.args[0]
        example_dir = path(__file__).parent.abspath() / "examples" / f"test_{builder}"
        argv = [
            "-b",
            builder,
            example_dir,
            example_dir / "_build",
        ]
        build_main(argv)

        with open(example_dir / "_build" / "index.html") as f:
            contents = f.read()

        return BeautifulSoup(contents, "html.parser")


def pytest_assertrepr_compare(op, left, right):
    comparer.pytest_assertrepr_compare(op, left, right)
