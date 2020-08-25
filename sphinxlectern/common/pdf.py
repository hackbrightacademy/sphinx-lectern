from typing import List
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

    def run(self) -> List[nodes.Node]:
        node = pdfobject('')

        node['pdf_file'] = self.arguments[0]

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def visit_pdfobject(self, node: nodes.Node) -> None:
    pdf_file = node['pdf_file']
    copy_asset(path.join(self.builder.srcdir, pdf_file),
               path.join(self.builder.outdir, '_static'))

    self.body.append(f'<div id="pdf-{PurePath(pdf_file).stem}" class="pdfobject" style="height: 400px;"></div>')
    self.body.append(f'<script>PDFObject.embed("_static/{pdf_file}", "#pdf-{PurePath(pdf_file).stem}");</script>')


def depart_pdfobject(self, node: nodes.Node) -> None:
    return


def setup(app: Sphinx) -> None:
    app.add_node(pdfobject,
                 html=(visit_pdfobject, depart_pdfobject),
                 handouts=(visit_pdfobject, depart_pdfobject),
                 revealjs=(visit_pdfobject, depart_pdfobject),)
    app.add_directive('pdf', PdfObject)
    app.add_directive('pdfobject', PdfObject)