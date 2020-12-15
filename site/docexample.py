from typing import List
from sphinx.testing.path import path
from sphinx.application import Sphinx

from pathlib import Path
from docutils.parsers.rst import Directive, directives
from docutils.nodes import General, Element, container, document, literal_block


class docexample(container):
    pass


class docexample_render(container):
    pass


class docexample_source(container):
    pass


def visit_docexample(self, node: docexample):
    self.body.append('<div class="docexample">')


def depart_docexample(self, node: docexample):
    self.body.append("</div>")


class DocExample(Directive):
    """Code example for docs website."""

    has_content = True
    option_spec = {"builder": directives.unchanged}

    # TODO: if builder is revealjs, take code inside and turn it into another
    # document, build that document with Sphinx
    def run(self):
        node = docexample("\n".join(self.content), **self.options)
        self.add_name(node)

        render_container = docexample_render(
            "\n".join(self.content), classes=["docexample-render"]
        )
        self.state.nested_parse(self.content, self.content_offset, render_container)
        node += render_container

        src_container = docexample_source("", classes=["docexample-src"])
        src_code_node = literal_block(
            "\n".join(self.content), "\n".join(self.content), language="rst"
        )
        src_container += src_code_node
        node += src_container

        return [node]


def setup(app: Sphinx):
    app.add_directive("docexample", DocExample)
    app.add_node(docexample, handouts=(visit_docexample, depart_docexample))
    app.add_html_theme(
        "docs",
        path(__file__).parent.abspath() / "theme",
    )
