import { Persona } from './persones';

/**
 *Classe que representa un treballador, hereta de persona y té un número de treballador i un sou.
 * 
 */
export class Treballador extends Persona {
    private numeroTreballador: number;
    private sou: number;

    /**
     * Constructor que inicialitza una nova instància de la classe Treballador.
     * 
     * @param nom - El nom de la persona.
     * @param cognom - El cognom de la persona.
     * @param numeroTreballador - El número d'identificació del treballador.
     * @param sou - El sou del treballador.
     */
    constructor(nom: string, cognom: string, numeroTreballador: number, sou: number) {
        super(nom, cognom);
        this.numeroTreballador = numeroTreballador;
        this.sou = sou;
    }

    /**
     * Obtenim el número de treballador.
     * 
     * @returns El número de treballador.
     */
    public getNumeroTreballador(): number {
        return this.numeroTreballador;
    }

    /**
     * Establim el número de treballador.
     * 
     * @param numero - El nou número de treballador per assignar.
     */
    public setNumeroTreballador(numero: number): void {
        this.numeroTreballador = numero;
    }

    /**
     * Obtenim el sou del treballador.
     * 
     * @returns El sou del treballador.
     */
    public getSou(): number {
        return this.sou;
    }

    /**
     * Establim el sou del treballador.
     * 
     * @param sou - El nou sou per assignar al treballador.
     */
    public setSou(sou: number): void {
        this.sou = sou;
    }
}
