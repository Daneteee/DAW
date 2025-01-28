<?php

require_once 'config/db.php';

class ModelBase {

    public $conn;

    // Ens connectem a la BBDD
    public function __construct() {
        $this->conn = Conectat::conexio();

    }

    // Fem un select
    public function aconseguirTots($taula) {
        $result = $this->conn->query("SELECT * FROM $taula ORDER BY nom DESC");
        return $result;
    }
}

?>