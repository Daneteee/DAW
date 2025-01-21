<?php
echo "<h1>PHP MVC </h1>";

require_once 'controllers/usuariController.php';

$controlador = new UsuariController();
$controlador->mostrarTots();

// quina lògica segueix:
/*

- A index.php carreguem el controlador


- Tenim 3 carpetes:
    -models
    -controllers
    -views

    a models tenim usuari.php
    un arxiu que correspon a la classe usuari.php 
    donem un cop d'ull a la classe, fixem-nos en 
    el mètode aconseguir tots

    a controllers tenim usuariController.php
    un arxiu que correspon a la classe usuariController 
    (notació estàndard)
    donem un cop d'ull

    a la views tenim una carpeta per cada model
    amb les vistes per cada acció

*/

?>
