// Classe Persona
/**
 * Classe que representa una persona amb nom i cognom.
 * 
 * Inclou getters, setters i una funció per obtenir el nom complet de la persona (nom + cognom).
 */
export class Persona {
    private nom: string;
    private cognom: string;

    /**
     * Constructor que inicialitza una nova instància de la classe Persona.
     * 
     * @param nom - El nom de la persona.
     * @param cognom - El cognom de la persona.
     */
    constructor(nom: string, cognom: string) {
        this.nom = nom;
        this.cognom = cognom;
    }

    /**
     * Obtenim el nom de la persona.
     * 
     * @returns El nom de la persona.
     */
    public getNom(): string {
        return this.nom;
    }

    /**
     * Establim el nom de la persona.
     * 
     * @param nom - El nou nom per assignar a la persona.
     */
    public setNom(nom: string): void {
        this.nom = nom;
    }

    /**
     * Obtenim el cognom de la persona.
     * 
     * @returns El cognom de la persona.
     */
    public getCognom(): string {
        return this.cognom;
    }

    /**
     * Establim el cognom de la persona.
     * 
     * @param cognom - El nou cognom per assignar a la persona.
     */
    public setCognom(cognom: string): void {
        this.cognom = cognom;
    }

    /**
     * Obté el nom complet de la persona (nom + cognom).
     * 
     * @returns El nom complet de la persona.
     */
    public getFullName(): string {
        return `${this.nom} ${this.cognom}`;
    }
}
