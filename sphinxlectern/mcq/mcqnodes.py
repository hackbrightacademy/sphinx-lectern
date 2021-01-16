"""mcq.nodes"""

from typing import Optional
from sphinx.application import Sphinx

from docutils import nodes


class UsesNameAsClass:
    """A mixin that adds self.classname to the node's list of classes."""

    classname: Optional[str] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.classname:
            self["classes"] += [self.classname]


class mcq(UsesNameAsClass, nodes.container):
    """Multiple choice question node."""

    classname = "mcq"


class mcq_body(UsesNameAsClass, nodes.container):
    """The prompt and body text of a multiple choice question."""

    classname = "mcq-body"


class mcq_choices_list(UsesNameAsClass, nodes.enumerated_list):
    """List of answer choices."""

    classname = "mcq-choices"


class mcq_choice(nodes.list_item):
    """Potential answer for a multiple choice question."""


class mcq_choice_feedback(nodes.container):
    """Feedback for a choice.

    This should contain information on why an answer choice is right or wrong.
    """


def visit_mcq(self, node: mcq):
    self.body.append(self.starttag(node, "div"))


def depart_mcq(self, node: mcq):
    if node.get("show_feedback"):
        self.body.append('<button class="mcq-answer-checker">Check Answer</button>')
        self.body.append('<p class="mcq-alert"></p>')

    self.body.append("</div>")


def visit_mcq_choices_list(self, node: mcq_choices_list):
    self.visit_enumerated_list(node)


def depart_mcq_choices_list(self, node: mcq_choices_list):
    self.depart_enumerated_list(node)


def visit_mcq_choice(self, node: mcq_choice):
    self.body.append(f'<div class="mcq-answer-group">')

    if node.parent.parent.get("show_feedback"):
        input_id = nodes.make_id(f"{node.get('mcq_id')}-input")
        self.body.append(
            f'<input id="{input_id}" type="radio" name="{node.get("mcq_id")}" value="{node.get("value")}" />'
        )
        self.body.append(f'<label for="{input_id}">')

    self.body.append(self.starttag(node, "li", **node.get("data_attrs", {})))


def depart_mcq_choice(self, node: mcq_choice):
    self.body.append("</li>")

    if node.get("should_have_feedback"):
        self.body.append("</label>")
    self.body.append("</div>")


def visit_mcq_choice_feedback(self, node: mcq_choice_feedback):
    """Most of the time, we'll want to skip rendering this node.

    ...since, you know, it contains the correct answer and all x)
    """

    raise nodes.SkipNode


def setup(app: Sphinx):
    app.add_node(
        mcq,
        handouts=(visit_mcq, depart_mcq),
    )
    app.add_node(
        mcq_choices_list,
        handouts=(visit_mcq_choices_list, depart_mcq_choices_list),
    )
    app.add_node(
        mcq_choice,
        handouts=(visit_mcq_choice, depart_mcq_choice),
    )
    app.add_node(
        mcq_choice_feedback,
        handouts=(visit_mcq_choice_feedback, None),
    )