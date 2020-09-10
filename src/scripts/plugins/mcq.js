(() => {
  'use strict';

  Array.from(document.querySelectorAll('.mcq')).forEach((el) => {
    const { id, ans, feedback } = el.dataset;
    const mcqAlert = el.querySelector('.mcq-alert');
    const mcqData = {
      id,
      ans,
      feedback: JSON.parse(feedback),
    };

    el.querySelector('.mcq-answer-checker').addEventListener('click', (e) => {
      // reset
      mcqAlert.classList.remove(...['mcq-correct', 'mcq-incorrect']);

      const selectedAns = el.querySelector(`input[name="${mcqData.id}"]:checked`);
      if (selectedAns) {
        mcqAlert.classList.add(
          selectedAns.value === mcqData.ans ? 'mcq-correct' : 'mcq-incorrect'
        );
        mcqAlert.innerText = mcqData.feedback[selectedAns.value];
      }
    });
  });
})();
