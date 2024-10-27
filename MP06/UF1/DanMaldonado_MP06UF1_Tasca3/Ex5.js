/**
 * Script que genera un array de 100 elements amb dades aleatòries seguint les següents premisses:
 * - Imports aleatoris entre 1 i 1000
 * - IVA aleatori del 10% o 21%
 * - Quantitats aleatòries entre 1 i 10
 * 
 * També genera els següents arrays:
 * - Imports finals ((Preu unitari + IVA) * Unitats)
 * - IVA (Preu unitari * IVA)
 * - PVP unitari amb IVA (Preu unitari + IVA)
 * 
 * A més, calcula:
 * - Import total
 * - Import total de l'IVA, desglossat per IVA del 10% i 21%
 */

const getRandom = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

// Generem l'array de nombres random
function generateRandomData() {
    const dataArray = [];

    for (let i = 0; i < 100; i++) {
        const unitPrice = getRandom(1, 1000); 
        const units = getRandom(1, 10); 
        const iva = getRandom(0, 1) === 0 ? 0.10 : 0.21; 
        
        dataArray.push([unitPrice, units, iva]);
    }
    
    return dataArray;
}

//  Generar un array amb els imports finals ((Preu unitari + IVA) * Unitats), 
function finalPrice(data_array) {
    finalPriceArray = [];
    for (let i = 0; i < data_array.length; i++) {
        const priceWithIVA = (data_array[i][0] + data_array[i][0] * data_array[i][2]) * data_array[i][1];
        finalPriceArray.push(priceWithIVA.toFixed(2));
    }
    return finalPriceArray;
}

//  Generi un array amb l’IVA (Preu unitari * IVA)
function generateIVAarray(data_array) {
    arrayIVA = [];
    for (let i = 0; i < data_array.length; i++) {
        const ivaAmount = data_array[i][0] * data_array[i][2];
        arrayIVA.push(ivaAmount.toFixed(2));
    }
    return arrayIVA;
}

//  Generi un array amb el PVP unitari amb IVA (Preu Unitari + IVA)
function generatePVPIVA(data_array) {
    PVParray = [];
    for (let i = 0; i < data_array.length; i++) {
        const pvp = data_array[i][0] + (data_array[i][0] * data_array[i][2]);
        PVParray.push(pvp.toFixed(2));
    }
    return arrayIVA;
}

// Calculem l’import total 
const generateTotal = data_array => data_array.reduce((total, current) => total + parseFloat(current), 0).toFixed(2);

// Calculem l'IVA total desglosat
function calculateTotalIVA(data_array) {
    let totalIVA = 0;
    let iva10 = 0;
    let iva21 = 0;

    for (let i = 0; i < data_array.length; i++) {
        const ivaAmount = data_array[i][0] * data_array[i][2]; 
        totalIVA += ivaAmount;

        if (data_array[i][2] === 0.10) {
            iva10 += ivaAmount;
        } else if (data_array[i][2] === 0.21) {
            iva21 += ivaAmount;
        }
    }
    return [totalIVA.toFixed(2), iva10.toFixed(2), iva21.toFixed(2)];
}


// Creem l'array
const randomArray = generateRandomData();


// Mostrem els resultats
console.log("Preu final: ", finalPrice(randomArray));
console.log("Array amb IVA: ", generateIVAarray(randomArray));
console.log("PVP unitari amb IVA: ", generatePVPIVA(randomArray));

const finalPricesArray = finalPrice(randomArray);
console.log("Import total: ", generateTotal(finalPricesArray));

const totalIVA = calculateTotalIVA(randomArray);
console.log("Import total IVA: ", totalIVA[0]);
console.log("IVA al 10%: ", totalIVA[1]);
console.log("IVA al 21%: ", totalIVA[2]);