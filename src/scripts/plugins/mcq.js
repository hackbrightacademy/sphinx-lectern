(() => {
  'use strict';

  Array.from(document.querySelectorAll('.mcq.show-feedback')).forEach((el) => {
    console.log(el);
    const { id, ans, feedback } = el.dataset;
    const mcqAlert = el.querySelector('.mcq-alert');

    el.querySelector('.mcq-answer-checker').addEventListener('click', (e) => {
      // reset
      mcqAlert.classList.remove(...['mcq-correct', 'mcq-incorrect']);

      const selectedAns = e.target.previousElementSibling
        .querySelector('input:checked')
        .parentElement.querySelector('li');
      const { isCorrect, feedback } = selectedAns.dataset;

      if (selectedAns) {
        mcqAlert.classList.add(isCorrect === 'True' ? 'mcq-correct' : 'mcq-incorrect');
        mcqAlert.innerHTML = `<div id="mcq-alert-body">${
          JSON.parse(feedback)['html']
        }</div>`;
      }
    });
  });
})();
