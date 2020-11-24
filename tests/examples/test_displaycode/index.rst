========================
Displaying Code Examples
========================

Displaying Code w/ `code-block` Directive
=========================================

Basic Example
-------------

`code-block` takes an optional argument --- the name of a language.

(Sphinx uses this to find a compatible Pygments lexer).

Example:

.. code-block:: rst

  .. code-block:: python

    print('Hello, world!')

...will output:

.. code-block:: python

  print('Hello, world!')

Adding Captions
---------------

.. code-block:: rst

  .. code-block:: javascript
    :caption: ReactPartialRenderHooks.js

.. code-block:: javascript
  :caption: ReactPartialRenderHooks.js

  function createWorkInProgressHook(): Hook {
    if (workInProgressHook === null) {
      // This is the first hook in the list
      if (firstWorkInProgressHook === null) {
        isReRender = false;
        firstWorkInProgressHook = workInProgressHook = createHook();
      } else {
        // There's already a work-in-progress. Reuse it.
        isReRender = true;
        workInProgressHook = firstWorkInProgressHook;
      }
    } else {
      if (workInProgressHook.next === null) {
        isReRender = false;
        // Append to the end of the list
        workInProgressHook = workInProgressHook.next = createHook();
      } else {
        // There's already a work-in-progress. Reuse it.
        isReRender = true;
        workInProgressHook = workInProgressHook.next;
      }
    }
    return workInProgressHook;
  }

.. code-block:: jsx

  const Hello = () => {
    return (
      <p>Hi</p>
    );
  }

.. mcq:: Hi
  :answer: A

  A. Wow

     :feedback: Wow