<!-- omit in toc -->
# Project Overview

***sphinx-lectern*** is a Sphinx extension that adds a bunch of nice markup we
use to generate handouts and slide decks.

### Contents of *this* file

- [About Sphinx](#about-sphinx)
  - [The basic idea though...](#the-basic-idea-though)
- [About sphinx-lectern](#about-sphinx-lectern)
  - [Project directory structure](#project-directory-structure)

#### Other docs you might be looking for

(None of these documents exist yet sorry)

- Quickstart
- How to write a basic lecture
- IDK what else to put here

## About Sphinx

Here's how Sphinx describes itself on [its homepage](https://www.sphinx-doc.org/en/master/):

> Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written
> by Georg Brandl and licensed under the BSD license.

...it's a *terrible* description. Not just because Sphinx was originally created for
building the Python docs and not much else but also 'cause &mdash; even though
its initial use-case was pretty specific &mdash; it can do **wayyyyy too much**.

### The basic idea though...

Sphinx can take a document written in some sort of markup language...

```rst
=============
Hello, World!
=============

This is a document written in a markup language called `reStructuredText <https://docutils.sourceforge.io/rst.html>`_.

Trendy Language is Trendy
=========================

Look, ma! Code!!!

.. code-block:: rust

  fn bubble_sort<T: PartialOrd + Clone>(items: &[T]) -> Vec<T> {
    // I looooOOOOove living in a type-safe nanny state!!
  }
```

...and turn it into some other type of document. Like this one:

```html
<section>
  <h1>Hello, World!</h1>
  <p>This is a document...</p>
  <section>
    <h2>Trendy Language is Trendy</h2>
    <p>Look, ma! Code!!!</p>
    <pre>
      <code><!-- ... --></code>
    </pre>
  </section>
</section>
```

Or this:

```json
{
  "node": "section",
  "children": [
    {
      "node": "header",
      "children": [
        {
          "node": "text",
          "body": "Hello, World!"
        }
      ]
    }
  ]
}
```

Or this:

```jsx
ReactDOM.render(
  <Document doctree={JSON.parse(doctree)} />,
  document.querySelector('#root')
);
```

## About sphinx-lectern

By default, Sphinx already has nice features for building documentation that are
also pretty convenient for building SWE bootcamp curriculum. But we needed more.

***sphinx-lectern*** is a Sphinx extension that adds a bunch of custom markup,
utilities, and behavior(s) to Sphinx. It's how we generate our lecture handouts
and slide decks.

Soooooo... yeah. That's it for now.

### Project directory structure

If you wanna figure out what's going on:

- **[tests/examples](../tests/examples)** is probably a good place to start? It
  has examples of ***sphinx-lectern's*** features in action.
- If you wanna look at code instead
  - **[sphinxlectern/](../sphinxlectern)** contains all the Sphinx extension
    guts
  - **[src/](../src)** is where you'll find the source for building static CSS and
    JS files for our custom Sphinx theme
    - We *don't* use Sphinx to put all our static dependencies in the right
      place (gross!); we use [Gulp](https://gulpjs.com/) like most sane people
      do
      - Like. Did you know that Sphinx has (at time of writing) a jQuery
        dependency and all sorts of other weird stuff?

That's really all I can tell you for now. Stay tuned for more later!