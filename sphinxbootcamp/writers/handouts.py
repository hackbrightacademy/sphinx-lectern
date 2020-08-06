"""Sphinx writer for handouts."""

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.builders.singlehtml import SingleFileHTMLBuilder

from ._html5 import HTML5Translator
from ._no_additional_pages import DontBuildAdditionalPages


class HandoutsTranslator(HTML5Translator):
    """Translator for Sphinx structure -> Hackbright HTML handouts.

    Overrides Sphinx HTML translator.
    """

    _previous_title = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings.field_name_limit = 50

    def _merge_consecutive_title(self, node):
        """Merge consecutive section titles.

        When a section has the same title as the previous, don't render it.
        """

        if str(node) == self._previous_title:
            raise nodes.SkipNode
        self._previous_title = str(node)

    def _after_hint_title(self):
        """Hide contents of hints in <details> tag."""

        self.body.append('<details class="admonition-body">')
        self.body.append('<summary></summary>')

    def visit_title(self, node: nodes.Node) -> None:
        if isinstance(node.parent, nodes.section):
            self._merge_consecutive_title(node)

        super().visit_title(node)

    def depart_title(self, node: nodes.Node) -> None:
        super().depart_title(node)
        if isinstance(node.parent, nodes.hint):
            self._after_hint_title()

    def visit_admonition(self, node: nodes.Node, name: str = '') -> None:
        self.body.append(self.starttag(
            node, 'div', CLASS=('admonition ' + name)))

    def depart_hint(self, node: nodes.Node) -> None:
        self.body.append('</details>')
        super().depart_hint(node)


class HandoutsBuilder(DontBuildAdditionalPages):
    """Builder for making HTML handouts using Sphinx."""

    name = 'handouts'


class SinglePageHandoutsBuilder(SingleFileHTMLBuilder):
    name = 'singlepage'


def setup(app: Sphinx) -> None:
    app.add_builder(HandoutsBuilder)
    app.add_builder(SinglePageHandoutsBuilder)
    app.set_translator('handouts', HandoutsTranslator)
    app.set_translator('singlepage', HandoutsTranslator)
    app.add_config_value('handouts_theme', 'handouts', 'env')
    app.add_config_value('handouts_imgmath_dvipng_args', [], 'env')
