/**
 * Classe per gestionar cookies al navegador.
 */
class Cookie {
    /**
     * Establim una cookie amb el nom, valor i opcions especificades.
     *
     * @param {string} name - El nom de la cookie.
     * @param {string} value - El valor de la cookie.
     * @param {Object} [options={}] - Opcions addicionals per la cookie.
     * @param {string} [options.path='/'] - La ruta on la cookie és accessible. Per defecte és '/'.
     * @param {Date|number} [options.expires] - La data o temps d’expiració de la cookie.
     * @param {boolean} [options.secure] - Indiquem si la cookie només es pot enviar per HTTPS.
     */
    static set(name, value, options = {}) {
        options = {
            path: '/',
            ...options,
        };

        // Convertim l'opció "expires" a cadena UTC si és un objecte Date
        if (options.expires instanceof Date) {
            options.expires = options.expires.toUTCString();
        }

        // Construim la cadena de la cookie
        let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

        // Afegim cada opció com a part de la cookie
        for (let optionKey in options) {
            updatedCookie += "; " + optionKey;
            let optionValue = options[optionKey];
            if (optionValue !== true) {
                updatedCookie += "=" + optionValue;
            }
        }

        // Establim la cookie al document
        document.cookie = updatedCookie;
    }

    /**
     * Recuperem el valor d’una cookie pel seu nom.
     *
     * @param {string} name - El nom de la cookie que volem obtenir.
     * @returns {string|undefined} - El valor de la cookie si existeix, sino `undefined`.
     */
    static get(name) {
        let matches = document.cookie.match(new RegExp(
            "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        ));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }

    /**
     * Eliminem una cookie pel seu nom.
     *
     * @param {string} name - El nom de la cookie que volem eliminar.
     */
    static delete(name) {
        this.set(name, "", { "max-age": -1 });
    }

    /**
     * Esborrem totes les cookies.
     */
    static clear_all() {
        document.cookie.split(";").forEach(cookie => {
            const eqPos = cookie.indexOf("=");
            const name = eqPos > -1 ? cookie.substring(0, eqPos) : cookie;
            document.cookie = `${name}=;path=/;max-age=0`;
        });
        location.reload(); // Recargar la página
    } 
}