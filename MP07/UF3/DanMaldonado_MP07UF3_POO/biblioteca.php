<?php

// Classe Biblioteca
class Biblioteca {

    public $cataleg;

    public function __construct() {
        $this->cataleg = array();
    }

    // Afegim llibre
    public function afegirLlibre($llibre) {
        $this->cataleg[] = $llibre;
    }

    // Eliminem llibre
    public function eliminarLlibre($llibre) {
        $index = array_search($llibre, $this->cataleg);
        if ($index !== false) {
            unset($this->cataleg[$index]);
        }
    }

    // Mostrem el catàleg
    public function mostrarCataleg() {
        foreach ($this->cataleg as $llibre) {
            echo $llibre->mostrarInformacio() . "<br>";
        }
    }
}