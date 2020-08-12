from typing import List, Callable
from sphinx.writers.html5 import HTML5Translator

from docutils.nodes import Node, SkipNode

from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
import sphinx.ext.graphviz as sphinx_graphviz


def attach_style_options(c: sphinx_graphviz.Graphviz):
    """Give Graphviz directive options to add 'style' HTML attribute.

    This will give you two options --- revealjs & handouts --- that
    are used to render a 'style' HTML attribute in order to resize
    dot-rendered SVGs.

        .. digraph::
          :revealjs: height: 50%;
          :handouts: width: 100%;

    """

    sphinx_graphviz.Graphviz.option_spec.update(
        {'revealjs': directives.unchanged,
         'handouts': directives.unchanged}
    )
    c.option_spec = sphinx_graphviz.Graphviz.option_spec

    def run(self) -> List[Node]:
        node = super(c, self).run()[0]
        node['revealjs'] = self.options.get('revealjs', 'width: 100%;')
        node['handouts'] = self.options.get('handouts', 'width: 100%;')

        return [node]

    c.run = run

    return c


@attach_style_options
class Graphviz(sphinx_graphviz.Graphviz):
    pass


@attach_style_options
class GraphvizSimple(sphinx_graphviz.GraphvizSimple):
    pass


def visit_graphviz_for(builder_name: str) -> Callable:
    """Return visit_graphviz function for given builder."""

    def visit_graphviz(self: HTML5Translator,
                       node: sphinx_graphviz.graphviz) -> None:
        if builder_name in node:
            self.body.append(f'<div class="resizer" style="{node[builder_name]}">')
        else:
            self.body.append(f'<div class="resizer">')

        try:
            sphinx_graphviz.render_dot_html(self,
                                            node,
                                            node['code'],
                                            node['options'])
        except SkipNode:
            self.body.append('</div>')

        raise SkipNode

    return visit_graphviz


def setup(app):
    """Monkey-patch our augmented versions of default doctest directives."""

    sphinx_graphviz.Graphviz = Graphviz
    sphinx_graphviz.GraphvizSimple = GraphvizSimple
    sphinx_graphviz.setup(app)
    app.add_node(sphinx_graphviz.graphviz,
                 html=(visit_graphviz_for('html'), None),
                 revealjs=(visit_graphviz_for('revealjs'), None),
                 handouts=(visit_graphviz_for('handouts'), None),
                 override=True)
