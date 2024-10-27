/**
 * Funció per tractar un array d'anys de naixement mitjançant una funció passada com a paràmetre.
 * @param {Array} arrayAnys - L'array d'anys de naixement.
 * @param {Function} funcioTracta - La funció que realitza una operació sobre aquests anys.
 * @returns {Array} - El resultat de la funció que tracta els anys.
 */
const tractaAnys = (arrayAnys, funcioTracta) => {
    return funcioTracta(arrayAnys)
}

/**
 * Funció 1: Retorna un array amb les edats calculades a partir dels anys de naixement.
 * @param {Array} arrayAnys - L'array d'anys de naixement.
 * @returns {Array} - Un array amb les edats calculades.
 */
const retornarEdats = arrayAnys => {
    let edats = []
    for (let i = 0; i < arrayAnys.length; i++) {
        edats.push(2024 - arrayAnys[i])
    }
    return edats
}

/**
 * Funció 2: Retorna un array amb valors booleans indicant si cada persona és major d'edat.
 * @param {Array} arrayAnys - L'array d'anys de naixement.
 * @returns {Array} - Un array amb valors true o false segons si la persona és major d'edat.
 */
const filtrarMajorsEdat = arrayAnys => {
    let edats = retornarEdats(arrayAnys)
    return edats.map(edat => edat >= 18)
}

/**
 * Funció 3: Retorna un array indicant quants anys queden per jubilar-se o -1 si ja estan jubilats.
 * @param {Array} arrayAnys - L'array d'anys de naixement.
 * @returns {Array} - Un array amb els anys que queden per jubilar-se o -1 si ja ho estan.
 */
const anysPerJubilarse = arrayAnys => {
    let edats = retornarEdats(arrayAnys)
    return edats.map(edat => edat >= 65 ? -1 : 65 - edat) // Retorna -1 si ja es poden jubilar, o els anys que queden si encara no poden.
}

let arrayAnys = [1992,1998,2002,2001,2010]

console.log("Crida 1:", tractaAnys(arrayAnys, retornarEdats))
console.log("Crida 2:", tractaAnys(arrayAnys, filtrarMajorsEdat))
console.log("Crida 3:", tractaAnys(arrayAnys, anysPerJubilarse))
