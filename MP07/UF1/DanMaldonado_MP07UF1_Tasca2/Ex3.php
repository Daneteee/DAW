<?php

// 3. Fes una pàgina on a partir d’un formulari on es recull una temperatura i en quina escala està, ens fa la conversió.

function conversor($de, $a, $temp) {

    // Condicionals per fer la conversió
    if ($de == 'celsius' && $a == 'fahrenheit') {
        return ($temp * 9/5) + 32;      
    } elseif ($de == 'celsius' && $a == 'kelvin') {
        return $temp + 273.15;
    } elseif ($de == 'fahrenheit' && $a == 'celsius') {
        return ($temp - 32) * 5/9;
    } elseif ($de == 'fahrenheit' && $a == 'kelvin') {
        return ($temp - 32) * 5/9 + 273.15;
    } elseif ($de == 'kelvin' && $a == 'celsius') {
        return $temp - 273.15;
    } elseif ($de == 'kelvin' && $a == 'fahrenheit') {
        return ($temp - 273.15) * 9/5 + 32;
    } else {
        return "ERROR: Valor incorrecte.";
    }
};

// Condicional per cridar a la funció
if (isset($_GET['convertir_de']) && isset($_GET['convertir_a']) && isset($_GET['temp'])) {
    $de = $_GET['convertir_de'];
    $a = $_GET['convertir_a'];
    $temp = $_GET['temp'];

    // Comprovem que sigui numeric
    if (is_numeric($temp)) {
        echo "La temperatura convertida es: " . conversor($de, $a, $temp);
    } else {
        echo "ERROR: La temperatura ha de ser un valor numèric.";
        return;
    } 
    
} else {
    echo "ERROR: Valor incorrecte.";
}
