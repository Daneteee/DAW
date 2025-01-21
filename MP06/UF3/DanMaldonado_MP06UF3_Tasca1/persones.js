"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Persona = void 0;
// Classe Persona
/**
 * Classe que representa una persona amb nom i cognom.
 *
 * Inclou getters, setters i una funció per obtenir el nom complet de la persona (nom + cognom).
 */
var Persona = /** @class */ (function () {
    /**
     * Constructor que inicialitza una nova instància de la classe Persona.
     *
     * @param nom - El nom de la persona.
     * @param cognom - El cognom de la persona.
     */
    function Persona(nom, cognom) {
        this.nom = nom;
        this.cognom = cognom;
    }
    /**
     * Obtenim el nom de la persona.
     *
     * @returns El nom de la persona.
     */
    Persona.prototype.getNom = function () {
        return this.nom;
    };
    /**
     * Establim el nom de la persona.
     *
     * @param nom - El nou nom per assignar a la persona.
     */
    Persona.prototype.setNom = function (nom) {
        this.nom = nom;
    };
    /**
     * Obtenim el cognom de la persona.
     *
     * @returns El cognom de la persona.
     */
    Persona.prototype.getCognom = function () {
        return this.cognom;
    };
    /**
     * Establim el cognom de la persona.
     *
     * @param cognom - El nou cognom per assignar a la persona.
     */
    Persona.prototype.setCognom = function (cognom) {
        this.cognom = cognom;
    };
    /**
     * Obté el nom complet de la persona (nom + cognom).
     *
     * @returns El nom complet de la persona.
     */
    Persona.prototype.getFullName = function () {
        return "".concat(this.nom, " ").concat(this.cognom);
    };
    return Persona;
}());
exports.Persona = Persona;
