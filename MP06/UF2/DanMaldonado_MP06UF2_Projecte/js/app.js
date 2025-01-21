import { renderSpotifyTracks } from './music_app/spotify.js';
import { initThemeSwitcher } from './utils/theme_switcher.js';
import { setupScrollToTop } from './utils/top_scroll.js';
import { createUserForm } from './userForm.js';
import { createRockQuiz } from './quiz/quiz.js';
import { initSlider } from './utils/slider.js';
import { setupClock } from './clock.js';

// Inicialitzem funcions
initThemeSwitcher();
initSlider();
setupScrollToTop();

function initSectionButtons() {
    const sectionButtons = document.querySelectorAll('.section-btn');
    const mainContent = document.querySelector('.main-content');

    // Afegim un event listener a cada botó
    sectionButtons.forEach(button => {
        button.addEventListener('click', async () => {

            // Deshabilitem els botons (Perque mentres carregui una secciona no es pugui carregar un altre)
            sectionButtons.forEach(btn => btn.disabled = true);
            
            const section = button.getAttribute('data-section');
            
            // Netegem el contingut anterior
            mainContent.innerHTML = '';

            // Actualitzem els estils de tots els botons
            sectionButtons.forEach(btn => btn.style.backgroundColor = 'var(--secondary)');
            button.style.backgroundColor = 'var(--accent)';

            // Funció depenent de la secció
            switch(section) {
                case 'music':
                    await renderSpotifyTracks(); 
                    break;
                case 'clock':
                    setupClock(); 
                    break;
                case 'register':
                    createUserForm(); 
                    break;
                case 'quiz':
                    createRockQuiz();
                    break;
                default:
                    mainContent.innerHTML = '<h2>Selecciona una secció</h2>';
            }

            // Habilitem els botons
            sectionButtons.forEach(btn => btn.disabled = false);

        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    initSectionButtons();
});
