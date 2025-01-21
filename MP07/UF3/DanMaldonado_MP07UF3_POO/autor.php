<?php

class Autor {
    private $nom;
    private $cognom;
    private $llibres;

    public function __construct($nom, $cognom) {
        $this->nom = $nom;
        $this->cognom = $cognom;
        $this->llibres = array();
    }

    // Afegir un llibre a l'autor
    public function afegirLlibre($llibre) {
        $this->llibres[] = $llibre;
    }

    // Mostrem els llibres que ha publicat l'autor
    public function mostrarLlibres() {
        echo "Llibres de " . $this->nom . " " . $this->cognom . ":<br>";
        foreach ($this->llibres as $llibre) {
            echo "- " . $llibre->getTitol() . "<br>";
        }
    }

    // Nom complet de l'autor
    public function nomComplet() {
        return "{$this->nom} {$this->cognom}";
    }
}