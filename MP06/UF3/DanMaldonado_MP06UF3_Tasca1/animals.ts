/**
 * Aquesta interfície defineix les accions bàsiques d'una mascota.
 * 
 * Les mascotes han de poder menjar i dormir.
 */
export interface Pet {
    eat(): void;
    sleep(): void;
}

/**
 * Classe gat que implementa la interfície Pet.
 * 
 * Afegim una propietat per saber si el gat està "miolant" i implementem les accions
 * de menjar i dormir.
 */
export class Cat implements Pet {
    private mew: boolean;

    /**
     * Constructor que inicialitza un gat amb l'estat de "miolar".
     * 
     * @param mew - Indica si el gat està miolant.
     */
    constructor(mew: boolean) {
        this.mew = mew;
    }

    /**
     * La funció de menjar per al gat.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que el gat està menjant.
     */
    public eat(): void {
        console.log("El gat està menjant.");
    }

    /**
     * La funció de dormir per al gat.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que el gat està dormint.
     */
    public sleep(): void {
        console.log("El gat està dormint.");
    }

    /**
     * Obtenim l'estat de si el gat està miolant.
     * 
     * @returns Verdader si el gat està miolant, fals si no ho està.
     */
    public isMewing(): boolean {
        return this.mew;
    }
}

/**
 * Classe gos que implementa la interfície Pet.
 * 
 * Afegim una propietat per saber si el gos està "lladrant" i implementem les accions
 * de menjar i dormir.
 */
export class Dog implements Pet {
    private bark: boolean;

    /**
     * Constructor que inicialitza un gos amb l'estat de "lladrar".
     * 
     * @param bark - Indica si el gos està lladrant.
     */
    constructor(bark: boolean) {
        this.bark = bark;
    }

    /**
     * La funció de menjar per al gos.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que el gos està menjant.
     */
    public eat(): void {
        console.log("El gos està menjant.");
    }

    /**
     * La funció de dormir per al gos.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que el gos està dormint.
     */
    public sleep(): void {
        console.log("El gos està dormint.");
    }

    /**
     * Obtenim l'estat de si el gos està lladrant.
     * 
     * @returns Verdader si el gos està lladrant, fals si no ho està.
     */
    public isBarking(): boolean {
        return this.bark;
    }
}

/**
 * Classe ocell que implementa la interfície Pet.
 * 
 * Afegim una propietat per saber si l'ocell està "piulant" i implementem les accions
 * de menjar i dormir.
 */
export class Bird implements Pet {
    private tweet: boolean;

    /**
     * Constructor que inicialitza un ocell amb l'estat de "piular".
     * 
     * @param tweet - Indica si l'ocell està piulant.
     */
    constructor(tweet: boolean) {
        this.tweet = tweet;
    }

    /**
     * La funció de menjar per a l'ocell.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que l'ocell està menjant.
     */
    public eat(): void {
        console.log("L'ocell està menjant.");
    }

    /**
     * La funció de dormir per a l'ocell.
     * 
     * Aquesta funció imprimeix en consola un missatge indicant que l'ocell està dormint.
     */
    public sleep(): void {
        console.log("L'ocell està dormint.");
    }

    /**
     * Obtenim l'estat de si l'ocell està piulant.
     * 
     * @returns Verdader si l'ocell està piulant, fals si no ho està.
     */
    public isTweeting(): boolean {
        return this.tweet;
    }
}
