"""Sphinx extensions for building handouts and slides."""

from sphinx.application import Sphinx

from . import (
    admonitions,
    doctest,
    fillin,
    graphviz,
    pdf,
    togglereveal,
    rstutil,
    revealjs as revealjs_ext
)
from .transformers import references
from .writers import handouts, revealjs


def setup(app: Sphinx) -> None:
    handouts.setup(app)
    revealjs.setup(app)
    admonitions.setup(app)
    doctest.setup(app)
    fillin.setup(app)
    graphviz.setup(app)
    pdf.setup(app)
    togglereveal.setup(app)
    rstutil.setup(app)
    revealjs_ext.setup(app)
    references.setup(app)