"""Utilities written in RST syntax (and not Python)

This is where we define roles for colors, substitutions, etc.

Basically, anything that should go in the rst_prolog should go here.
"""

from sphinx.application import Sphinx

COLORS = """
.. role:: red
.. role:: green
.. role:: orange
.. role:: tan
.. role:: blue
.. role:: purple
.. role:: yellow
.. role:: cmd
.. role:: white
.. role:: gray
.. role:: comment
.. role:: gone
.. role:: inv-red
.. role:: text-heavy
"""

REVEAL_BR = """
.. role:: raw-revealjs(raw)
  :format: html
.. |reveal-br| replace:: :raw-revealjs:`<br>`
"""

SYMBOLS = """
.. |nbsp| unicode:: U+000A0 .. NONBREAKING SPACE
.. |rarr| unicode:: U+02192 .. →
.. |larr| unicode:: U+02190 .. ←
.. |uarr| unicode:: U+02191 .. ↑
.. |darr| unicode:: U+02193 .. ↓
.. |lrarr| unicode:: U+02194 .. ↔
.. |plus| unicode:: U+0002B .. +
.. |times| unicode:: U+000D7 .. ×
.. |check| unicode:: U+02713 .. ✓
.. |approx| unicode:: U+02248 .. ≈
.. |sub2| unicode:: U+02082 .. SUBSCRIPT 2
.. |super2| unicode:: U+000B2 .. SUPERSCRIPT 2
"""

PYTHON_SUBSTITUTIONS = """
.. |py| replace:: python3
.. |pyname| replace:: Python 3
.. |pyi| replace:: `python3`
.. |pycmd| replace:: `python3`:cmd:

.. |ipy| replace:: ipython3
.. |ipyi| replace:: `ipython3`
.. |ipycmd| replace:: `ipython3`:cmd:

.. |pip|       replace:: pip3
.. |pipi|      replace:: `pip3`
.. |pipcmd|    replace:: `pip3`:cmd:

.. |venv|      replace:: virtualenv
.. |venvi|     replace:: `virtualenv`
.. |venvcmd|   replace:: `virtualenv`:cmd:
"""

EDITOR_SUBSTITUTIONS = """
.. |editor|    replace:: subl
.. |editori|   replace:: `subl`
.. |editcmd|   replace:: `subl`:cmd:
.. |editorname|  replace:: Sublime Text
"""


def add_rst_prolog(app, config):
    """Add roles to config.rst_prolog."""

    if not config.rst_prolog:
        config.rst_prolog = ""

    config.rst_prolog += COLORS + REVEAL_BR


def add_rst_epilog(app, config):
    """Add substitutions to config.rst_epilog."""

    if not config.rst_epilog:
        config.rst_epilog = ""

    config.rst_epilog += SYMBOLS + PYTHON_SUBSTITUTIONS + EDITOR_SUBSTITUTIONS


def setup(app: Sphinx) -> None:
    app.connect("config-inited", add_rst_prolog)
    app.connect("config-inited", add_rst_epilog)
