<?php

require_once 'modelBase.php';

class Nota extends modelBase {

    private $nom;
    private $contingut;

    public function __construct() {
        parent::__construct();
    }

    /**
     * Retorna totes les notes de la taula 'notes'.
     * @return array
     */
    public function obtenirTotes() {
        return $this->aconseguirTots('notes'); 
    }

    public function desarNota() {
        // Escapem els valors per evitar SQL Injection
        $nom = $this->conn->real_escape_string($this->nom);
        $contingut = $this->conn->real_escape_string($this->contingut);
    
        // Consulta SQL per inserir una nova nota
        $sql = "INSERT INTO notes (nom, contingut) VALUES ('$nom', '$contingut')";
    
        // Executem
        $desat = $this->conn->query($sql);
    
        return $desat;
    }


    // Setters i getters
    public function getNom() {
        return $this->nom;
    }

    public function setNom($nom) {
        $this->nom = $nom;
    }

    public function getcontingut() {
        return $this->contingut;
    }

    public function setcontingut($contingut) {
        $this->contingut = $contingut;
    }
}
?>
