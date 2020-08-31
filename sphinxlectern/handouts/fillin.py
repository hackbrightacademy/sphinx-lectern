"""Extension to render text as input[type="text"] in handouts.

Usage:

  API is short for :fillin:`application programming interface`
"""

from typing import List
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive


class fillin(nodes.Part, nodes.TextElement):
    role_name = "fillin"
    role_markup = f":{role_name}:``"


class FillIn(Directive):
    has_content = True

    def run(self) -> List[nodes.Node]:
        self.assert_has_content()

        text = "\n".join(self.content)

        node = fillin(text, text)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_fillin(self, node: fillin) -> None:
    # TODO: Comment me, wtf is this
    self.body.append(
        f'<input type="text" id="fillin-{node.index}" class="fillin" style="width: {(len(node.rawsource) - len(node.role_markup)) / 2 + 2}em;">'
    )


def visit_fillin_reveal(self, node: fillin) -> None:
    return


def depart_fillin(self, node: fillin) -> None:
    self.body.append("</input>")


def depart_fillin_reveal(self, node: fillin) -> None:
    # TODO: Explain yourself, you monster
    # for slides, emit text (but dont emit the shit that will
    # turn this thing into a fill-in-the-blank doo-dad)
    return


def process_fillin(app: Sphinx, doctree: nodes.document, fromdocname: str) -> None:
    if app.builder.name == "handouts":
        count = 0
        for node in doctree.traverse(fillin):
            node.children = []  # Remove all text nodes

            node.index = count
            count += 1


def setup(app: Sphinx) -> None:
    app.add_node(
        fillin,
        html=(visit_fillin, depart_fillin),
        handouts=(visit_fillin, depart_fillin),
        revealjs=(visit_fillin_reveal, depart_fillin_reveal),
    )
    app.add_generic_role("fillin", fillin)
    app.connect("doctree-resolved", process_fillin)
