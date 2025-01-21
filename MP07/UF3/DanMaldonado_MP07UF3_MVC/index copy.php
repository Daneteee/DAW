<?php
echo "<h1>PHP MVC </h1>";

require_once 'controllers/usuariController.php';

$controlador = new UsuariController();
// 1r
//$controlador->mostrarTots();


/*

quina lògica segueix:

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

// 2n afegim crear Usuari

//$controlador->crearUsuari();

// 4t primer hauríem de mirar si existeix el controlador

if (isset($_GET['controller']) && class_exists($_GET['controller'])) 


// 3r ens cal una manera de fer-ho més dinàmic
// passem per get el mètode que volem cridar

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    $controlador->$action();
}



// fem la prova http://localhost/mp7-php/UF3/MVC/?action=mostrarTots
//              http://localhost/mp7-php/UF3/MVC/?action=crearUsuari










?>
