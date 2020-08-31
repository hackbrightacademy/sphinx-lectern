"""Newslide.

Use this to create a new slide. Content will resume on the new
slide.

Pass in an argument to give the new slide a title::

    .. newslide:: Title

If you prepend your title with a '+', the original title will be
prepended to the new slide's title::

    .. newslid:: *(cont.)

With no arguments, the new slide will have the same title as its
parent slide.

Contents:
    - newslide
    - Newslide
    - process_newslides
"""

from typing import List
from sphinx.application import Sphinx
from docutils import nodes
from ._slides import BaseSlide


class newslide(nodes.General, nodes.Element):
    """Newslide node."""


class Newslide(BaseSlide):
    """Newslide directive."""

    optional_arguments = 1
    final_argument_whitespace = True

    def run(self) -> List[nodes.Element]:
        local_title = self.arguments[0] if self.arguments else ""

        slide_node = newslide("", localtitle=local_title)
        self.attach_options(slide_node)

        # This directive is only used for post-processing after the
        # doctree has been resolved, so we should never have to call
        # self.add_name

        return [slide_node]


def process_newslides(app: Sphinx, doctree, fromdocname: str) -> None:
    """Process newslides after doctree is resolved."""

    while doctree.traverse(newslide):
        newslide_node = doctree.next_node(newslide)
        if app.builder.name != "revealjs":
            newslide_node.parent.remove(newslide_node)
            continue

        parent_section = newslide_node.parent

        # parent_section might have been created by a newslide_node.
        # If so, traverse until we find a "real" slide.
        check_section = parent_section
        while "localtitle" in check_section.attributes:
            i = check_section.parent.index(check_section)
            check_section = check_section.parent.children[i - 1]

        local_title = newslide_node.attributes["localtitle"].strip()
        title = check_section.children[0].astext().strip()
        if local_title and local_title.startswith("+"):
            title = f"{title} {local_title[1:]}"
        elif local_title:
            title = local_title

        new_section = nodes.section("")
        new_section.attributes = newslide_node.attributes
        doctree.set_id(new_section)

        new_section += nodes.title("", title)

        for next_node in parent_section[parent_section.index(newslide_node) + 1 :]:
            new_section.append(next_node.deepcopy())
            parent_section.remove(next_node)

        chapter = parent_section.parent
        chapter.insert(chapter.index(parent_section) + 1, new_section)
        parent_section.remove(newslide_node)


def setup(app: Sphinx) -> None:
    app.add_node(newslide)
    app.add_directive("newslide", Newslide)
    app.connect("doctree-resolved", process_newslides)
