===============
Example Lecture
===============

Section Heading
===============

Slide Title
-----------

- Notice how `h2` create title slides

- Use these to divide a lecture by its topics

Another Slide
-------------

Each `h3` creates a new slide

Subsection
^^^^^^^^^^

`h4` will stay on the same slide though

Newslide
--------

Another way to create a new slide is with `newslide`:

.. code-block:: rst

  .. newslide::

.. newslide::

`newslide` does not take any children, so don't indent!

.. interslide::

  An interslide

One More Thing
==============

One More Thing
--------------

You *are* required to make an `h3` right after an `h2`.

Don't worry, these headers won't repeat in handouts.

Transitions
===========

Incremental Directive
---------------------

.. incr:: one

  Make this appear on `Space`

.. incr:: one

  Then make this one appear

Increment Ea. Item
------------------

This works with any list & will cause each item @ top-level |reveal-br|
to appear one at a time

.. incr:: item

  - One

  - Two

  - Three

.. newslide::

.. incr:: item

  #. One

  #. Two

  #. Three

.. newslide::

.. incr:: item

  Def one
    def

  def two
    hi

.. newslide::

.. incr:: item

  - Children will appear too

    - Child

    - Child

  - Hi

  - Hello

    - Child

Increment Every Item
--------------------

To increment every item, no matter how far they're nested, use

.. code-block:: rst

  .. incr:: item

.. newslide::

.. incr:: item

  - Greetings

    - Hi

    - Hello

  - Goodbyes

    - Goodbye

    - Bye

      - Buh-bye

