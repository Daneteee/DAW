<?php
echo "<h1>PHP MVC </h1>";

require_once 'controllers/usuariController.php';

$controlador = new UsuariController();

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    $controlador->$action();
}

// http://localhost/mp7-php/UF3/MVC/MVC-01/index3.php?action=crearUsuari
// http://localhost/mp7-php/UF3/MVC/MVC-01/index3.php?action=mostrarTots


?>
