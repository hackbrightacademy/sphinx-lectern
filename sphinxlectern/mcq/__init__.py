"""sphinxlectern.mcq

Multiple-choice questions.

For examples, see tests/examples/text_mcq/index.rst.
"""

from typing import List, Union, Optional
from typing import cast
from sphinx.application import Sphinx

import json
import html
from sphinx.util.docutils import SphinxDirective
from sphinx.util.docfields import _is_single_paragraph
from sphinx.util import logging

from docutils import nodes
from docutils.parsers.rst import directives

from . import mcqnodes, answerkey, scantron

from .mcqnodes import (
    mcq,
    mcq_body,
    mcq_choices_list,
    mcq_choice,
    mcq_choice_feedback,
)
from .answerkey import AnswerKey

logger = logging.getLogger(__name__)


def _list_with_field_feedback(node: nodes.Node) -> Optional[nodes.field_list]:
    """Search node for a field list with a field named "feedback"."""

    for field in node.traverse(nodes.field):
        field_name = field.children[0]
        if field_name.astext().lower() == "feedback":
            return field.parent

    return None


def _transform_field_list(
    node: nodes.field_list,
) -> mcq_choice_feedback:
    """Turn field list into mcq_choice_feedback.

    Search field list for field named 'feedback' and turn its body into mcq_choice_feedback node.
    """

    for field in node.children:
        field_name, field_body = field.children

        if field_name.astext().strip().lower() == "feedback":
            # Collect the content, trying not to keep unnecessary paragraphs
            if _is_single_paragraph(field_body):
                paragraph = cast(nodes.paragraph, field_body[0])
                content = paragraph.children
            else:
                content = field_body.children

            break
    else:
        content = []

    return mcq_choice_feedback("", nodes.paragraph("", "", *content))


def _transform_enumerated_list(
    node: nodes.enumerated_list,
) -> mcq_choices_list:
    """Transform enumerated_list node into mcq_choices_list."""

    choices_node = mcq_choices_list("")
    choices_node += node.children
    choices_node.update_all_atts(node)
    # TODO: maybe do node.replace_self(choices_node) which will call
    # update_all_atts for me...?
    # just kidding, tit calls update_basic_atts, not all_atts

    return choices_node


def _transform_list_item(node: nodes.list_item) -> mcq_choice:
    """Transform list_item node to mcq_choice."""

    choice_node = mcq_choice("", *node.children)
    choice_node.update_all_atts(node)

    return choice_node


class Mcq(SphinxDirective):
    """Multiple choice question directive."""

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    node_class = mcq
    option_spec = {
        "class": directives.class_option,
        "answer": directives.unchanged,
        "name": directives.unchanged,
        "numbered": directives.flag,
        "show_feedback": directives.flag,
    }
    choice_indexes = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def _init(self):
        if not getattr(self.env, "_mcq_count", None):
            self.env._mcq_count = 0
        self.env._mcq_count += 1

        # Create name if it doesn't exist
        if not self.options.get("name"):
            self.options["name"] = f"mcq-{self.env._mcq_count}"

        # Parse flags in self.options to True/False
        for opt_name, opt_type in self.option_spec.items():
            if opt_type is directives.flag:
                self.options[opt_name] = opt_name in self.options

        # 'numbered' and 'show_feedback' options should become classes
        classes = self.options.setdefault("classes", [])
        if self.options.get("numbered"):
            classes.append("numbered")
        if self.options.get("show_feedback"):
            classes.append("show-feedback")

    def create_choices_list(self, node: mcq) -> mcq_choices_list:
        """Create list of answer choices."""

        # Find the first enumerated list with enumtype 'upperalpha'
        try:
            choices_enumlist = next(
                iter(
                    node.traverse(
                        lambda n: isinstance(n, nodes.enumerated_list)
                        and n.get("enumtype") == "upperalpha"
                    )
                )
            )
        except StopIteration:
            logger.warning(
                f"MCQ '{self.arguments[0]}' around line {self.lineno} does not have a list of answer choices."
            )
            return

        choices_list = _transform_enumerated_list(choices_enumlist)
        self.add_name(choices_list)

        self._replace_li_with_mcq_choice(choices_list)
        choices_enumlist.replace_self(choices_list)

        return choices_list

    def _replace_li_with_mcq_choice(
        self, choices_list: mcq_choices_list
    ) -> None:
        """ "Replace list_item in mcq_choices_list with mcq_choice nodes."""

        gen_index = iter(self.choice_indexes)
        for list_item in choices_list.children:
            choice_node = _transform_list_item(list_item)
            choice_node["mcq_id"] = f"{self.options.get('name')}"
            choice_node["value"] = next(gen_index)

            # Collect feedback from choice first. We use field_list markup for
            # annotating feedback.
            feedback_field_list = _list_with_field_feedback(list_item)
            if feedback_field_list:
                feedback_node = _transform_field_list(feedback_field_list)

                # Since we don't actually want to render feedback as HTML,
                # remove the field list.
                choice_node.remove(feedback_field_list)
            else:
                feedback_node = mcq_choice_feedback(
                    "", nodes.paragraph("", "")
                )

            feedback_node["is_correct"] = choice_node[
                "value"
            ] == self.options.get("answer")
            choice_node += feedback_node

            # Now we can replace list_item
            list_item.replace_self(choice_node)

            self.add_name(choice_node)

    def run(self) -> List[mcq]:
        """Build an mcq node.

        Contents of mcq node/hierarchy should be:

        - mcq_body
          - children
        - mcq_choices_list
          - mcq_choice
            - children
            - mcq_feedback
        """

        self._init()

        node = mcq("\n".join(self.content), **self.options)
        self.add_name(node)

        # First argument becomes the first paragraph of the question
        textnodes, _ = self.state.inline_text(self.arguments[0], self.lineno)
        first_paragraph = nodes.paragraph(self.arguments[0], "", *textnodes)

        body = mcq_body("\n".join(self.content))
        self.state.nested_parse(self.content, self.content_offset, body)
        choices_list = self.create_choices_list(body)
        if choices_list:
            body.remove(choices_list)

        # Rearrange body.children so it starts with first_paragraph followed
        # by the rest of body.children. Then we can add body to node's children.
        body.children = [first_paragraph, *body.children]
        node += body
        if choices_list:
            node += choices_list

        return [node]


def add_feedback_to_choices(
    app, answerkey: AnswerKey, doctree: nodes.document
) -> None:
    """For questions where show_feedback is True, store feedback in choice
    nodes.

        Since this relies on answerkey data, you should register this function as a callback on the event "mcq-answerkey-created" ("mcq-answerkey-created" is a custom event, not a builtin one).
    """

    for node in doctree.traverse(mcq):
        if node.get("show_feedback"):
            mcq_id = node.get("ids")[0]

            choices_list = node.children[-1]
            choices_data = answerkey.question_lookup[mcq_id].choices
            for choice, choice_data in zip(choices_list, choices_data):
                choice["data_attrs"] = {
                    "data-is-correct": choice_data.feedback.is_correct,
                    "data-feedback": json.dumps(
                        {"html": choice_data.feedback.html}
                    ),
                }


def setup(app: Sphinx):
    app.add_event("mcq-answerkey-created")
    app.connect("mcq-answerkey-created", add_feedback_to_choices)

    app.add_directive("mcq", Mcq)

    answerkey.setup(app)
    mcqnodes.setup(app)
    scantron.setup(app)
