<?php
// Classe Llibre
class Llibre {
    private $titol;
    private $autor;
    private $isbn;
    private $disponible;

    public function __construct($titol, Autor $autor, $isbn) {
        $this->titol = $titol;
        $this->autor = $autor;
        $this->isbn = $isbn;
        $this->disponible = true;
    }

    // Prèstec d'un llibre
    public function prestar() {
        $this->disponible = false;
    }

    // Retornem un llibre
    public function retornar() {
        $this->disponible = true;
    }

    // Informació sobre el llibre
    public function info() {
        return "Títol: {$this->titol}, Autor: {$this->autor->nomComplet()}, Disponible: " . ($this->disponible ? 'Sí' : 'No');
    }

    // Mostrem si el llibre está disponible per préstec
    public function estaDisponible() {
        return $this->disponible;
    }
}