<?php
function generar_data() {
    // Generem un timestamp aleatori entre 18 i 80 anys
    $timestamp = strtotime(rand(18, 80) . ' years ago ' . rand(1, 365) . ' days');
    return date('Y-m-d', $timestamp); 
}

$noms = ['Marc', 'Anna', 'Josep', 'Maria', 'Pau', 'Laura', 'Joan', 'Marta', 'Pere', 'Carla'];
$cognoms = ['Garcia', 'Martinez', 'López', 'Serra', 'Puig', 'Vila', 'Ferrer', 'Soler', 'Costa', 'Vidal'];

// Obrim en mode escriptura, tot i que no caldría ja que a l'index ja comprovem 
// que només es creen les dades si l'arxiu està buit
$arxiu = fopen('dades.csv', 'w');

// Afegim la capçalera
fputcsv($arxiu, ['Nom', 'Cognom', 'Data_Naixement']);

for ($i = 0; $i < 100; $i++) {

    // Afegim la resta de dades
    $nom = $noms[array_rand($noms)];
    $cognom = $cognoms[array_rand($cognoms)];
    $data = generar_data();
    fputcsv($arxiu, [$nom, $cognom, $data]);
}

fclose($arxiu);
?>
