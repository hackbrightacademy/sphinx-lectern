==============
Sphinx-Lectern
==============

`sphinx-lectern` is a `Sphinx <https://www.sphinx-doc.org/en/master>`_ extension
`we <https://hackbrighacademy.com/>`_ made to build our curriculum.

The simple idea behind `sphinx-lectern` --- start with one document ➡️ **instantly generate**
lecture handouts, slide decks, tests, demo code, or anything else we've yet to come up with 🌈!

.. warning:: This page is under construction

  Pardon our dust!

Getting Started
===============

Install
-------

You can install `sphinx-lectern` directly from its `GitHub repository <https://github.com/hackbrightacademy/sphinx-lectern>`_
(we haven't published this in PyPI yet but... someday...).

.. parsed-literal::
  :class: console

  $ `pip install git+ssh://git@github.com/hackbrightacademy/sphinx-lectern.git#egg=sphinx-lectern`:cmd:

Then, add ``"sphinxlectern"`` to `extensions` in `conf.py`:

.. code-block::
  :caption: conf.py
  :emphasize-lines: 3

  extensions = [
     # ...
     "sphinxlectern"
  ]

Things You Can Do
=================

Multiple Choice Questions
-------------------------

.. docexample::
  :builder: handouts

  .. mcq:: True or false: Hackbright is a coding bootcamp
    :answer: B

    A. True

       :feedback: We do teach coding but we're not just a coding bootcamp

    B. False

       :feedback: Hackbright is a software engineering bootcamp!

You can put a question in the `knowledge-check` admonition:

.. docexample::
  :builder: handouts

  .. knowledge-check::

    .. mcq:: The differences between natural and formal languages include:
      :answer: B

      A. Natural languages can be parsed while formal languages cannot

         :feedback: Actually both languages can be parsed (determining the structure of the sentence),
                    but formal languages can be parsed more easily in software.

      B. Ambiguity, redundancy, and literalness

         :feedback: All of these can be present in natural languages, but cannot exist in formal languages

      C. There are no differences between natural and formal languages

         :feedback: There are several differences between the two but they are also similar

      D. Tokens, structure, syntax, and semantics

         :feedback: These are the similarities between the two