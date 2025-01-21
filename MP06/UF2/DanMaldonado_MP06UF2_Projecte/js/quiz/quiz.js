import { fetchRockQuestions } from './rockQuestions.js';
import { shuffleArray } from './utils.js';
import { renderQuiz } from './renderQuiz.js';

// Quiz de Rock
export async function createRockQuiz() {
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = '<div id="quiz-container"></div>';
    const quizContainer = document.getElementById('quiz-container');

    try {
        // Petició a la API de Open Trivia 
        const rockQuestions = await fetchRockQuestions();
        
        // Barrejem les preguntes
        const shuffledQuestions = shuffleArray(rockQuestions);

        // Renderitzem preguntes
        renderQuiz(shuffledQuestions);

    } catch (error) {
        console.error('Error en carregar el quiz:', error);
        quizContainer.innerHTML = `<p>Error en carregar el quiz. Intenta-ho de nou.</p>`;
    }
}

// Afegim el full d'estils
const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = '/css/quiz.css';
document.head.appendChild(link);
