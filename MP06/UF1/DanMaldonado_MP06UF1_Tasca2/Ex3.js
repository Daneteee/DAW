/*
 * Funció que ordena alfabèticament els caràcters d'una cadena de text.
 * Aquesta funció rep una cadena i retorna una nova cadena amb els caràcters
 * ordenats en ordre alfabètic.
 * 
 * @param {string} cadena - La cadena de text a ordenar.
 * @returns {string} - La cadena ordenada alfabèticament.
 */
const ordenarCadena = cadena => cadena.split('').sort().join('')

console.log(ordenarCadena("abska"))
