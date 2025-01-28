<?php
require_once __DIR__ . '/../models/nota.php';

class NotaController {


    public function mostrarTotes() {
        $nota = new Nota();
        $totesLesNotes = $nota->obtenirTotes(); 

        require_once __DIR__ . '/../views/notes/mostrarNotes.php';
    }


    // Mètode crear nota
    public function crear() {
        $nota = new Nota();

        $nota->setNom("Nota1");
        $nota->setContingut("Aquesta és una nota d'exemple per provar el mètode crear.");

        require_once __DIR__ . '/../views/notes/crearNota.php';
    }

    // Mètode per desar una nota
    public function desar() {

        $nota = new Nota();
        $nota->setNom('Exemple de nom');
        $nota->setContingut('Exemple de contingut');
    
        // Cridem al mètode per desar la nota
        $resultat = $nota->desarNota();
    
        // Comprovar si s'ha desat correctament
        if ($resultat) {
            echo "Nota desada correctament!";
        } else {
            echo "Error en desar la nota.";
        }
    }
    
}


?>