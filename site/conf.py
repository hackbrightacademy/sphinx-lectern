"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""
import sys
import os
from pathlib import Path

sys.path.extend(
    [
        os.path.join(str(Path(__file__).resolve().parent), "../"),
        os.path.abspath(str(Path(__file__).resolve().parent)),
    ]
)

master_doc = "index"
extensions = ["docexample", "sphinxlectern"]
project = "sphinx-lectern, a Sphinx extension by Hackbright Academy"

html_theme = handouts_theme = "docs"
pygments_style = "sphinx"
html_theme_path = [os.path.abspath(Path(__file__).resolve().parent)]
html_theme_options = {"show_backlink": False}
html_add_permalink = "#"
