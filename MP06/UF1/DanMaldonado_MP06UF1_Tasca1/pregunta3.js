// 3. Mostra per pantalla la taula de multiplicar d’un nombre que l’usuari introdueix per teclat. 
// El nombre ha de ser positiu i entre l’1 i el 10.

'use strict'

function getNumberInRange(missatge, min, max) {
    let number
    do {
        number = prompt(missatge) 
        if (number !== null) {
            number = Number(number) 
        } else {
            alert('ERROR: Introdueix un nombre vàlid.') 
        }
      // Comprova que el nombre estigui dins del rang especificat
    } while (isNaN(number) || number < min || number > max) 
    return number 
}

function pregunta3() {
    let num = getNumberInRange("Introdueix un nombre entre 1 i 10: ", 1, 10)
    let result = ""
    for (let i = 1; i <= 10; i++) {
        result += `${num} x ${i} = ${num * i}\n`
    }
    alert(result)
    
}