// 4. Fes una calculadora demani 2  nombres per pantalla, i després demani l’operació aritmètica a realitzar (+ - * / %) 
// i finalment mostri amb una alerta el resultat.Fes una calculadora demani 2  nombres per pantalla, i després demani 
// l’operació aritmètica a realitzar (+ - * / %) i finalment mostri amb una alerta el resultat.

'use strict'

// Funció per demanar un nombre vàlid
function getNumber(missatge) {
    let number
    do {
        number = prompt(missatge)
        if (number !== null) {
            number = Number(number)
        } else {
            alert('ERROR: Introdueix un nombre vàlid.')
        }
    } while (isNaN(number))
    return number
}

// Funció de calculadora
function pregunta4() {

    let num1 = getNumber("Introdueix el primer nombre: ")
    let num2 = getNumber("Introdueix el segon nombre: ")
    let operacio = prompt("Introdueix l'operació a realitzar (+ - * / %): ")
    let resultat

    // Creem els condicionals corresponents
    switch (operacio) {
        case '+':
            resultat = num1 + num2
            break
        case '-':
            resultat = num1 - num2
            break
        case '*':
            resultat = num1 * num2
            break
        case '/':
            if (num2 == 0) {
                alert("Error: Divisió per zero.")
                return
            }
            resultat = num1 / num2
            break
        case '%':
            if (num2 == 0) {
                alert("Error: Divisió per zero.")
                return
            }
            resultat = num1 % num2
            break
        default:
            alert("Operació no vàlida.")
            return
    }

    // Mostra el resultat només si l'operació és vàlida
    alert(`El resultat de ${num1} ${operacio} ${num2} és ${resultat}.`)
}