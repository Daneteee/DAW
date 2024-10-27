/**
 * Funció genèrica que aplica una funció a tots els elements d'un array.
 * @param {Array} array - L'array d'elements a tractar.
 * @param {Function} funcio - La funció que s'aplicarà a cada element de l'array.
 * @returns {Array} - Un nou array amb els resultats de l'aplicació de la funció.
 */
const dividirXDos = (num) => num / 2 // Retornem el nombre dividit per 2
const aplicarFuncio = (array, funcio) => array.map(funcio) // Apliquem la funció a cada element de l'array

const nombres = [2, 4, 6, 8, 10]

console.log(aplicarFuncio(nombres, dividirXDos)) 
