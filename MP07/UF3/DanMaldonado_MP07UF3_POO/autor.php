<?php

class Autor {
    private string $nom;
    private string $cognom;
    private array $llibres = [];

    public function __construct(string $nom, string $cognom) {
        $this->nom = $nom;
        $this->cognom = $cognom;
    }

    public function afegirLlibre(Llibre $llibre) {
        $this->llibres[] = $llibre;
    }

    public function mostrarLlibres() {
        echo "Llibres escrits per {$this->nomComplet()}:\n";
        foreach ($this->llibres as $llibre) {
            echo "- " . $llibre->__get("titol") . "\n";
        }
    }

    public function nomComplet(): string {
        return "{$this->nom} {$this->cognom}";
    }
}