"""Incremental directive.

This will add a transition to its children so they appear one at a time.
``incremental`` is aliased to ``incr``, so you can use either name to refer to
this directive.

Contents:
    - Incremental
"""

from typing import List

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


class Incremental(Directive):
    """Incremental directive."""

    required_arguments = 1
    _valid_arguments = ('one', 'item', 'nest')
    has_content = True
    option_spec = {
        'class': directives.class_option
    }

    def validate_args(self) -> None:
        """Warn user if argument is an invalid option."""

        location = self.state_machine.get_source_and_line(self.lineno)
        if self.arguments[0] not in self._valid_arguments:
            logger.warning(
                f'{self.arguments[0]} must be one of {self._valid_arguments}',
                location=location
            )

    def assert_is_incrementable(self, node: nodes.Element) -> None:
        """Warn user if we can't apply transitions to this node."""

        location = self.state_machine.get_source_and_line(self.lineno)
        if not isinstance(node, nodes.Sequential):
            logger.warning(
                'contents of directive \'incremental\' must be a list or sequence',
                location=location
            )

    def increment_list_items(self, node: nodes.Sequential) -> None:
        """Add class 'fragment' to Sequential node's children."""

        for list_item in node.children[0].children:
            try:
                list_item['classes'] += ['fragment']
            except TypeError:
                continue

    def increment_nested_list_items(self, node: nodes.Sequential) -> None:
        """Add class 'fragment' to a Sequential node's descendants."""

        def traverse_condition(node: nodes.Node) -> bool:
            return (isinstance(node, nodes.list_item) or
                    isinstance(node, nodes.term) or
                    isinstance(node, nodes.definition))

        for list_item in node.traverse(traverse_condition):
            list_item['classes'] += ['fragment']

    @staticmethod
    def contain_definition_list_items(dl_node: nodes.definition_list) -> None:
        """Group definitions and terms in containers."""

        dl_children = []
        for def_list_item in dl_node.children:
            container = nodes.container()
            container.children.append(def_list_item)
            dl_children.append(container)

        dl_node.children = dl_children

    def run(self) -> List[nodes.Node]:
        self.validate_args()
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = nodes.container(text)
        self.state.nested_parse(self.content, self.content_offset, node)

        if self.arguments[0] == 'one':
            node['classes'] += self.options.get('class', [])
            node['classes'].append('fragment')
            return [node]
        else:
            self.assert_is_incrementable(node.children[0])

            # Since we're gonna discard the parent node, copy
            # classes set by the user onto the first child node
            node.children[0]['classes'] += self.options.get('class', [])

            if isinstance(node.children[0], nodes.definition_list):
                self.contain_definition_list_items(node.children[0])

            if self.arguments[0] == 'item':
                self.increment_list_items(node)
            elif self.arguments[0] == 'nest':
                self.increment_nested_list_items(node)

            return node.children


def setup(app: Sphinx) -> None:
    app.add_directive('incremental', Incremental)
    app.add_directive('incr', Incremental)