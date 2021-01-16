=========================
Multiple Choice Questions
=========================

Question in an Admonition
=========================

You can put a question in the `knowledge-check` admonition:

.. knowledge-check::

   .. mcq:: The differences between natural and formal languages include:
     :answer: B
     :show_feedback:

     A. Natural languages can be parsed while formal languages cannot

        :feedback: Actually both languages can be parsed (determining the structure of the
                   sentence), but formal languages can be parsed more easily in software.

                   I'm continuing the paragraph here **and** adding *styles* to see if the extension can handle nested text

     B. Ambiguity, redundancy, and literalness

        :feedback: All of these can be present in natural languages, but cannot exist in formal languages

     C. There are no differences between natural and formal languages

        :feedback: There are several differences between the two but they are also similar

     D. Tokens, structure, syntax, and semantics

        :feedback: These are the similarities between the two

Standalone Question
===================

A question that's not inside an admonition:

.. mcq:: The differences between natural and formal languages include:
  :answer: B
  :numbered:

  A. Natural languages can be parsed while formal languages cannot

     :feedback: Actually both languages can be parsed (determining the structure of the sentence),
                but formal languages can be parsed more easily in software.

  B. Ambiguity, redundancy, and literalness

     :feedback: All of these can be present in natural languages, but cannot exist in formal languages

  C. There are no differences between natural and formal languages

     :feedback: There are several differences between the two but they are also similar

  D. Tokens, structure, syntax, and semantics

     :feedback: These are the similarities between the two

.. mcq:: True or false: Hackbright is a coding bootcamp
  :answer: B
  :numbered:

  You can have even more complex stuff in here. I hope.

  .. code-block:: python

    print("hi")

  A. True

     :feedback: We do teach coding but we're not just a coding bootcamp

  B. False

     :feedback: `Hackbright` is a software engineering bootcamp!