// Funció per inicialitzar el carrusel
export function initSlider() {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.slider-dot');
    let currentSlide = 0; 

    // Funció per mostrar una diapositiva específica
    function showSlide(index) {
        // Eliminem la classe 'active' de totes les diapositives
        slides.forEach(slide => {
            slide.classList.remove('active');
        });

        // Desactivem tots els punts del carrusel
        dots.forEach(dot => {
            dot.classList.remove('active');
        });

        // Activem la diapositiva i el punt actual
        slides[index].classList.add('active');
        dots[index].classList.add('active');
    }

    // Events als punts per canviar de diapositiva
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentSlide = index; 
            showSlide(currentSlide); 
        });
    });

    // Funció per avançar automàticament les diapositives
    function autoAdvanceSlide() {
        currentSlide = (currentSlide + 1) % slides.length; 
        showSlide(currentSlide); 
    }

    setInterval(autoAdvanceSlide, 5000);

    showSlide(currentSlide);
}

export default initSlider;
