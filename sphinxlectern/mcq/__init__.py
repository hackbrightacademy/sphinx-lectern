"""sphinxlectern.mcq

Multiple-choice questions.

Example:

  .. mcq:: The differences between natural and formal languages include:
    :answer: B

    A. Natural languages can be parsed while formal languages cannot

       :feedback: Actually both languages can be parsed (determining the structure of the sentence),
       but formal languages can be parsed more easily in software.

    B. Ambiguity, redundancy, and literalness

       :feedback: All of these can be resent in natural languages, but cannot exist in formal languages

    C. There are no differences between natural and formal languages

       :feedback: There are several differences between the two but they are also similar

    D. Tokens, structure, syntax, and semantics

       :feedback: These are the similarities between the two
"""

from typing import List, Union, Optional
from docutils.nodes import Node
from sphinx.application import Sphinx

from docutils.parsers.rst import Directive, directives
from docutils import nodes
from docutils.nodes import General, Element
import json
import html


class mcq(General, Element):
    """Multiple choice question node."""


class mcq_choice(General, Element):
    """Potential answer for a multiple choice question."""

    def __init__(self, rawsource: str = "", value: str = "", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self.value = value
        self["names"] += value


class Mcq(Directive):
    """Multiple choice question directive."""

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    node_class = mcq
    option_spec = {"class": directives.class_option, "answer": directives.unchanged}
    answer_choices = list("abcdefghijklmnop")

    @staticmethod
    def find_feedback_field_body(
        node: nodes.field_list,
    ) -> Union[None, List[nodes.paragraph]]:
        for field in node.children:
            field_name, field_body = field.children
            if field_name.astext() == "feedback":
                return field_body.children[0].astext().replace("\n", " ")
        return None

    def collect_feedback(self, node: mcq):
        """Collect feedback for each choice (if it exists)."""

        node["feedback"] = {}

        counter = 0
        for l_item in node.traverse(nodes.list_item):
            if fieldlist := l_item.children[
                l_item.first_child_matching_class(nodes.field_list)
            ]:
                field_body_text = self.find_feedback_field_body(fieldlist)
                node["feedback"][self.answer_choices[counter]] = field_body_text

                # Remove this field list because we don't need it anymore
                l_item.remove(fieldlist)

            counter += 1

    def wrap_choices(self, node: mcq):
        counter = 0
        for l_item in node.traverse(nodes.list_item):
            mcq_choice_node = mcq_choice(
                "",
                self.answer_choices[counter],
                *l_item.children,
                mcq=node,
                **l_item.attributes,
            )
            l_item.replace_self(mcq_choice_node)

            counter += 1

    def run(self) -> List[mcq]:
        node = mcq("\n".join(self.content), **self.options)
        node["answer"] = self.options.get("answer", "")

        textnodes, _ = self.state.inline_text(self.arguments[0], self.lineno)
        node += nodes.paragraph(self.arguments[0], "", *textnodes)

        self.add_name(node)

        body = nodes.container("\n".join(self.content))
        self.state.nested_parse(self.content, self.content_offset, body)
        node += body

        self.collect_feedback(node)
        self.wrap_choices(node)

        return [node]


def visit_mcq(self, node: mcq):
    """Visit mcq."""

    if getattr(self, "_mcq_count", None) is None:
        self._mcq_count = 0

    self._mcq_count += 1

    mcq_id = f"mcq-{self._mcq_count}"
    ans = node["answer"].lower()
    feedback = html.escape(json.dumps(node["feedback"]), quote=True)

    self.body.append(
        f'<div class="mcq" data-id="{mcq_id}" data-ans="{ans}" data-feedback="{feedback}">'
    )


def depart_mcq(self, node: mcq):
    """Depart mcq."""

    self.body.append('<button class="mcq-answer-checker">Check Answer</button>')
    self.body.append('<p class="mcq-alert"></p>')
    self.body.append("</div>")


def visit_mcq_choice(self, node: mcq_choice):
    """Visit mcq_choice."""

    mcq_id = f"mcq-{self._mcq_count}"
    input_id = f"{mcq_id}-{node.value}"

    self.body.append(f'<div class="mcq-answer-group">')
    self.body.append(
        f'<input id="{input_id}" type="radio" name="{mcq_id}" value="{node.value}" />'
    )
    self.body.append(f'<label for="{input_id}">')
    self.body.append("<li>")


def depart_mcq_choice(self, node: mcq_choice):
    self.body.append("</li>")
    self.body.append("</label>")
    self.body.append("</div>")


def setup(app: Sphinx):
    app.add_node(mcq, handouts=(visit_mcq, depart_mcq))
    app.add_node(mcq_choice, handouts=(visit_mcq_choice, depart_mcq_choice))
    app.add_directive("mcq", Mcq)
