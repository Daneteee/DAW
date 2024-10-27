// 1. Feu un programa que demani dos nombres i ens digui amb una alerta, si són iguals,o bé quin és el més gran i quin és el més petit. (feu el programa robust)
// Afegeix que si el nombres no són de tipus nombre o bé són negatius, que els torni a demanar. Ajuda isNaN();

'use strict'

// Funció que demana un nombre positiu al usuari
function getPositiveNumber(missatge) {
    let num
    do {
        num = prompt(missatge) 
        if (num !== null) {
            num = Number(num) 
        } else {
            alert('ERROR: Introdueix un nombre positiu') 
        }
      // Repeteix si el valor no és un nombre o és negatiu
    } while (isNaN(num) || num < 0) 
    return num 
}
 
// Funció principal que compara dos nombres
function pregunta1() {
    let num1, num2   

    let text

    // Sol·licitem els nombres
    num1 = getPositiveNumber("Introdueix el primer nombre: ") 
    num2 = getPositiveNumber("Introdueix el segon nombre: ") 
        
    // Mostrem un missatge segons la condició
    if (num1 === num2) {
        text = "Els nombres són iguals." 
    } else {
        text = num1 > num2 ? "El primer nombre és més gran." : "El segon nombre és més gran." 
    }

    // Mostrem el resultat
    alert(text) 
}
