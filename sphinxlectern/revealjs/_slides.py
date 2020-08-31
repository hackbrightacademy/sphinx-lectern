"""Common, slides-related stuff.

This is where we put shared functionality for slides.
"""

from docutils.nodes import Element
from docutils.parsers.rst import Directive, directives


class BaseSlide(Directive):
    """Base for slide-related directives."""

    option_spec = {
        "class": directives.class_option,
        "background": directives.unchanged,
        # The choices below are all from Revealjs.
        # See https://revealjs.com/transitions/
        "transition": lambda arg: directives.choice(
            arg, ("none", "fade", "slide", "convex", "concave", "zoom")
        ),
        "transition-speed": lambda arg: directives.choice(
            arg, ("default", "fast", "slow")
        ),
    }

    def attach_options(self, node: Element) -> None:
        node["background"] = self.options.get("background")
        node["transition"] = self.options.get("transition")
        node["transition_speed"] = self.options.get("transition-speed")
        node["classes"] += self.options.get("class", [])
