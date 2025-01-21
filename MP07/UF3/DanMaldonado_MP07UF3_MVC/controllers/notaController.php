<?php

class NotaController {

    public function mostrarTots(){

        require_once 'models/usuari.php';

        $usuari = new Usuari();
        $totsElsUsuaris=$usuari->aconseguirTots();

        require_once 'views/usuaris/mostrarTots.php';


    }

    public function crearUsuari() {

        require_once 'views/usuaris/crearUsuari.php';

    }

}
?>