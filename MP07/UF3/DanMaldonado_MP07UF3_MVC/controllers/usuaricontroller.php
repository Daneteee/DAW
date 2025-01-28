<?php

class UsuariController {

    // El controlador encapsula accions
    // una acció de crear usuari, mostrar usuari, ...


    //fixem-nos el nom del mètode
    // carreguem el model
    // fem un usari nou
    // a una variable li assignem el resultat del
    // mètode aconseguir tots
    // carreguem a la vista


    public function mostrarTots(){
        
        require_once __DIR__ . '/../models/usuari.php';
        
        $usuari = new Usuari();
        $totsElsUsuaris=$usuari->aconseguirTots("usuaris");

        require_once __DIR__ . '/../views/usuaris/mostrarTots.php';


    }

    public function crearUsuari() {
        

    }

}
?>