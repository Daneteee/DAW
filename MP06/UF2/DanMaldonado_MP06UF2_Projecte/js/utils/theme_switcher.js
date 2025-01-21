export function initThemeSwitcher() {
    const themeBtns = document.querySelectorAll('.theme-btn');
    
    // Funció per establir el tema seleccionat
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        
        // Guardem el tema seleccionat en una cookie
        document.cookie = `selected-theme=${theme}; path=/; max-age=31536000`; 
    }

    // Funció per obtenir el tema guardat a partir de les cookies
    function getThemeFromCookie() {
        const cookies = document.cookie.split('; '); 
        const themeCookie = cookies.find(row => row.startsWith('selected-theme='));
        
        // Si existeix la cookie del tema la retornem sino retornem el tema per defecte
        return themeCookie ? themeCookie.split('=')[1] : 'default';
    }

    // Carreguem el tema guardat quan inicialitzem el selector
    const savedTheme = getThemeFromCookie();
    setTheme(savedTheme);

    // Apliquem l'estil de selecció al botó del tema actual
    themeBtns.forEach(btn => {
        btn.classList.remove('active'); 
        if (btn.getAttribute('data-theme') === savedTheme) {
            btn.classList.add('active'); 
        }
    });
    
    // Afegim esdeveniments als botons per canviar de tema
    themeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const theme = btn.getAttribute('data-theme');
            
            // Establim el tema seleccionat
            setTheme(theme);
            
            // Actualitzem l'estil dels botons
            themeBtns.forEach(b => b.classList.remove('active')); 
            btn.classList.add('active'); 
        });
    });
}

export default initThemeSwitcher;
