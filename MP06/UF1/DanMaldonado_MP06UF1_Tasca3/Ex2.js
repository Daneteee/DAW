/**
 * Funcions per treballar amb un array numèric utilitzant funcions de fletxa.
 * 
 * Aquesta sèrie de funcions realitza les següents operacions sobre un array de nombres:
 * 
 * 1. **oddNumbers**: Retorna un array amb tots els nombres senars.
 * 2. **average**: Retorna la average de tots els elements de l'array.
 * 3. **biggest**: Retorna el valor més gran de l'array.
 * 4. **smallest**: Retorna el valor més petit de l'array.
 * 
 * @param {number[]} num_array - L'array numèric sobre el qual s'aplicaran les funcions.
 * 
 * @returns {void} - Aquesta funció no retorna cap valor, però imprimeix els resultats 
 * al consola de manera estructurada.
 * 
 * Exemple d'ús:
 *  - Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 *  - Output:
 *    - Nombres senars: [1, 3, 5, 7, 9]
 *    - average: 5.5
 *    - Més gran: 10
 *    - Més petit: 1
 */


// Fes una funció en javascript que donat un array numèric, i utilitzant funcions de fletxa:

const numericArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//      => una funció que mostra quins nombres senars hi ha
const oddNumbers = (num_array) => {
    return num_array.filter(num => num % 2 !== 0);
}

//      => una funció que  retorna la average de tots els elements de l’array
const average = (num_array) => {
    let suma = num_array.reduce((c, num) => c + num, 0);
    return suma / num_array.length;
}

//      => una funció que retorna el més gran
const biggest = (num_array) => Math.max(...num_array);

//      => una funció que retorna el més petit
const smallest = (num_array) => Math.min(...num_array);


// Funció que executa totes les operacions i mostra els resultats
function executeFunctions(num_array) {
    console.log("Nombres senars: " + oddNumbers(num_array));
    console.log("Mitjana: " + average(num_array));
    console.log("Més gran: " + biggest(num_array));
    console.log("Més petit: " + smallest(num_array));
}

// Executem les operacions
executeFunctions(numericArray);