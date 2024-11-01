"use strict";

const get_grades = () => {
    const grades = {}; 

    // Agafem els noms de les UFs, les hores i la nota
    for (let i = 0; i < 4; i++) {
        const uf_name = prompt(`Nom de la UF${i + 1}:`); 
        
        let hours = 0;
        do {
            hours = parseInt(prompt(`Hores corresponents a ${uf_name}:`), 10); 
        } while (isNaN(hours) || hours <= 0 || hours % 1 !== 0); 

        // Si les hores son decimals les arrodonim
        let grade = 0;
        do {
            grade = Math.round(parseFloat(prompt(`Nota corresponent a ${uf_name}:`))); 
        } while (isNaN(grade) || grade < 0 || grade > 10); 

        grades[uf_name] = {
            hours: hours,
            grade: grade
        };
    }

    return grades; 
};


// Agafem el literal
const get_literal = (grade) => {
    if (grade >= 9 && grade <= 10) {
        return 'A';
    } else if (grade >= 7 && grade < 9) {
        return 'B';
    } else if (grade >= 5 && grade < 7) {
        return 'C';
    } else {
        return 'D';
    }
};

// Creem entrades perque es vegi bonic
const get_entry = (grades) => {
    const entries = []; 

    // Iterem sobre les notes i generant l'array d'entries
    for (const uf in grades) {
        const grade = grades[uf].grade;
        const literal = get_literal(grade);
        const entryText = `La ${uf} te la nota ${grade} i el literal ${literal}`;
        entries.push(entryText); 
    }

    // Ordenem les entrades per nota
    entries.sort((a, b) => {
        return b.grade - a.grade; 
    });

    return entries; 
};

// Agafem la mitjana ponderada
const get_average = (grades) => {
    
    // Sumem les hores ponderades
    const weighted_hours = Object.keys(grades)
        .map(uf => grades[uf].hours * grades[uf].grade) // Creem l'array amb hores*nota
        .reduce((accumulator, current_value) => accumulator + current_value, 0); // Sumem els valos
    
    // Sumem totes les hores per tenir el total
    const total_hours = Object.keys(grades)
        .map(uf => grades[uf].hours) // Obtenim les hores totals
        .reduce((accumulator, current_value) => accumulator + current_value, 0); // Les sumem

    // Calculem la mitjana ponderada
    const weightedAverage = weighted_hours / total_hours;

    return weightedAverage; 
};


// Obtenim les notes i les entrades
const grades = get_grades();
const entries = get_entry(grades); /
const average = get_average(grades); 
const averageLiteral = get_literal(average); 


const results_div = document.getElementById('results');

// Mostrar les resultats
results_div.innerHTML = `
    <ul>
        ${entries.map(entry => `<li>${entry}</li>`).join('')}
    </ul>
    <p><strong>La mitjana ponderada es: ${average.toFixed(2)} que <br> correspon a ${averageLiteral}</strong></p>`;
