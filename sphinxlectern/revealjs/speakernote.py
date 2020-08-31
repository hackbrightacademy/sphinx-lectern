from typing import List
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive


class speakernote(nodes.General, nodes.Element):
    pass


class Speakernote(Directive):
    has_content = True

    def run(self) -> List[nodes.Node]:
        self.assert_has_content()
        node = speakernote("\n".join(self.content))
        node["classes"] += ["notes"]
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_speakernote(self, node: nodes.Node) -> None:
    classes = " ".join(node["classes"])
    self.body.append(f'<aside class="{classes}">')


def depart_speakernote(self, node: nodes.Node) -> None:
    self.body.append("</aside>")


def ignore_speakernote(self, node: nodes.Node) -> None:
    raise nodes.SkipNode


def setup(app: Sphinx) -> None:
    app.add_node(
        speakernote,
        html=(ignore_speakernote, None),
        handouts=(ignore_speakernote, None),
        revealjs=(visit_speakernote, depart_speakernote),
    )
    app.add_directive("speaker", Speakernote)
