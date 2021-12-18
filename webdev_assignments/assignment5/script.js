const questions = [];
const quizContainer = document.getElementById("quiz");
const resultsContainer = document.getElementById("results");
const submitButton = document.getElementById("submit");

$.getJSON("questions.json", function (data) {
  for (question of data) {
    questions.push(question);
  }

  (function () {
    function showQuiz() {
      const output = [];

      questions.forEach((presentQuestion, questionLetter) => {
        const answers = [];

        for (letter_choice in presentQuestion.answers) {
          answers.push(
            `<label>
            <input type="radio" name="question${questionLetter}" value="${letter_choice}">
            ${letter_choice} :
            ${presentQuestion.answers[letter_choice]}
          </label>`
          );
        }

        output.push(
          `<div class="question"> ${presentQuestion.question} </div>
        <div class="answers"> ${answers.join("")} </div>`
        );
      });

      quizContainer.innerHTML = output.join("");
    }

    function showResults() {
      const answerContainers = quizContainer.querySelectorAll(".answers");

      let numCorrect = 0;

      questions.forEach((presentQuestion, questionLetter) => {
        const answerContainer = answerContainers[questionLetter];
        const selector = `input[name=question${questionLetter}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {})
          .value;

        if (userAnswer === presentQuestion.correctAnswer) {
          numCorrect++;
        }
      });

      resultsContainer.innerHTML = `You got ${numCorrect} out of ${questions.length} points`;
    }

    window.open(showQuiz());

    submitButton.addEventListener("click", showResults);
  })();
});
