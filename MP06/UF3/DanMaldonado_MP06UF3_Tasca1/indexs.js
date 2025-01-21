"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var persones_1 = require("./persones");
var treballadors_1 = require("./treballadors");
var animals_1 = require("./animals");
var animals_2 = require("./animals");
var animals_3 = require("./animals");
/**
 * Creem un array de 3 persones amb els seus noms i cognoms.
 */
var persones = [
    new persones_1.Persona("Joe", "Doe"),
    new persones_1.Persona("Jane", "Dane"),
    new persones_1.Persona("George", "Smith")
];
/**
 * Llistem totes les persones del array i imprimim els seus noms complets a la consola.
 *
 * @param persones - Un array de persones per llistar.
 */
function llistarPersones(persones) {
    persones.forEach(function (persona) {
        console.log(persona.getFullName());
    });
}
/**
 * Creem un array de 3 treballadors amb els seus noms, cognoms, números de treballador i salaris.
 */
var treballadors = [
    new treballadors_1.Treballador("Pepe", "Viyuela", 1, 2500),
    new treballadors_1.Treballador("Dan", "Maldonado", 2, 3000),
    new treballadors_1.Treballador("Bon", "Dia", 3, 2800)
];
/**
 * Calculem la despesa total dels salaris dels treballadors.
 *
 * Utilitzem la funció `reduce` per sumar els salaris de tots els treballadors.
 *
 * @param treballadors - Un array de treballadors per calcular la despesa salarial.
 * @returns El total de les despeses salarials.
 */
function despesesSalarials(treballadors) {
    return treballadors.reduce(function (total, treballador) { return total + treballador.getSou(); }, 0);
}
/**
 * Creem objectes per a cada tipus de mascota (gat, gos, ocell).
 */
var gat = new animals_1.Cat(true);
var gos = new animals_2.Dog(true);
var ocell = new animals_3.Bird(true);
/**
 * Provem totes les funcionalitats definides:
 * - Llistem les persones i mostrem els seus noms complets.
 * - Calculem i imprimim les despeses salarials.
 * - Mostrem les accions de menjar, dormir i l'estat de cada mascota (miolar, lladrar, piular).
 */
console.log("Persones:");
llistarPersones(persones);
console.log("\nDespesa salarial:", despesesSalarials(treballadors));
console.log("\nMascotes:");
console.log("Gat:");
gat.eat();
gat.sleep();
console.log("Està miolant:", gat.isMewing());
console.log("\nGos:");
gos.eat();
gos.sleep();
console.log("Està llandrant:", gos.isBarking());
console.log("\nOcell:");
ocell.eat();
ocell.sleep();
console.log("Està piolant:", ocell.isTweeting());
