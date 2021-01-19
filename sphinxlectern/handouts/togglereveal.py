"""A directive that hides its contents in a <details> tag.

We use the default behavior of the <details> tag --- children of the
tag are hidden until you click to expand them.
"""

from typing import List
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class togglereveal(nodes.General, nodes.Element):
    pass


class ToggleReveal(Directive):
    final_argument_whitespace = True
    has_content = True

    option_spec = {"class": directives.class_option}

    def run(self) -> List[nodes.Node]:
        self.assert_has_content()
        text = "\n".join(self.content)

        node = togglereveal(text)
        node["classes"] += self.options.get("class", [])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_togglereveal(self, node: nodes.Node) -> None:
    classes = " ".join(node.get("classes", []))
    self.body.append(f'<div class="togglereveal {classes}">')
    self.body.append('<details class="admonition-body">')
    self.body.append("<summary></summary>")


def depart_togglereveal(self, node: nodes.Node) -> None:
    self.body.append("</details></div>")


def ignore_togglereveal(self, node: nodes.Node) -> None:
    raise nodes.SkipNode


def setup(app: Sphinx) -> None:
    app.add_node(
        togglereveal,
        html=(visit_togglereveal, depart_togglereveal),
        handouts=(visit_togglereveal, depart_togglereveal),
        revealjs=(ignore_togglereveal, None),  # type: ignore
    )
    app.add_directive("togglereveal", ToggleReveal)
    app.add_directive("toggle", ToggleReveal)
