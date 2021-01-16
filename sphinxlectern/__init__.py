"""Sphinx extensions for building handouts and slides."""

from sphinx.application import Sphinx

from . import (
    common,
    handouts,
    revealjs,
    themes,
    writers,
    mcq,
    pdf,
)
from .transformers import references


def setup(app: Sphinx) -> None:
    common.setup(app)
    handouts.setup(app)
    revealjs.setup(app)
    themes.setup(app)
    writers.setup(app)
    references.setup(app)
    pdf.setup(app)
