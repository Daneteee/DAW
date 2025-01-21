<?php

require_once 'modelBase.php';

class Nota extends modelBase {

    private $nom;
    private $titol;

    public function __construct($host, $dbname, $user, $password) {
        parent::__construct($host, $dbname, $user, $password);
    }

    /**
     * Retorna totes les notes de la taula 'notes'.
     * @return array
     */
    public function obtenirTotes() {
        return $this->aconseguirTots('notes'); // Especifica la taula 'notes'
    }

    public function getNom() {
        return $this->nom;
    }

    public function setNom($nom) {
        $this->nom = $nom;
    }

    public function getTitol() {
        return $this->titol;
    }

    public function setTitol($titol) {
        $this->titol = $titol;
    }
}
?>
