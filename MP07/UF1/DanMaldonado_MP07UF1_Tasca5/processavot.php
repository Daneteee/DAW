<?php

session_start();

# Comprovem si l'usuari està loguejat
if (!isset($_SESSION['user'])) {
    $_SESSION['missatge'] = "On vas? Primer t'has de loguejar";
    header("Location: index.php");
    exit;
}

# Guardem una variable de l'usuari
$user = $_SESSION['user'];

# Comprovem si l'usuari ha votat, en cas que si, redirigim a logout.php
if (isset($_COOKIE['haVotat_' . $user])) {
    $_SESSION['missatge'] = "Ja has votat!!";
    header("Location: logout.php");
    exit;

} 

# Registrem el vot si l'usuari no ha votat
if (isset($_POST['vot'])) { 
    # Com estem al mateix navegador necessitem una cookie individual per a cada usuari, o fem afegint l'usuari al nom de la cookie
    setcookie("haVotat_" . $user, "true", time() + 3600);
    $_SESSION['missatge'] = "Vot registrat correctament!!";
    header("Location: logout.php");
    exit;

} 

?>