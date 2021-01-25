"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""

import os
import datetime
import subprocess
import sys
import imp
import logging

sys.path.append(os.path.abspath("./../../.."))

project = html_title = "Hackbright Engineering"
copyright = f"{datetime.datetime.now().year} Hackbright Academy"
version = release = ""
master_doc = "index"
templates_path = ["_templates"]

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.mathjax",
    # "matplotlib.sphinxext.plot_directive",
    "sphinxlectern",
]

exclude_patterns = [
    "_build",
    "skit.rst",
    "**/rubric",
    "**/skit",
    "**/*-demo",
    "meta",
    "**/*_",
    "**/env",
    "**/venv",
]

pygments_style = "sphinx"

html_context = {"backurl": "/"}
html_theme = handouts_theme = "handouts"
html_show_sourcelink = False
html_show_sphinx = False
html_use_index = False
html_domain_indices = False
html_scaled_image_link = False
html_copy_source = False
html_add_permalinks = ""
revealjs_theme = "revealjs"

hb_hostname = "fellowship.hackbrightacademy.com"

imgmath_image_format = "svg"
imgmath_add_tooltips = False
imgmath_font_size = 16
# pngmath_add_tooltips = False
# revealjs_imgmath_dvipng_args = ['-gamma', '1.5', '-D', '275']

graphviz_dot_args = [
    "-Gmargin=0.2",
    "-Nfontname=Helvetica",
    "-Gfontname=Helvetica",
    "-Efontname=Helvetica",
    "-Npenwidth=0.5",
]
graphviz_output_format = "svg"

plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ["png"]

# if "matplotlib.sphinxext.plot_directive" in extensions:
#     from matplotlib.sphinxext import plot_directive

#     plot_directive.TEMPLATE = """
# {{ source_code }}

# .. only:: html

#   .. image:: {{ build_dir }}/{{ images[0].basename }}.png
#     {% for option in options -%}
#       {{ option }}
#     {% endfor %}

#   {{ caption }}
# """
