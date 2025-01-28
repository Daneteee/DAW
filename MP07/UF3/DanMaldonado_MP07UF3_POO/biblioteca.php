<?php

class Biblioteca {
    private array $cataleg;

    public function __construct() {
        $this->cataleg = [];
    }

    public function afegirLlibre(Llibre $llibre) {
        $this->cataleg[] = $llibre;
    }

    public function eliminarLlibre(Llibre $llibre) {
        foreach ($this->cataleg as $index => $llibreCataleg) {
            if ($llibreCataleg === $llibre) {
                unset($this->cataleg[$index]);
                echo "Llibre eliminat del catàleg: " . $llibre->__get("titol") . "\n";
                return;
            }
        }
        echo "El llibre no es troba al catàleg.\n";
    }

    public function mostrarCataleg() {
        echo "Catàleg de la biblioteca:\n";
        foreach ($this->cataleg as $llibre) {
            $llibre->info();
        }
    }
}