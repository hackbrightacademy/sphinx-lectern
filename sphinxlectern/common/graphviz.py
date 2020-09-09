from typing import List, Callable, Type, Union
from sphinx.ext.graphviz import Graphviz, GraphvizSimple
from sphinx.writers.html5 import HTML5Translator
from docutils.nodes import Node, SkipNode

from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
import sphinx.ext.graphviz as sphinx_graphviz


def attach_style_options(c: Type[Graphviz]) -> Type[Graphviz]:
    """Give Graphviz directive options to add 'style' HTML attribute.

    This will give you two options --- revealjs & handouts --- that will
    render a 'style' HTML attribute used to resize dot-rendered SVGs.

        .. digraph::
          :revealjs: height: 50%;
          :handouts: width: 100%;

    """

    c.option_spec.update(
        {"revealjs": directives.unchanged, "handouts": directives.unchanged}
    )

    def run(self) -> List[Node]:
        node = super(c, self).run()[0]
        node["revealjs"] = self.options.get("revealjs", "width: 100%;")
        node["handouts"] = self.options.get("handouts", "width: 100%;")

        return [node]

    c.run = run  # type: ignore

    return c


@attach_style_options
class LecternGraphviz(Graphviz):
    """Our Graphviz directive, which we'll use to monkey-patch Sphinx's."""


@attach_style_options
class LecternGraphvizSimple(GraphvizSimple):
    """Our GraphvizSimple directive, which we'll use to monkey-patch Sphinx's."""


def visit_graphviz_for(builder_name: str) -> Callable:
    """Return visit_graphviz function for given builder."""

    def visit_graphviz(self: HTML5Translator, node: sphinx_graphviz.graphviz) -> None:
        if builder_name in node:
            self.body.append(f'<div class="resizer" style="{node[builder_name]}">')
        else:
            self.body.append(f'<div class="resizer">')

        try:
            sphinx_graphviz.render_dot_html(self, node, node["code"], node["options"])
        except SkipNode:
            self.body.append("</div>")

        raise SkipNode

    return visit_graphviz


def setup(app):
    """Monkey-patch our augmented versions of default doctest directives."""

    sphinx_graphviz.Graphviz = LecternGraphviz
    sphinx_graphviz.GraphvizSimple = LecternGraphvizSimple
    sphinx_graphviz.setup(app)
    app.add_node(
        sphinx_graphviz.graphviz,
        html=(visit_graphviz_for("html"), None),
        revealjs=(visit_graphviz_for("revealjs"), None),
        handouts=(visit_graphviz_for("handouts"), None),
        override=True,
    )
