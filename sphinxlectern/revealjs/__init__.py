"""RevealJS extenstion for Sphinx."""

from sphinx.application import Sphinx

from . import (incremental,
               interslide,
               newslide,
               speakernote, )


def setup(app: Sphinx) -> None:
    incremental.setup(app)
    interslide.setup(app)
    newslide.setup(app)
    speakernote.setup(app)