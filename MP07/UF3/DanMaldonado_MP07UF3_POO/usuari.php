<?php

class Usuari {
    private string $nom;
    private string $cognom;
    private array $llibresPrestats = [];

    public function __construct(string $nom, string $cognom) {
        $this->nom = $nom;
        $this->cognom = $cognom;
    }

    public function prestarLlibre(Llibre $llibre) {
        if ($llibre->__get("disponible")) {
            $llibre->prestar();
            $this->llibresPrestats[] = $llibre;
            echo "Llibre prestat: " . $llibre->__get("titol") . "\n";
        } else {
            echo "El llibre '{$llibre->__get("titol")}' no està disponible.\n";
        }
    }

    public function retornarLlibre(Llibre $llibre) {
        foreach ($this->llibresPrestats as $index => $prestat) {
            if ($prestat === $llibre) {
                $llibre->retornar();
                unset($this->llibresPrestats[$index]);
                echo "Llibre retornat: " . $llibre->__get("titol") . "\n";
                return;
            }
        }
        echo "Aquest llibre no està a la teva llista de préstecs.\n";
    }

    public function mostrarLlibresPrestats() {
        echo "Llibres prestats per {$this->nom} {$this->cognom}:\n";
        foreach ($this->llibresPrestats as $llibre) {
            echo "- " . $llibre->__get("titol") . "\n";
        }
    }
} 