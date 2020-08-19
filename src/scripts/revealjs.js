const Reveal = require('reveal.js');
const RevealNotes = require('./plugins/notes.js');

Reveal.initialize({
  maxScale: 5,
  width: 1280,
  height: 800,
  margin: 0.1,
  transition: 'slide'
});

Reveal.registerPlugin('notes', RevealNotes('_static/revealjs/notes.html', Reveal));

Array.from(document.querySelectorAll('.external'))
  .forEach((link) => {
    link.setAttribute('target', '_blank');
  });
