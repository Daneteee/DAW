import { Persona } from './persones';
import { Treballador } from './treballadors';
import { Cat } from './animals';
import { Dog } from './animals';
import { Bird } from './animals';

/**
 * Creem un array de 3 persones amb els seus noms i cognoms.
 */
const persones: Persona[] = [
    new Persona("Joe", "Doe"),
    new Persona("Jane", "Dane"),
    new Persona("George", "Smith")
];

/**
 * Llistem totes les persones del array i imprimim els seus noms complets a la consola.
 * 
 * @param persones - Un array de persones per llistar.
 */
function llistarPersones(persones: Persona[]): void {
    persones.forEach(persona => {
        console.log(persona.getFullName());
    });
}

/**
 * Creem un array de 3 treballadors amb els seus noms, cognoms, números de treballador i salaris.
 */
const treballadors: Treballador[] = [
    new Treballador("Pepe", "Viyuela", 1, 2500),
    new Treballador("Dan", "Maldonado", 2, 3000),
    new Treballador("Bon", "Dia", 3, 2800)
];

/**
 * Calculem la despesa total dels salaris dels treballadors.
 * 
 * Utilitzem la funció `reduce` per sumar els salaris de tots els treballadors.
 * 
 * @param treballadors - Un array de treballadors per calcular la despesa salarial.
 * @returns El total de les despeses salarials.
 */
function despesesSalarials(treballadors: Treballador[]): number {
    return treballadors.reduce((total, treballador) => total + treballador.getSou(), 0);
}

/**
 * Creem objectes per a cada tipus de mascota (gat, gos, ocell).
 */
const gat = new Cat(true);
const gos = new Dog(true);
const ocell = new Bird(true);

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
