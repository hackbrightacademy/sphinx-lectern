"""Sphinx writer for slides."""

from typing import Dict, Any, Tuple
from sphinx.application import Sphinx
from docutils import nodes

from os import path
from pathlib import PurePath

from ._no_additional_pages import DontBuildAdditionalPages
from ._html5 import HTML5Translator

IMG_EXTENSIONS = ["jpg", "png", "gif", "svg"]


def get_attrs_as_html(node_attrs: Dict[str, Any]):
    """Convert docutil node attributes to HTML data- attributes."""

    basic_attrs = set(nodes.section.basic_attributes)

    html_attrs = {}
    for attr, val in node_attrs.items():
        if attr not in basic_attrs and type(val) is str:
            attr_name = f"data-{attr}" if attr != "class" else attr
            html_attrs[attr_name] = val
    return html_attrs


class RevealJSTranslator(HTML5Translator):
    """Translator for writing RevealJS slides."""

    permalink_text = False
    _dl_fragment = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.builder.add_permalinks = False

    def _add_path_to_builder(self, name: str, path: str) -> None:
        """Add path to a resource to builder."""

        parsed_path = PurePath(path.lower())
        if parsed_path.suffix in [f".{ext}" for ext in IMG_EXTENSIONS]:
            self.builder.images[name] = parsed_path.name

    def _new_section(self, node: nodes.Node) -> None:
        """Add a new section.

        In RevealJS, a new section is a new slide.
        """

        html_attrs = get_attrs_as_html(node.attributes)

        if "data-background" in html_attrs:
            bg_name = node.attributes["background"]
            self._add_path_to_builder(bg_name, html_attrs["data-background"])
            if bg_name in self.builder.images:
                html_attrs["data-background"] = path.join(
                    self.builder.imagedir, self.builder.images[bg_name]
                )

        attrs = " ".join([f'{attr}="{val}"' for attr, val in html_attrs.items()])
        self.body.append(f"<section {attrs}>")

    def visit_section(self, node: nodes.Node) -> None:
        """Only add a new section for 2nd- or 3rd-level sections."""

        self.section_level += 1

        if self.section_level in [2, 3]:
            self._new_section(node)

    def depart_section(self, node: nodes.Node) -> None:
        self.section_level -= 1

        if self.section_level in [1, 2]:
            self.body.append("</section>")

    def visit_title(self, node: nodes.Node) -> None:
        if self.section_level == 1:
            raise nodes.SkipNode

        if self.section_level == 2:
            self.body.append("<section>")

        super().visit_title(node)

    def depart_title(self, node: nodes.Node) -> None:
        super().depart_title(node)

        if self.section_level == 2:
            self.body.append("</section>")

    def visit_admonition(self, *args):
        raise nodes.SkipNode

    def visit_sidebar(self, node: nodes.Node) -> None:
        raise nodes.SkipNode

    def visit_topic(self, node: nodes.Node) -> None:
        raise nodes.SkipNode


class RevealJSBuilder(DontBuildAdditionalPages):
    """Builder for making RevealJS using Sphinx."""

    name = "revealjs"
    default_translator_class = RevealJSTranslator

    def get_theme_config(self) -> Tuple[str, Dict]:
        return self.config.revealjs_theme, self.config.html_theme_options


def setup(app: Sphinx) -> None:
    app.add_builder(RevealJSBuilder)
    app.set_translator("revealjs", RevealJSTranslator)
    app.add_config_value("revealjs_theme", "revealjs", "env")
    app.add_config_value("revealjs_imgmath_dvipng_args", [], "env")
