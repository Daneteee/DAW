<?php

class Llibre {
    private string $titol;
    private Autor $autor;
    private string $isbn;
    private bool $disponible;

    public function __construct(string $titol, Autor $autor, string $isbn) {
        $this->titol = $titol;
        $this->autor = $autor;
        $this->isbn = $isbn;
        $this->disponible = true;
    }

    public function prestar() {
        if ($this->disponible) {
            $this->disponible = false;
        } else {
            echo "El llibre '{$this->titol}' no està disponible.\n";
        }
    }

    public function retornar() {
        $this->disponible = true;
    }

    public function info() {
        $disponibilitat = $this->disponible ? "Disponible" : "No disponible";
        echo "Títol: {$this->titol}, Autor: {$this->autor->nomComplet()}, Disponibilitat: {$disponibilitat}\n";
    }

    public function __get($propietat) {
    if (property_exists($this,$propietat)) {
        return $this->$propietat;
        };
    }
}