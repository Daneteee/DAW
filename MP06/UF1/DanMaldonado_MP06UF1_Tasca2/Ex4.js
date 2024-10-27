/**
 * Funció per convertir una quantitat d'euros a diferents monedes.
 * Aquesta funció rep una quantitat d'euros i retorna un array 
 * que conté els valors equivalents en iens japonesos, pesetes espanyoles 
 * i corones txeques.
 * 
 * @param {number} euros - Quantitat d'euros a convertir.
 * @returns {Array} - Un array amb les conversions a diferents monedes.
 */

const convertirMonedes = (euros) => [
    (euros * 157.94),
    (euros * 166.386),  
    (euros * 24.93) 
]

const euros = 100
const resultats = convertirMonedes(euros)
console.log(`Euros: ${euros}`)
console.log(`Yens: ${resultats[0]} JPY`)
console.log(`Pesetes: ${resultats[1]} PTE`)
console.log(`Corones: ${resultats[2]} CZK`)
