"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""
import sys
import os

sys.path.append(os.path.abspath('./../../..'))

master_doc = 'index'
extensions = [
    'sphinxlectern'
]

revealjs_theme = 'revealjs'
pygments_style = 'sphinx'
