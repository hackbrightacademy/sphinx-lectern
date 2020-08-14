"""This is deprecated.

See DeprecationWarning on line 26.
"""

from docutils.parsers.rst import directives
from sphinx.directives.code import container_wrapper
from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info
import sphinx.ext.doctest as sphinx_doctest
from sphinx.util import logging

logger = logging.getLogger(__name__)


class DisplayCodeMixin:
    option_spec = {
        'hide': directives.flag,
        'options': directives.unchanged,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }

    def run(self) -> None:
        logger.warning('DeprecationWarning: doctest directives will be deprecated due to lack of interest. Please use code-block or literalinclude instead.')

        node = super().run()[0]

        # This code copied from sphinx.directives.code
        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = [x + 1 for x in parselinenos(linespec, nlines)]
            except ValueError as err:
                document = self.state.document
                return [document.reporter.warning(str(err), line=self.lineno)]
        else:
            hl_lines = None

        node['classes'] += self.options.get('class', [])
        extra_args = node['highlight_args'] = {}
        if hl_lines is not None:
            extra_args['hl_lines'] = hl_lines
        if 'lineno-start' in self.options:
            extra_args['linenostart'] = self.options['lineno-start']
        set_source_info(self, node)

        caption = self.options.get('caption')
        if caption:
            try:
                node = container_wrapper(self, node, caption)
            except ValueError as exc:
                document = self.state.document
                errmsg = _('Invalid caption: %s' % exc[0][0].astext())
                return [document.reporter.warning(errmsg, line=self.lineno)]

        self.add_name(node)

        return [node]


class DoctestDirective(DisplayCodeMixin, sphinx_doctest.DoctestDirective):
    pass


class TestcodeDirective(DisplayCodeMixin, sphinx_doctest.TestcodeDirective):
    pass


class TestoutputDirective(DisplayCodeMixin,
                          sphinx_doctest.TestoutputDirective):
    pass


def setup(app):
    """Monkey-patch our augmented versions of default doctest directives."""

    sphinx_doctest.DoctestDirective = DoctestDirective
    sphinx_doctest.TestcodeDirective = TestcodeDirective
    sphinx_doctest.TestoutputDirective = TestoutputDirective

    return sphinx_doctest.setup(app)
