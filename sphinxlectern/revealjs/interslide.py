"""Interslide.

Use this directive to create interslides. These are slides that can
be used for intermissions, interjections, or transitions. They're
slides that can contain content but don't have their own title.

Also, they're not rendered in lecture handouts, so don't use
them to display critical information that should be included in the
lecture notes!

Contains:
    - interslide
    - Interslide
    - visit_interslide
    - depart_interslide
    - ignore_interslide
"""

from typing import List
from sphinx.application import Sphinx

from docutils import nodes
from ._slides import BaseSlide


class interslide(nodes.General, nodes.Element):
    """Interslide node."""


class Interslide(BaseSlide):
    """Interslide directive."""

    has_content = True

    def run(self) -> List[nodes.Node]:
        text = "\n".join(self.content)

        slide_node = interslide(text)
        self.attach_options(slide_node)

        self.add_name(slide_node)
        self.state.nested_parse(self.content, self.content_offset, slide_node)

        return [slide_node]


def visit_interslide(self, node: nodes.Node) -> None:
    """Create a new slide.

    If the parent slide is a normal slide (i.e. it is not a title or sub-title
    slide), close it.

    This function should only be registered with the revealjs builder.
    """

    if self.section_level > 2:
        self.body.append("</section>")

    self._new_section(node)


def depart_interslide(self, node: nodes.Node) -> None:
    """Only close the slide if we're a top-level interslide."""

    if self.section_level == 2:
        self.body.append("</section>")


def ignore_interslide(self, node: nodes.Node) -> None:
    raise nodes.SkipNode


def setup(app: Sphinx) -> None:
    app.add_node(
        interslide,
        html=(ignore_interslide, None),  # type: ignore
        handouts=(ignore_interslide, None),  # type: ignore
        revealjs=(visit_interslide, depart_interslide),
    )
    app.add_directive("interslide", Interslide)
