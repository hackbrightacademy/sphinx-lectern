from docutils import nodes

from sphinx.writers.html5 import HTML5Translator as HTMLTranslator


class HTML5Translator(HTMLTranslator):
    def visit_section(self, node: nodes.Element) -> None:
        self.section_level += 1
        self.body.append(self.starttag(node, "section", CLASS="section"))

    def depart_section(self, node: nodes.Element) -> None:
        self.section_level -= 1
        self.body.append("</section>\n")
