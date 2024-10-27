<?php

// Funció Anònima per Filtrar Array. Donat un array de números, utilitza una funció anònima dins array_filter per 
// retornar un nou array que conté només els elements que són múltiples de 3. Els nombres de l’array provindran d’un formulari, 
// els nombres s'escriuen separats per comes.

// Comprovar si el paràmetre 'filtre' existeix en la sol·licitud GET
if (isset($_GET['filtre'])) {
    // Convertir la cadena en un array de números
    $array_numeros = array_map('intval', explode(',', $_GET['filtre']));

    // Filtrar l'array per obtenir només els múltiplos de 3
    $array_multiples_3 = array_filter($array_numeros, function($numero) {
        return $numero % 3 == 0;
    });

    // Mostrem el resultat amb una llista
    echo "Múltiples de 3:";
    if (!empty($array_multiples_3)) {
        echo "<ul>";
        foreach ($array_multiples_3 as $numero) {
            echo "<li>$numero</li>";
        }
        echo "</ul>";
    } else {
        echo "No hi ha múltiples de 3 en l'array.";
    }
} else {
    echo "ERROR: Valor incorrecte.";
}