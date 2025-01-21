<?php

require_once 'modelBase.php';

// Classe usuari
class Usuari extends modelBase{
    private $nom;
    private $cognom;
    private $llibres_prestats;

    public function __construct($nom, $cognom) {
        $this->nom = $nom;
        $this->cognom = $cognom;
        $this->llibres_prestats = array();
    }

    // Fem el préstec d'un llibre
    public function prestarLlibre($llibre) {
        if ($llibre->estaDisponible()) {
            $this->llibres_prestats[] = $llibre;
            $llibre->prestar();
            echo "Llibre prestat: {$llibre->info()}\n";
        } else {
            echo "El llibre no està disponible per prestar.";
        }
    }

    // Retornem un llibre
    public function retornarLlibre($llibre) {
        $index = array_search($llibre, $this->llibres_prestats);
        if ($index !== false) {
            unset($this->llibres_prestats[$index]);
            $llibre->retornar();
            echo "Llibre retornat: {$llibre->info()}\n";
        } else {
            echo "No tens aquest llibre prestat.";
        }
    }

    // Llibres prestats
    public function mostrarLlibresPrestats() {
        echo "Llibres prestats per {$this->nom} {$this->cognom}:\n";
        foreach ($this->llibres_prestats as $llibre) {
            echo "- {$llibre->info()}\n";
        }
    }

}