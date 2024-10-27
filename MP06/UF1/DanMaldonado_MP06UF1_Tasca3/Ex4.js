/**
 * Programa que gestiona un array de números introduïts per l'usuari amb diverses funcionalitats:
 * 
 * 1. Demana 6 números per teclat i els emmagatzema en un array.
 * 2. Mostra tots els elements de l'array en el document HTML com una llista desordenada 
 *    (usant `forEach`) i també en la consola.
 * 3. Ordena l'array numèricament i el mostra.
 * 4. Inverteix l'array i el mostra.
 * 5. Mostra quants elements té l'array.
 * 6. Permet cercar un value introduït per l'usuari i retorna l'índex d'aquest value en l'array.
 * 
 * Exemples d'entrada per fer les proves: 1000, 101, 121, 13, 15, 11111
 */

// Demanem un nombre vàlid
function inputValidNum(message) {
    let num;
    do {
        num = prompt(message);
    } while (isNaN(num) || num === null); 
    return Number(num); 
}

// Funció per crear un array de nombres vàlids
function validNumArray(message, quantitat) {
    let nums = []; 
    for (let i = 0; i < quantitat; i++) {
        let num = inputValidNum(message);
        nums.push(num); 
    }
    return nums; 
}

//Mostrem l'array a una llista desordenada
function showArray(nums) {
    document.write("<ul>"); 
    nums.forEach(num => {
        document.write(`<li>${num}</li>`); 
    });
    document.write("</ul>"); 
    console.log(nums);
}

// Busquem l'índex d'un valor
function searchValue(nums, value) {
    let index = nums.indexOf(value); 
    return index; 
}

// Mostrem l'array original
let num_array = validNumArray("Introdueix un nombre: ", 6);
document.write("<h2>Array original</h2>");
showArray(num_array);

// Creem una còpia de num_array i l'ordenem
let arrangedArray = [...num_array].sort((a, b) => a - b);
document.write("<h2>Array ordenada</h2>");
showArray(arrangedArray); 

// Revertir l'array original
let invertedArray = [...num_array].reverse();
document.write("<h2>Array al revés de l'ORIGINAL</h2>");
showArray(invertedArray); 

// Mostrem quants elements té l'array
document.write(`<p>El nombre d'elements en l'array és: ${num_array.length}</p>`);

value = inputValidNum("Introdueix un valor a cercar: ");
let index = searchValue(num_array, value);
if (index === -1) {
    document.write(`<p>El valor ${value} no s'ha trobat en l'array.</p>`);
} else {
    document.write(`<p>El valor ${value} s'ha trobat a l'índex ${index} de l'array ORIGINAL.</p>`);
}