"""Sphinx extensions for building handouts and slides."""

from sphinx.application import Sphinx

from . import (
    common,
    handouts,
    revealjs,
    themes,
    writers,
    mcq,
)
from .transformers import references


def setup(app: Sphinx) -> None:
    common.setup(app)
    handouts.setup(app)
    revealjs.setup(app)
    themes.setup(app)
    writers.setup(app)
    references.setup(app)
    mcq.setup(app)

    def debug_doctree(app, doctree):
        import pdb

        pdb.set_trace()

    def output_doctree(app, doctree):

        print(doctree.traverse())

    app.connect("doctree-read", output_doctree)
