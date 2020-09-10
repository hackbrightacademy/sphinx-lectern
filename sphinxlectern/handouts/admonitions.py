"""Monkeypatch default admonition directives so they all require titles."""

from typing import List, Optional, Callable, Type
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx


class BaseAdmonition(Directive):
    final_argument_whitespace = True
    option_spec = {"class": directives.class_option, "name": directives.unchanged}
    has_content = True
    required_arguments = 1

    node_class: Optional[Type[nodes.Node]] = None

    def get_title(self) -> str:
        """By default, this returns the first, required argument.

        Override to set a custom title.
        """

        return self.arguments[0]

    def run(self) -> List[nodes.Node]:
        self.assert_has_content()
        text = "\n".join(self.content)

        admonition_node = self.node_class(text, **self.options)  # type: ignore
        admonition_node["classes"] += self.options.get("class", [])

        title_text = self.get_title()
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        title = nodes.title(title_text, "", *textnodes)
        title.source, title.line = self.state_machine.get_source_and_line(self.lineno)

        admonition_node += title

        self.add_name(admonition_node)

        body = nodes.container(text)
        body["classes"] += ["admonition-body"]
        self.state.nested_parse(self.content, self.content_offset, body)
        admonition_node += body
        admonition_node += messages

        return [admonition_node]


class Admonition(BaseAdmonition):
    node_class = nodes.admonition


class Hint(BaseAdmonition):
    node_class = nodes.hint


class Note(BaseAdmonition):
    node_class = nodes.note


class Warning(BaseAdmonition):
    node_class = nodes.warning


class knowledge_check(nodes.Admonition, nodes.Element):
    pass


def visit_knowledge_check(self, node: knowledge_check):
    self.visit_admonition(node, "knowledge_check")


def depart_knowledge_check(self, node: knowledge_check):
    self.depart_admonition(node)


class KnowledgeCheck(BaseAdmonition):
    node_class = knowledge_check
    required_arguments = 0

    def get_title(self) -> str:
        return ""


def setup(app: Sphinx) -> None:
    app.add_directive("admonition", Admonition, override=True)
    app.add_directive("hint", Hint, override=True)
    app.add_directive("note", Note, override=True)
    app.add_directive("warning", Warning, override=True)
    app.add_directive("knowledge-check", KnowledgeCheck)
    app.add_node(
        knowledge_check, handouts=(visit_knowledge_check, depart_knowledge_check)
    )
