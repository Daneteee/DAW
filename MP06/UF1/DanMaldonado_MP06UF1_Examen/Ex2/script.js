"use strict";

// Inicialitzem variables
const text_elements = document.querySelectorAll("p");
const vowels = ['a', 'e', 'i', 'o', 'u'];

// Guardem el text original de cada element a una nova array
let original_text = Array.from(text_elements).map(element => element.innerText);


// Utilitzem una funció fletxa per reemplaçar les lletres
const replace_vowels = (letter) => {
    // Iterem sobre cada element de text_elements
    for (let i = 0; i < text_elements.length; i++) {
        let text = text_elements[i].innerText;

        // Utilitzem Array.map per transformar cada caràcter del text
        // Primerament, convertim la cadena de text en un array de caràcters, després utilitzem un map per aplicar
        // la funció de reemplaçar vocals si és una vocal, o retornar el caràcter original si no és una vocal
        let newText = Array.from(text).map((char) => {
            // Si el caràcter és una vocal, el canviem per la lletra escollida
            if (vowels.includes(char.toLowerCase())) {
                return letter; 
            } else {
                return char; 
            }
        // Finalment, unim els caràcters transformats en una nova cadena
        }).join(""); 

        // Actualitzem el text de l'element amb el nou text
        text_elements[i].innerText = newText;
    }
};



// Restaurem el text original
const reset_text = () => {
    // Restaurem cada element del text per l'element original
    for (let i = 0; i < text_elements.length; i++) {
        text_elements[i].innerText = original_text[i]; 
    }
};
