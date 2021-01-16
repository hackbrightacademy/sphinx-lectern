"""mcq.scantron

The setup function (at the bottom of this file) adds a bunch of stuff that'll
build a scantron out of any numbered MCQs in a doctree.

A scantron is really just a plaintext file that looks like this:

    1)
    2)
    3)

Then, students can fill it out like this:

    1) A
    2) A
    3) B

To enable scantrons, set mcq_build_scantron to True in your Sphinx configuration
file (usually called config.py). By default, this will create a scantron in scantron.txt.
If you want a different filename, set a value for mcq_scantron_file in your
configuration file.
"""

from .answerkey import AnswerKey
from sphinx.application import Sphinx

from os import path
from sphinx.util.osutil import os_path


def build_scantron(app: Sphinx, answerkey: AnswerKey, _) -> None:
    """Generate scantron with entry for each numbered question."""

    if not app.config.mcq_build_scantron:  # type: ignore
        return

    # Generate numbers for all the questions where numbered = True
    question_range = range(
        1, len([quest for quest in answerkey.questions if quest.numbered]) + 1
    )

    scantron_filename = app.config.mcq_scantron_file  # type: ignore
    outpath = path.join(app.builder.outdir, os_path(scantron_filename))
    with open(outpath, "w") as f:
        f.write("\n".join([f"{num}) " for num in question_range]))


def setup(app: Sphinx):
    app.add_config_value("mcq_build_scantron", False, "env")
    app.add_config_value("mcq_scantron_file", "scantron.txt", "env")

    app.connect("mcq-answerkey-created", build_scantron)