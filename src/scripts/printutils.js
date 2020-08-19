(() => {
  "use strict";

  window.addEventListener('beforeprint', (e) => {
    for (const el of document.querySelectorAll('details')) {
      el.setAttribute('open', true);
    }
  });

  window.addEventListener('afterprint', (e) => {
    for (const el of document.querySelectorAll('details')) {
      el.setAttribute('open', false);
    }
  });
})();
