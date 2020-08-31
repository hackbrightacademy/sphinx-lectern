"""sphinxlectern.common

Modules for both lecture notes and slides.
"""

from sphinx.application import Sphinx

from . import (
    doctest,
    graphviz,
    pdf,
    rstutil,
)


def setup(app: Sphinx):
    doctest.setup(app)
    graphviz.setup(app)
    pdf.setup(app)
    rstutil.setup(app)
