<?php

require_once 'modelBase.php';

class Usuari extends modelBase {
    private $nom;
    private $cognoms;
    private $email;
    private $password;

    public function __construct($host, $dbname, $user, $password) {
        parent::__construct($host, $dbname, $user, $password);
    }

    /**
     * Obtenir tots els usuaris de la taula 'usuaris'.
     * @return array
     */
    public function obtenirTots() {
        return $this->aconseguirTots('usuaris'); // Especifica la taula 'usuaris'
    }

    /**
     * Get the value of nom
     */
    public function getNom() {
        return $this->nom;
    }

    /**
     * Set the value of nom
     */
    public function setNom($nom) {
        $this->nom = $nom;
        return $this;
    }

    /**
     * Get the value of cognoms
     */
    public function getCognoms() {
        return $this->cognoms;
    }

    /**
     * Set the value of cognoms
     */
    public function setCognoms($cognoms) {
        $this->cognoms = $cognoms;
        return $this;
    }

    /**
     * Get the value of email
     */
    public function getEmail() {
        return $this->email;
    }

    /**
     * Set the value of email
     */
    public function setEmail($email) {
        $this->email = $email;
        return $this;
    }

    /**
     * Get the value of password
     */
    public function getPassword() {
        return $this->password;
    }

    /**
     * Set the value of password
     */
    public function setPassword($password) {
        $this->password = $password;
        return $this;
    }
}
?>
