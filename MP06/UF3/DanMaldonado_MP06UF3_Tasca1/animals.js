"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Bird = exports.Dog = exports.Cat = void 0;
/**
 * Classe gat que implementa la interfície Pet.
 *
 * Afegim una propietat per saber si el gat està "miolant" i implementem les accions
 * de menjar i dormir.
 */
var Cat = /** @class */ (function () {
    /**
     * Constructor que inicialitza un gat amb l'estat de "miolar".
     *
     * @param mew - Indica si el gat està miolant.
     */
    function Cat(mew) {
        this.mew = mew;
    }
    /**
     * La funció de menjar per al gat.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que el gat està menjant.
     */
    Cat.prototype.eat = function () {
        console.log("El gat està menjant.");
    };
    /**
     * La funció de dormir per al gat.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que el gat està dormint.
     */
    Cat.prototype.sleep = function () {
        console.log("El gat està dormint.");
    };
    /**
     * Obtenim l'estat de si el gat està miolant.
     *
     * @returns Verdader si el gat està miolant, fals si no ho està.
     */
    Cat.prototype.isMewing = function () {
        return this.mew;
    };
    return Cat;
}());
exports.Cat = Cat;
/**
 * Classe gos que implementa la interfície Pet.
 *
 * Afegim una propietat per saber si el gos està "lladrant" i implementem les accions
 * de menjar i dormir.
 */
var Dog = /** @class */ (function () {
    /**
     * Constructor que inicialitza un gos amb l'estat de "lladrar".
     *
     * @param bark - Indica si el gos està lladrant.
     */
    function Dog(bark) {
        this.bark = bark;
    }
    /**
     * La funció de menjar per al gos.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que el gos està menjant.
     */
    Dog.prototype.eat = function () {
        console.log("El gos està menjant.");
    };
    /**
     * La funció de dormir per al gos.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que el gos està dormint.
     */
    Dog.prototype.sleep = function () {
        console.log("El gos està dormint.");
    };
    /**
     * Obtenim l'estat de si el gos està lladrant.
     *
     * @returns Verdader si el gos està lladrant, fals si no ho està.
     */
    Dog.prototype.isBarking = function () {
        return this.bark;
    };
    return Dog;
}());
exports.Dog = Dog;
/**
 * Classe ocell que implementa la interfície Pet.
 *
 * Afegim una propietat per saber si l'ocell està "piulant" i implementem les accions
 * de menjar i dormir.
 */
var Bird = /** @class */ (function () {
    /**
     * Constructor que inicialitza un ocell amb l'estat de "piular".
     *
     * @param tweet - Indica si l'ocell està piulant.
     */
    function Bird(tweet) {
        this.tweet = tweet;
    }
    /**
     * La funció de menjar per a l'ocell.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que l'ocell està menjant.
     */
    Bird.prototype.eat = function () {
        console.log("L'ocell està menjant.");
    };
    /**
     * La funció de dormir per a l'ocell.
     *
     * Aquesta funció imprimeix en consola un missatge indicant que l'ocell està dormint.
     */
    Bird.prototype.sleep = function () {
        console.log("L'ocell està dormint.");
    };
    /**
     * Obtenim l'estat de si l'ocell està piulant.
     *
     * @returns Verdader si l'ocell està piulant, fals si no ho està.
     */
    Bird.prototype.isTweeting = function () {
        return this.tweet;
    };
    return Bird;
}());
exports.Bird = Bird;
