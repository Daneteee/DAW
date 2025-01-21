export function setupScrollToTop() {
    // Creem el botó de "tornar a dalt"
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.innerHTML = '↑';
    
    // Estils del botó
    scrollToTopButton.style.position = 'fixed';
    scrollToTopButton.style.bottom = '20px';
    scrollToTopButton.style.right = '20px';
    scrollToTopButton.style.backgroundColor = 'var(--accent)';
    scrollToTopButton.style.color = 'white';
    scrollToTopButton.style.border = 'none';
    scrollToTopButton.style.borderRadius = '50%';
    scrollToTopButton.style.width = '50px';
    scrollToTopButton.style.height = '50px';
    scrollToTopButton.style.fontSize = '24px';
    scrollToTopButton.style.cursor = 'pointer';
    scrollToTopButton.style.zIndex = '1000';

    // Inicialment ocult
    scrollToTopButton.style.display = 'none'; 
    scrollToTopButton.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
    scrollToTopButton.style.outline = 'none';
    scrollToTopButton.style.transition = 'opacity 0.3s';

    document.body.appendChild(scrollToTopButton);

    // Funció per mostrar o ocultar el botó
    function toggleScrollToTopButton() {
        // Mostrem el botó quan hàgim baixat més de 300 píxels
        if (window.scrollY > 300) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    }

    // Event de scroll per comprovar quan mostrar el botó
    window.addEventListener('scroll', toggleScrollToTopButton);

    // Event de clic per tornar a dalt
    scrollToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    scrollToTopButton.addEventListener('mouseenter', () => {
        scrollToTopButton.style.opacity = '0.8';
    });

    scrollToTopButton.addEventListener('mouseleave', () => {
        scrollToTopButton.style.opacity = '1';
    });
}

document.addEventListener('DOMContentLoaded', setupScrollToTop);
