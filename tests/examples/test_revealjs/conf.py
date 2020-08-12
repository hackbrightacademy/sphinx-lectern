"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""
import sys
import os

sys.path.append(os.path.abspath('./../../..'))

master_doc = 'index'
templates_path = ['_templates']
html_theme_path = [os.path.abspath('./../../../themes')]

extensions = [
    'sphinxbootcamp'
]

revealjs_theme = 'revealjs'
# exclude_patterns = ['_build',
#                     'skit.rst',
#                     '**/rubric',
#                     '**/skit',
#                     '**/*-demo',
#                     'meta',
#                     '**/*_',
#                     '**/env',
#                     '**/venv']

# pygments_style = 'sphinx'

# rst_epilog = symbols + python_substitutions + text_editor_substitutions

# html_context = {'backurl': '/'}
# html_theme = handouts_theme = 'handouts'
# html_show_sourcelink = False
# html_show_sphinx = False
# html_use_index = False
# html_domain_indices = False
# html_scaled_image_link = False
# html_copy_source = False
# html_add_permalinks = ""
# revealjs_theme = 'revealjs'

# hb_hostname = 'fellowship.hackbrightacademy.com'
