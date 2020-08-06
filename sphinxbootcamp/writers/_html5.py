from docutils import nodes

from sphinx.writers.html5 import HTML5Translator as HTMLTranslator


class HTML5Translator(HTMLTranslator):
    def visit_section(self, node: nodes.Element) -> None:
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'section', CLASS='section'))

    def depart_section(self, node: nodes.Element) -> None:
        self.section_level -= 1
        self.body.append('</section>\n')

    def visit_reference(self, node: nodes.Element) -> None:
        # This is copied from sphinx.writers.html5.HTML5Translator
        atts = {'class': 'reference'}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'

        if 'refuri' in node:
            atts['href'] = node['refuri'] or '#'
            if (self.settings.cloak_email_addresses and
                    atts['href'].startswith('mailto')):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
        else:
            assert 'refid' in node, \
                   'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']

        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'

        if 'reftitle' in node:
            atts['title'] = node['reftitle']

        if 'target' in node:
            atts['target'] = node['target']
            atts['rel'] = 'noreferrer noopener'  # Added this line

        self.body.append(self.starttag(node, 'a', '', **atts))
