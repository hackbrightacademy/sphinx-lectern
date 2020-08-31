"""sphinxlectern.common.pdf

Embed PDF files into a document.

This relies on https://www.npmjs.com/package/pdfobject
"""

from typing import List
from docutils.node import Node

from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from os import path
from pathlib import PurePath
from sphinx.util.fileutil import copy_asset


class pdfobject(nodes.General, nodes.Element):
    pass


class PdfObject(Directive):
    final_argument_whitespace = False
    has_content = False
    required_arguments = 1

    @staticmethod
    def assert_is_pdf(path: str) -> None:
        """Assert that path is a PDF."""

        # TODO: Use pathlib to parse path & check suffix

    def run(self) -> List[Node]:
        pdf_path = self.arguments[0]

        try:
            self.assert_is_pdf(pdf_path)
        except:
            # TODO: Log that path isn't valid and return node
            # with ref to file
            pass

        node = pdfobject("")
        node["pdf_file"] = pdf_path

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def visit_pdfobject(self, node: Node) -> None:
    pdf_file = node["pdf_file"]
    copy_asset(
        path.join(self.builder.srcdir, pdf_file),
        path.join(self.builder.outdir, "_static"),
    )

    self.body.append(
        f'<div id="pdf-{PurePath(pdf_file).stem}" class="pdfobject" style="height: 400px;"></div>'
    )
    self.body.append(
        f'<script>PDFObject.embed("_static/{pdf_file}", "#pdf-{PurePath(pdf_file).stem}");</script>'
    )


def depart_pdfobject(self, node: Node) -> None:
    return


def setup(app: Sphinx) -> None:
    app.add_node(
        pdfobject,
        html=(visit_pdfobject, depart_pdfobject),
        handouts=(visit_pdfobject, depart_pdfobject),
        revealjs=(visit_pdfobject, depart_pdfobject),
    )
    app.add_directive("pdf", PdfObject)
    app.add_directive("pdfobject", PdfObject)
