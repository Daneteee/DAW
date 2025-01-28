<?php

require_once 'modelBase.php';

class Usuari extends modelBase {
    private $nom;
    private $cognoms;
    private $email;
    private $password;

    public function __construct() {
        parent::__construct();
    }

    /**
     * Obtenim tots els usuaris de la taula 'usuaris'.
     * @return array
     */
    public function obtenirTots() {
        return $this->aconseguirTots('usuaris'); 
    }


    // Setters i getters
    public function getNom() {
        return $this->nom;
    }

    public function setNom($nom) {
        $this->nom = $nom;
        return $this;
    }

    public function getCognoms() {
        return $this->cognoms;
    }

    public function setCognoms($cognoms) {
        $this->cognoms = $cognoms;
        return $this;
    }

    public function getEmail() {
        return $this->email;
    }

    public function setEmail($email) {
        $this->email = $email;
        return $this;
    }

    public function getPassword() {
        return $this->password;
    }

    public function setPassword($password) {
        $this->password = $password;
        return $this;
    }
}
?>
