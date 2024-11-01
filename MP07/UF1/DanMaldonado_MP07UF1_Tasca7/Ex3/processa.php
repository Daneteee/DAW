<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $nom = $_GET['nom'];
    $cognom = $_GET['cognom'];
    $data_naixement = $_GET['data_naixement'];

    // Obrir l'arxiu en mode append
    $arxiu = fopen('dades.csv', 'a');
    
    // Escriure les noves dades
    fputcsv($arxiu, [$nom, $cognom, $data_naixement]);
    
    // Tancar l'arxiu
    fclose($arxiu);
    
    // Redirigir amb missatge d'èxit
    header("Location: mostrar_dades.php");
    exit();
}
?>   