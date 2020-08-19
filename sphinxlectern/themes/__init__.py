from sphinx.application import Sphinx

from sphinx.testing.path import path

def setup(app: Sphinx) -> None:
    app.add_html_theme('revealjs',
                       path(__file__).parent.abspath() / 'revealjs',
                       )
    app.add_html_theme('handouts',
                       path(__file__).parent.abspath() / 'handouts',
                       )
