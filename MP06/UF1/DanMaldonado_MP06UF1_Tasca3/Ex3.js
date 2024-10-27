/**
 * Funció que retorna l'element que té més repeticions en un array.
 * 
 * Aquesta funció compta quantes vegades apareix cada element en l'array
 * i determina quin és l'element que es repeteix més vegades. 
 * Si hi ha un empat, es retornarà el primer element que es troba amb el màxim de repeticions.
 * 
 * @param {Array} array - L'array d'elements sobre el qual s'analitza la freqüència.
 * @returns {string} - Una cadena que indica quin element té més repeticions i quantes vegades apareix.
 * 
 * Exemple d'ús:
 *  Input: ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'a', 'a']
 *  Output: "La lletra: a 5 apareix vegades"
 */

const arrayLletres = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'a', 'a'];

const mostRepeated = (array) => {
    let comptador = {};

    // Creem una llista associativa per comptar cada cop que apareix una lletra
    for (let element of array) {
        if (comptador[element]) {
            comptador[element]++;
        } else {
            comptador[element] = 1;
        }
    }

    let maxRepeticions = 0;
    let elementAmbMesRepeticions = 0;

    // Busquem la lletrea amb més repeticions
    for (let element in comptador) {
        if (comptador[element] > maxRepeticions) {
            maxRepeticions = comptador[element];
            elementAmbMesRepeticions = element;
        }
    }

    return `La lletra: ${elementAmbMesRepeticions} ${maxRepeticions} apareix vegades`;
};


console.log(mostRepeated(arrayLletres));