// 2. Utilitzant un bucle demana a l’usuari  nombres introduïts per teclat fins que introdueix un nombre negatiu. 
// És a dir, l’usuari anirà introduint nombres, fins que introdueix un nombre negatiu. Finalment mostra la mitjana i 
// l’acumulat de tots els nombres positius;

'use strict'

// Funció que valida un nombre
function getNumber(missatge) {
    let number
    do {
        number = prompt(missatge)
        if (number !== null) {
            number = Number(number)
        } else {
            alert('ERROR: Introdueix un nombre vàlid.')
        }
    } while (isNaN(number) || number == 0)
    return number
}

// Funció principal
function pregunta2() {
    let c = 0
    let num
    let suma = 0
    let mitjana

    // Bucle on demanem nombres fins introduïr un nombre negatiu
    do {
        num = getNumber("Introdueix un nombre (negatiu per acabar): ")
        // En cas que sigui 0 no sumem ni actualitzem el comptador
        if (num > 0) {
            suma += num
            c += 1
        }
    } while (num > 0)
    
    mitjana = suma/c

    alert(`La mitjana és ${mitjana}.\nL'acumulat és ${suma}`)
}
