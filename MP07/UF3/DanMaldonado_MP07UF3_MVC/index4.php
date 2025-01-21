<?php
echo "<h1>PHP MVC </h1>";

require_once 'controllers/usuariController.php';
$error = false;

// Convertim l'índex en un controlador frontal
// mirem si existeix el controlador 1r

if (isset($_GET['controller']) && class_exists($_GET['controller'].'Controller')) {
    $nom_controlador = $_GET['controller'].'Controller';
    $controlador = new $nom_controlador;

    // en aquest cas mirem que existeixi el mètode
    if (isset($_GET['action']) && method_exists($nom_controlador, $_GET['action'])) {
        $action = $_GET['action'];
        $controlador->$action();
    }
    else {
        $error = true;
    }
    

} else {
    $error =true;
}

if ($error) {
    echo "Error: Aquesta pàgina no existeix";
}

// Provem el codi

// http://localhost/mp7-php/UF3/MVC/MVC-01/index4.php?controller=usuari&action=mostrarTots
// http://localhost/mp7-php/UF3/MVC/MVC-01/index4.php?controller=usuari&action=crearUsuari
// http://localhost/mp7-php/UF3/MVC/MVC-01/index4.php?controller=usuari&action=nuse
// http://localhost/mp7-php/UF3/MVC/MVC-01/index4.php?controller=nuse&action=mostrarTots




?>
