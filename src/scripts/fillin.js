// Script for implementing `fillin` directive.

(() => {
  "use strict";

  const FillinCache = {
    // Get hash of window location & store it on window
    getLocation: function () {
      if (!window.fillinLocationHash) {
        return crypto.subtle.digest(
          'SHA-1',
          new TextEncoder().encode(window.location)
        ).then((buffer) => {
          return Array.from(new Uint8Array(buffer))
            .map(b => b.toString(16).padStart(2, '0'))
            .join('');
        }).then((hashedLocation) => {
          window.fillinLocationHash = hashedLocation;
          return window.fillinLocationHash;
        });
      } else {
        return new Promise((res, rej) => {
          res(window.fillinLocationHash)
        });
      }
    },

    // Get value from localStorage
    getItem: function (key, val) {
      return this.getLocation()
        .then((location) => {
          return localStorage.getItem([location, key].join('-'));
        });
    },

    // Set value in localStorage
    setItem: function (key, val) {
      return this.getLocation()
        .then((location) => {
          return localStorage.setItem([location, key].join('-'), val);
        });
    }
  };

  for (const el of document.querySelectorAll('.fillin')) {
    // Set value of all .fillin elements to cached value.
    // Ids for .fillin elements are prefixed with 'fillin-';
    // the remaining part of the id is the actual value of
    // keys in localStorage
    FillinCache.getItem(el.getAttribute('id')
      .split('-')
      .slice(-1)
    ).then((val) => el.value = val);

    // Cache value on blur
    el.addEventListener('blur', (e) => {
      const target = e.target;
      if (target.value) {
        FillinCache.setItem(
          target.getAttribute('id').split('-').slice(-1),
          target.value
        );
      }
    });
  }
})();
