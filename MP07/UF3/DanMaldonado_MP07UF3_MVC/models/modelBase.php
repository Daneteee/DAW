<?php

require_once 'config/database.php';

class ModelBase {

    /**
     * Mètode per aconseguir tots els registres d'una taula.
     * @param string $taula El nom de la taula de la qual es volen obtenir els registres.
     * @return array Retorna un array associatiu amb els resultats.
     */
    public function aconseguirTots($taula) {
        try {
            $sql = "SELECT * FROM $taula";
            $stmt = $this->conn->prepare($sql);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            die("Error en aconseguirTots: " . $e->getMessage());
        }
    }
}

?>