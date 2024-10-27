/**
 * Inserta guions entre les xifres parells consecutives d'un nombre.
 *
 * Aquesta funció accepta un nombre enter, el converteix a cadena, i insereix
 * guions entre xifres parells consecutives. Si el nombre no és vàlid
 * (no és un nombre o és menor o igual a zero), retorna un
 * missatge d'error.
 *
 * @param {number} num - El nombre enter al qual es volen inserir guions.
 * @returns {string} - La cadena resultant amb els guions inserits o un
 *                     missatge d'error si el nombre no és vàlid.
 *
 * @example
 * posaGuionsEntreParells(225468); // Retorna "2-254-6-8"
 * posaGuionsEntreParells(8675309); // Retorna "8-675309"
 */

const posaGuionsEntreParells = num => {

    if (!isNaN(num) && num > 0) {
        let numStr = num.toString()
        let resultat = ""

        for (let i = 0; i < numStr.length; i++) {
            resultat += numStr[i]

            if (numStr[i] % 2 === 0 && numStr[i + 1] % 2 === 0) {
                resultat += "-"  
            }
        }

        return resultat

    } else {
        return "ERROR: El nombre no és vàlid"
    }
}

console.log(posaGuionsEntreParells(225468))
console.log(posaGuionsEntreParells("8675343241234134142134309"))

