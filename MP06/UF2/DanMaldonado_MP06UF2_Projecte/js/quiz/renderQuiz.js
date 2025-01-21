import { shuffleArray } from './utils.js';

export function renderQuiz(questions) {
    const quizContainer = document.getElementById('quiz-container');
    
    const quizHTML = questions.map((q, index) => {
        // Barregem les respostes
        const allAnswers = [q.correct_answer, ...q.incorrect_answers];
        const shuffledAnswers = shuffleArray(allAnswers); 

        return `
            <div class="quiz-question">
                <h3>${index + 1}. ${decodeHTML(q.question)}</h3>
                <div class="quiz-options">
                    ${shuffledAnswers.map((answer, answerIndex) => `
                        <label>
                            <input 
                                type="radio" 
                                name="question${index}" 
                                value="${answer}"
                            >
                            ${decodeHTML(answer)}
                        </label>
                    `).join('')}
                </div>
            </div>
        `;
    }).join('');

    // Afegim el botó per avaluar les respostes
    quizContainer.innerHTML += `
        <div id="quiz-controls">
            <button id="evaluate-btn">Evaluar Respostes</button>
        </div>
    `;

    // Inserim les preguntes
    const quizQuestionsContainer = document.createElement('div');
    quizQuestionsContainer.innerHTML = quizHTML;
    quizContainer.insertBefore(quizQuestionsContainer, document.getElementById('quiz-controls'));

    // Habilitem el botó d'avaluació quan es responguin totes les preguntes
    const radioButtons = quizContainer.querySelectorAll('input[type="radio"]');
    const evaluateBtn = document.getElementById('evaluate-btn');

    radioButtons.forEach(radio => {
        radio.addEventListener('change', () => {
            // Obtenim tots els grups de preguntes
            const questionGroups = new Set(
                Array.from(radioButtons).map(r => r.getAttribute('name'))
            );
            
            // Obtenim les preguntes que han estat respostes
            const answeredQuestions = new Set(
                Array.from(radioButtons)
                    .filter(r => r.checked)
                    .map(r => r.getAttribute('name'))
            );

            // Habilitem el botó d'avaluació si totes les preguntes estan respostes
            if (questionGroups.size === answeredQuestions.size) {
                evaluateBtn.style.display = "block";
            }
        });
    });

    // Avaluem les respostes
    evaluateBtn.addEventListener('click', () => {
        let correctAnswers = 0;

        // Comprovem cada pregunta
        questions.forEach((q, index) => {
            const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
            const questionContainer = selectedOption.closest('.quiz-question');
            const labels = questionContainer.querySelectorAll('label');

            labels.forEach(label => {
                const radioInput = label.querySelector('input');
                
                // Si la resposta seleccionada és correcta, afegim la classe 'correct-answer'
                if (radioInput.value === q.correct_answer) {
                    label.classList.add('correct-answer');
                    
                    // Comprovem si la resposta seleccionada és correcta
                    if (radioInput === selectedOption) {
                        correctAnswers++;
                    }
                } else if (radioInput === selectedOption) {
                    label.classList.add('incorrect-answer');
                }

                // Deshabilitem les respostes després de l'avaluació
                radioInput.disabled = true;
            });
        });

        // Mostrem el resultat
        const resultMessage = document.createElement('div');
        resultMessage.classList.add('result-message');
        resultMessage.innerHTML = `
            Has encertat ${correctAnswers} de ${questions.length} preguntes.
        `;
        
        quizContainer.appendChild(resultMessage);

        evaluateBtn.style.display = 'none';
    });
}

// Funció per decodificar les entitats HTML
function decodeHTML(html) {
    const txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
}
