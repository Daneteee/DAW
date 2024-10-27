/**
 * Funció que elimina tots els elements innecessaris d'un array.
 * Per exempla: 
 * cadenes buides (''), valors falsos (false), indefinits (undefined), 
 * zero (0) i valors nuls (null).
 *
 * @param {Array} array - L'array original amb elements diversos.
 * @returns {Array} - Nova array sense valors innecessaris.
 *
 */

let array = [0, 1, false, 2, '', 3, null, undefined, NaN, 4];
let result = array.filter(Boolean);

console.log(result); // [1, 2, 3, 4]
