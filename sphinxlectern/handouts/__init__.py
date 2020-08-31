"""sphinxlectern.handouts

Modules for building lecture notes.
"""

from sphinx.application import Sphinx

from . import admonitions, fillin, togglereveal


def setup(app: Sphinx):
    admonitions.setup(app)
    fillin.setup(app)
    togglereveal.setup(app)
