<?php
echo "<h1>PHP MVC </h1>";

require_once 'controllers/usuariController.php';

$controlador = new UsuariController();
$controlador->mostrarTots();

// afegim crear Usuari

$controlador->crearUsuari();

?>
