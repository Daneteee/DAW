"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.Treballador = void 0;
var persones_1 = require("./persones");
/**
 *Classe que representa un treballador, hereta de persona y té un número de treballador i un sou.
 *
 */
var Treballador = /** @class */ (function (_super) {
    __extends(Treballador, _super);
    /**
     * Constructor que inicialitza una nova instància de la classe Treballador.
     *
     * @param nom - El nom de la persona.
     * @param cognom - El cognom de la persona.
     * @param numeroTreballador - El número d'identificació del treballador.
     * @param sou - El sou del treballador.
     */
    function Treballador(nom, cognom, numeroTreballador, sou) {
        var _this = _super.call(this, nom, cognom) || this;
        _this.numeroTreballador = numeroTreballador;
        _this.sou = sou;
        return _this;
    }
    /**
     * Obtenim el número de treballador.
     *
     * @returns El número de treballador.
     */
    Treballador.prototype.getNumeroTreballador = function () {
        return this.numeroTreballador;
    };
    /**
     * Establim el número de treballador.
     *
     * @param numero - El nou número de treballador per assignar.
     */
    Treballador.prototype.setNumeroTreballador = function (numero) {
        this.numeroTreballador = numero;
    };
    /**
     * Obtenim el sou del treballador.
     *
     * @returns El sou del treballador.
     */
    Treballador.prototype.getSou = function () {
        return this.sou;
    };
    /**
     * Establim el sou del treballador.
     *
     * @param sou - El nou sou per assignar al treballador.
     */
    Treballador.prototype.setSou = function (sou) {
        this.sou = sou;
    };
    return Treballador;
}(persones_1.Persona));
exports.Treballador = Treballador;
