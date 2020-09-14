"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""
import sys
import os

sys.path.append(os.path.abspath("./../../"))
sys.path.append(os.path.abspath("./"))

master_doc = "index"
extensions = ["docexample", "sphinxlectern", "sphinxlectern.mcq"]
project = "sphinx-lectern, a Sphinx extension by Hackbright Academy"

html_theme = handouts_theme = "docs"
pygments_style = "sphinx"
html_theme_options = {"show_backlink": False}
html_add_permalink = "#"