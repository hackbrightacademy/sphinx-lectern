============
Demo Lecture
============

Section Heading
===============

Slide Title
-----------

- This is a fake lecture

- But it should show lots of feature of our Sphinx system

- It is also a test case for our builders/CSS stylesheets

- As you add features/CSS classes/etc, please add them here

Another Slide Title
-------------------

- It's Pretty Rare

- But You Can Have a Subsection!

Subsection
++++++++++

Like This

Basic Styling
=============

Typography
----------

Put blank lines between paragraphs.

Basic Styling
-------------

- For emphasis, use *italics*

- For more emphasis, use **bold**

- For link, use `Go to Google <http://google.com>`_

Citations
---------

Citations use single backticks: \`like this\`. Use for:

- variable names

  - eg: We can now set `x`

- file or path names

  - eg: Store this in `secrets.sh`

- class names

  - eg: Remember our `Cat` class?

- function or method names

  - eg: Never call `lets_play_global_thermonuclear_war`

**Do not use this for general emphasis, please!** Use bold or italics for that.

Code Literals
-------------

Code literals use double backticks: \`\`like this\`\`

These are for literal code blocks or literal coding values:

- things like ``x = 0``

- but not for just talking *about* a variable, function, etc.

  - use `citations` for that

- eg: call `set_color` like this: ``set_color('blue')``

Dashes
------

Use 3 dashes for an em dash---like this.

Two dashes makes an "en dash"--it's too short!

Superscripts and Subscripts
---------------------------

O(n\ `2`:sup:\ )

log\ `2`:sub:\ n

.. only:: not revealjs

  Notice how we use a backslashed space there---it's not legal
  to have styles right next to a word (like O(n`2`:sup:), which
  doesn't look right). The backslash space separates the tokens,
  but does't add a real space.

Line Breaks
-----------

As an example:

| You can force line breaks
| by doing this

Or, you can add a slide-only break |reveal-br|
like this.

Symbols
-------

- |nbsp|    NONBREAKING SPACE

- |rarr|    RIGHTWARDS ARROW

- |larr|    LEFTWARDS ARROW

- |lrarr|   BOTH ARROW

- |plus|    PLUS SIGN

- |times|   MULTIPLICATION SIGN

- |check|   CHECK MARK

- |approx|  ALMOST EQUAL TO

- |sub2|    SUBSCRIPT 2

- |super2|  SUPERSCRIPT 2

.. newslide::

- |pycmd|   The command to run Python

And the same replacement, inside the console:

.. parsed-literal::
   :class: console

   $ |pycmd| `show_prompt.py`:cmd:

Lists
=====

Lists
-----

- Always put blank line between bulleted list items

- Otherwise bad things will happen!

  - You can have many levels

  - Just indent them

    - Useful for further explanations

  - Try to stick to 2

    - Our CSS only stylizes up to level 3

    - So stop here

- And back to level one

Complex Lists
-------------

- You can also have lists that are not "simple"

  This is where you have multiple paragraphs in a list

  - You can still nest these

    Like so

.. newslide::

More about complex lists:

- This happens with things like code blocks

  .. code-block::

    x = 0

- See?

.. newslide::

More about complex lists:

- Another case is

- Where you have a simple list

  - Containing a complex list

    This has a second paragraph

- The spacing should work out

Horizontal Lists
----------------

You can make short, side-by-side lists like this:

.. hlist::

  - one

  - two

  - three

  - four

You can specify # columns, too:

.. hlist::
  :columns: 3

  - one

  - two

  - three

  - four

  - five

  - six

Organization
============

Organization
------------

If your slide title is the same as the section title, like this,
the handouts won't repeat it. So do this for things like the "Goals"
slide in a "Goals" section.

New Slides
----------

When you want slide break that shouldn't cause a new
heading in the handouts, |reveal-br| use the `newslide` directive.

.. newslide::

This is a new slide with the same title, but on the handouts, it
just flows.

Note: slide content isn't contained in `newslide`,
it just appears after it.

.. newslide:: New Title

This is a new slide with a new title, but on the handouts, it just
flows.

.. newslide:: +(continued)

A new slide with an addition to the title.

.. newslide:: Colors
  :background: yellow

You can also use newslide to get background colors

.. newslide:: Images
  :background: porcupine.jpg

`Or images!`:white:

.. interslide::

  Interslides never appear on the handouts and don't have a title.

  They're useful for fun, silly things, like large images and text.

  Notice the content of interslide is inside the interslide.

.. interslide::

  You can put any type of content in an interslide.

  .. image:: porcupine.jpg
    :width: 100%

.. interslide::
  :background: porcupine.jpg

  `They can also have backgrounds`:white:

Images
======

Images
------

Add images like so:

.. image:: porcupine.jpg
  :width: 50%

It's good to set a width on it --- otherwise, these are huge on the handouts.

.. newslide::

To make an image smaller on handouts, size it with ems:

.. image:: porcupine.jpg
  :width: 10em

(since ems are so much bigger on slides than handouts)

.. only:: not revealjs

  This is especially good for things like book cover images,
  since we want them to appear big on slides for visual pop,
  but they can appear much smaller on handouts.

.. newslide::

For images without good definition, you can add a border:

.. image:: porcupine.jpg
  :width: 50%
  :class: image-border

.. newslide::

For less-important images that should appear in handouts but not
on printed material, use the `noprint` class:

.. image:: porcupine.jpg
  :width: 50%
  :class: noprint

Transitions
===========

Arbitrary Items
---------------

To make things appear one at a time, use the `incremental` directive

.. incremental:: one

  .. code-block:: rst

    .. incremental:: one

      Like this

.. incremental:: one

  Using it multiple times works, too!

Lists
-----

You can use on lists, too!

.. incremental:: item

  - This causes each top-level bullet point

  - To appear at once

    - But secondary points

    - Appear with parents

  - Like so

.. newslide::

The `nest-incremental` class makes each bullet appear incrementally:

.. incremental:: nest

  - Each bullet

    - Now appears

      - Incrementally

  - Like so

.. newslide::

Works on numbered lists:

.. incremental:: item

  #. One

  #. Two

  #. Three

.. newslide::

And definition lists:

.. incremental:: item

  Term one
    This is a definition list

  Term two
    Use it to define or describe terms

.. newslide::

When you use ``.. incremental:: nest`` on a definition list, both terms
and definitions will appear one at a time:

.. incremental:: nest

  Term one
    Definition

  Et cetera
    Definition

Effects
-------

We rarely use these, but they work so here ya go

.. incremental:: one
  :class: grow

  This Grows!

.. incremental:: one
  :class: fade-out

  This fades out

.. incremental:: one
  :class: current-visible

  This is visible then goes away

Literal Blocks
==============

Literal Blocks
--------------

To show literal text blocks, use the explicit ``code-block`` directive

.. code-block::

  Hello! *not italics*

Parsed Literal
--------------

You can use parsed literal for literal blocks that still parse for
style stuff.

.. parsed-literal::

  Hello *italics* and `citation` and `red`:red:

Console
-------

We use a special class on parsed literal for showing shell commands:

.. parsed-literal::
  :class: console

  $ `echo "this is a command"`:cmd:
  this is a command

  $ `echo`:cmd:  `# comment`:comment:

.. parsed-literal::
  :class: console

  Hello

Code Blocks
===========

Code Blocks
-----------

Ask for a code block like so

.. code-block:: python

  if name == "joel":
      print("hi")

.. code-block:: html

  <a href="yo.html">&copy; <!-- comment --></a>

(also: js, sql, xml, and many others---see "pygments" library)

Emphasizing Lines
-----------------

Can emphasize lines:

.. code-block:: python
  :emphasize-lines: 1, 3-4, 6-

  if name == "joel":
      print("hi")
      print("there")
      print("joel")
      print("and")
      print("everyone")
      print("else")

Add Captions
------------

.. code-block:: python
  :caption: example.py

  if name == "joel":
      print("hi")

.. only:: not revealjs

  It's our style to use this for the filenames of demo files
  or if some explanation is needed of where this code is coming from.

.. code-block:: python
  :caption: example.py

  if name == "joel":
      print("hi")

Literal Includes
----------------

Whenever possible, don't inline code --- it's too easy for it to have bugs!

Instead, keep the code in a separate file, so we can test it and include as
demo code

.. newslide::

.. literalinclude:: demo-demo/demo-include.py

.. newslide::

Can use caption/name like for code blocks:

.. literalinclude:: demo-demo/demo-include.py
  :caption: A Demo

.. newslide::

Better, if caption is there but blank, it gets file name

.. literalinclude:: demo-demo/demo-include.py
  :caption:

Finding Things
--------------

Can only include certain lines and can emphasize:

.. literalinclude:: demo-demo/demo-include.py
  :lines: 1, 2, 14-15
  :emphasize-lines: 3

.. newslide::

Better is to find things with `pyobject`

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat

.. newslide::

Can also use `start-after` and `end-before` to match text:

.. literalinclude:: demo-demo/demo-include.py
  :start-after: Do other stuff

.. literalinclude:: demo-demo/demo-include.py
  :lines: 3-
  :end-before: Do other stuff

.. newslide::

This lets us show only one method on a class:

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat.meow
  :prepend: class Cat(object):  # ...

This is used when we want to highlight part of a longer class.

.. newslide::

Or, if we want to pull the method out to show it simply:

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat.meow
  :dedent: 4

(The `dedent` removes four leading spaces)

Don't Use `code`
----------------

There's also a `code` directive that works for Sphinx but it
appears to be undocumented. We style it the same, but don't use it---use
`code-block`, instead.

Notes, Sidebars, Hints, etc.
============================

Admonition
----------

Notes, warnings, and hints are all subclasses of the `admonition` directive.

.. admonition:: They all require titles!

  You can put anything inside of 'em and they **only appear in handouts.**

Notes
-----

Notes are blue.

.. note:: This is a note.

  It goes on.

  And on.

Use notes for sidebar-style information.

.. note:: Other Stuff In Notes

  You can put anything ou want in a note.

  .. code-block:: python

    if name == "joel":
        print("hi")

Warnings
--------

Use warnings to catch students' attention and warn them about gotchas.

.. warning:: This is a warning.

  Make sure you run this command in the correct directory.

Hints
-----

Hints are special; their content is hidden behind an expanding toggle.

.. hint:: Using a certain data structure will make this problem easier

  You could solve this in other ways, but using a linked list (or a
  doubly-linked list) is often a good way to solve this problem. You can do so by
  making the list "circular" --- having the last item in the linked list point back
  to the first item.

  This will let you traverse the list, removing items until one remains.

Hiding Details
--------------

If you want to hide something that's not a hint, use `toggle-reveal`

.. togglereveal::

  Write a function that takes in a number and blah blah blah.

Containers
==========

Containers
----------

The `container` directive just adds a div.

.. container::

  Boring!

This is useful if you want to put a class on it:

.. container:: someclass

  Now I have `someclass` on my `div`

Big Code
--------

`big` makes code blocks and literal blocks bigger

.. container:: big

    .. code-block:: python

        if name == "joel":
            print("hi")


.. newslide:: Works with Parsed Literals

.. container:: big

  .. parsed-literal::

    Hey, I'm `red`:red: and big!

.. parsed-literal::
  :class: big

  Hey, I'm also `red`:red: and big!

Small Code
----------

For longer listings:

.. container:: compare

  .. container::

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (normal size)

  .. container:: small

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (smaller)

Text-Heavy
----------

For big, bold text on slides, use text-heavy:

.. container:: text-heavy

  Like this

Or even `like this`:text-heavy:

Comparing Things
================

Comparing Things
----------------

Instead of just one thing:

.. code-block:: js

  if (name == "joel")
      console.log("hi");

Side-by-side comparisons are useful:

.. container:: compare

  .. code-block:: js

    if (name == "joel")
        console.log("hi");

  .. code-block:: python

    if name == "joel":
        print("hi")

.. newslide::

.. container:: compare

  .. container::

    The spacing should look right even if we lead with compare, or
    if the compares are textual.

  .. container::

    .. code-block:: python

      if name == "joel":
          print("hi")

    .. code-block:: python

      if name == "joel2":
          print("hi")

.. newslide::

You can compare an arbitrary #  of things:

.. container:: compare

  .. container::

    Hi

  .. container::

    - A list

    - Of things

  .. code-block:: python

    print('Hello, world!')

Only
====

Only
----

To have things only appear on slides:

.. only:: revealjs

  This only appears on slides

To have things not appear on slides, but everywhere else:

.. only:: not revealjs

  This does not appear on slides.

  Don't ever say "only:: handouts"---since we have other possible
  non-slide formats (LaTeX, epub, etc). Always say "only:: not revealjs".

ifconfig
--------

You can use ifconfig for logical conditions:

.. ifconfig:: 1 + 1 == 2

  Math works!

.. ifconfig:: 1 + 1 == 3

  Ut Oh.

.. ifconfig:: 'Fall 2015' in project

  You can refer to variables in the conf.py

Definition Lists
================

Definition Lists
----------------

A Definition List
  Is useful for things like

Glossary Terms
  And stuff like that

.. newslide::

Also Works
  When the things are multi-paragraph

  like here.

Should Look Ok
  Even if some thing are not multi-paragraph

Tables
======

Standard Table
--------------

====================== =========== =========== =========== ============ ============
Data Structure         Get         Add         Delete      Iterate      Memory
====================== =========== =========== =========== ============ ============
Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
====================== =========== =========== =========== ============ ============

Centered Columns
----------------

Can center columns other than first:

.. rst-class:: td-center

  ====================== =========== =========== =========== ============ ============
  Data Structure         Get         Add         Delete      Iterate      Memory
  ====================== =========== =========== =========== ============ ============
  Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
  Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
  Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
  ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
  ====================== =========== =========== =========== ============ ============

Right Columns
-------------

Can right-justify columns other than first:

.. rst-class:: td-right

  ====================== =========== =========== =========== ============ ============
  Data Structure         Get         Add         Delete      Iterate      Memory
  ====================== =========== =========== =========== ============ ============
  Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
  Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
  Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
  ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
  ====================== =========== =========== =========== ============ ============

Quotes
======

Quote
-----

Always use the explicit `epigraph` directive

.. epigraph::

  A rose is a rose is a rose.

  -- Gertrude Stein

.. newslide::

.. epigraph::

  I like green eggs and ham.

  I really do. I'm Sam I Am.

  -- Sam I Am

Do not add quotes --- our CSS will do that for you

Plots
=====

Plots
-----

Add `matplotlib` plots:

.. plot::
  :width: 20em

  import numpy as np
  import matplotlib.pyplot as plt

  x = np.arange(0, 100000, 5000)
  plt.plot(x, x / 1000, 'bo')
  plt.ylabel('time', fontsize=20)
  plt.xlabel('size of list', fontsize=20)
  plt.xticks([])
  plt.yticks([])
  plt.title('pop()', fontsize=35)

Math
====

Math
----

Adding math:

.. math::

    r = \frac{\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\Sigma^n_{i=1}(x_i - \bar{x})^2 \times \Sigma^n_{i=1}(y_i - \bar{y})^2}}

Or `n = {x}^2`:math: for inline.

Graphs
======

Graphs
------

Graphviz graphs are super-common and useful:

.. digraph:: org
  :revealjs: width: 50%;
  :handouts: width: 80%;

  Organisms -> { Plants, Fungi, Animals, Bacteria, Protists };
  Animals -> { Cnidaria, Molluscs, Chordata, Arthropods, Echinoderms };
  Chordata -> { Actinopterygii, Mammalia, Chondrichthyes, Aves, Amphibia, Reptilia };
  Mammalia -> { Carnivora, Primate, Artiodactyla, Rodentia };

Put in sizes for `revealjs`, `handouts`, and `latex`.

Generally, `handouts` and `latex` will be about half the size of `revealjs`.

Colors
======

Colors
------


You can use colors:

- `red`:red:

- `green`:green:

- `orange`:orange:

- `tan`:tan:

- `blue`:blue:

- `purple`:purple:

- `yellow`:yellow:

- `gray`:gray:

- `gone`:gone:

- `inv-red`:inv-red:

.. newslide::

How these look in a literal block:

.. parsed-literal::

    `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `purple`:purple: `yellow`:yellow: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

And in a console:

.. parsed-literal::
    :class: console

    `cmd`:cmd: `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `purple`:purple: `yellow`:yellow: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

Speaker Notes
=============

Speaker Notes
-------------

You can add speaker notes with the `speaker` directive. These appear in "speaker notes" view
(press **S** in revealjs). This never appears on handouts.

.. speaker::

  Example speaker note.

Stress Test Longest Possible Section Title
==========================================

Stress Test Longest Possible Slide Title Is This One
----------------------------------------------------

- One This Should Fit On One Line Even Though It's Really Really Long

- Two

- Three

- Four

- Five

- Six

- Seven

- Eight

- Nine

- Ten

- Eleven

Code Stress Test
----------------

.. code-block:: python

    class Cat5(object):
        """Cat with class methods."""

        _SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"
        _UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name"

        def __init__(self, name, hunger):     # special method
            self.name = name                  # object attribute
            self.hunger = hunger

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.commit()

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.commit()
