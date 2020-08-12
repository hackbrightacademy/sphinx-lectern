from bs4 import BeautifulSoup
import pytest


@pytest.mark.builder('revealjs')
def test_html4_output(build_contents: BeautifulSoup):
    assert build_contents.body is not None