"""sphinxlectern.writers"""

from sphinx.application import Sphinx

from . import (handouts,
               revealjs,
               )


def setup(app: Sphinx):
    handouts.setup(app)
    revealjs.setup(app)