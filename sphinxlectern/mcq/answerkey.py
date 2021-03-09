"""mcq.answerkey

The setup function (at the bottom of this file) will do the following:

- Register configuration values:
  - mcq_build_answerkey: Set to True to build an answer key from any mcq nodes
    in a document. Defaults to False.
  - mcq_answerkey_file: Set the file name of the answer key. Defaults to "answerkey.json".
    The file will appear in your build folder (ours is usually named _build/)
- Register a callback on "doctree-resolved" called create_answerkey to traverse
  doctree and parse MCQ data into an AnswerKey.
- Register a callback on "mcq-answerkey-created" to build the answerkey file
  (this will only happen if mcq_build_answerkey is set to True)
"""

from typing import Optional, List, Dict, Union
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder as Builder
from . import mcqnodes

from dataclasses import dataclass, field, asdict
import json
from os import path

from docutils import nodes
from sphinx.util.osutil import os_path


@dataclass
class McqFeedback:
    is_correct: Union[bool, None] = None
    text: str = ""
    html: str = ""

    @classmethod
    def from_node(
        cls, node: mcqnodes.mcq_choice_feedback, builder: Builder
    ) -> "McqFeedback":
        """Extract data from a mcq_choice_feedback node."""

        return cls(
            is_correct=node.get("is_correct"),
            text=node.astext(),
            html=builder.render_partial(node.children[0])["fragment"],
        )


@dataclass
class McqChoice:
    text: str
    html: str
    feedback: McqFeedback = field(default_factory=McqFeedback)

    @classmethod
    def from_node(cls, node: mcqnodes.mcq_choice, builder: Builder) -> "McqChoice":
        """Extract data from a mcq_choice node."""

        # Find children of mcq_choice that aren't feedback.
        # FIXME: this is a bad idea. We should create separate node for value of
        # choice so we can separate it from feedback
        not_feedback = [
            child
            for child in node.children
            if type(child) is not mcqnodes.mcq_choice_feedback
        ]
        # Create a node so we can render not_feedback nodes
        choice_body = nodes.container("", classes=[])
        choice_body += not_feedback

        return cls(
            text=choice_body.astext(),
            html=builder.render_partial(choice_body)["fragment"],
        )


@dataclass
class McqQuestion:
    id: str
    text: str
    html: str
    answer: str
    show_feedback: bool = False
    numbered: bool = False
    choices: List[McqChoice] = field(default_factory=list)

    @classmethod
    def from_node(cls, node: mcqnodes.mcq, builder: Builder) -> "McqQuestion":
        """Extract data from an mcq node."""

        # The prompt of the question is stored in mcq_body
        body_index = node.first_child_matching_class(mcqnodes.mcq_body)
        question_body = node.children[body_index]

        return McqQuestion(
            id=node.get("ids", [""])[0],
            text=question_body.astext(),
            html=builder.render_partial(question_body)["fragment"],
            answer=node.get("answer"),
            show_feedback=node.get("show_feedback"),
            numbered=node.get("numbered"),
        )


class AnswerKey:
    def __init__(self, questions: Optional[List[McqQuestion]] = None) -> None:
        self.questions = questions or []

    @property
    def question_lookup(self) -> Dict[str, McqQuestion]:
        if not getattr(self, "_questions_lookup", None):
            self._questions_lookup = {
                question.id: question for question in self.questions if question.id
            }
        return self._questions_lookup

    @classmethod
    def from_doctree(cls, doctree: nodes.document, builder: Builder) -> "AnswerKey":
        """Create answer key from doctree."""

        # questions will be used to instantiate an AnswerKey
        questions = []
        for mcq in doctree.traverse(mcqnodes.mcq):
            question = McqQuestion.from_node(mcq, builder)

            # Populate question.choices from the list of mcq_choice nodes in mcq.
            # Each choice contains text of the answer choice as well as any feedback.
            choices_list = mcq.children[1]
            for choice in choices_list.children:
                choice_data = McqChoice.from_node(choice, builder)

                # Find feedback node and attach its data to choice_data
                fb_index = choice.first_child_matching_class(
                    mcqnodes.mcq_choice_feedback
                )
                fb_node = choice[fb_index]
                choice_data.feedback = McqFeedback.from_node(fb_node, builder)

                question.choices.append(choice_data)

            # Finished building question, so append to questions list
            questions.append(question)

        return cls(questions)

    def to_json(self) -> list:
        """Return jsonifiable list.

        We use the return value of this method in json.dumps to build the answerkey file
        (if mcq_build_answerkey is True).
        """

        return [asdict(question) for question in self.questions]

    def write_to_file(self, outpath: str):
        """Write answerkey to file."""

        answerkey_json = json.dumps(self.to_json(), indent=2)
        with open(outpath, "w") as f:
            f.write(answerkey_json)


def create_answerkey(app, doctree, docname) -> None:
    """Callback for doctree-resovled. Build an AnswerKey out of doctree.

    When done buidling answerkey, emit event mcq-answerkey-created.
    """

    answerkey = AnswerKey.from_doctree(doctree, app.builder)
    if answerkey.questions:
        app.emit("mcq-answerkey-created", answerkey, doctree)


def build_answerkey(app, answerkey: AnswerKey, _) -> None:
    """Callback for mcq-answerkey-created to build and write answerkey file.

    (But only if mcq_build_answerkey is True)
    """

    if not app.config.mcq_build_answerkey:
        return

    outpath = path.join(app.builder.outdir, os_path(app.config.mcq_answerkey_file))
    answerkey.write_to_file(outpath)


def setup(app: Sphinx):
    # By default, answer key goes in solution/answerkey.json
    app.add_config_value("mcq_build_answerkey", False, "env")
    app.add_config_value("mcq_answerkey_file", "answerkey.json", "env")

    app.connect("doctree-resolved", create_answerkey)
    app.connect("mcq-answerkey-created", build_answerkey)
