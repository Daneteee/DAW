<?php
// 2. Declara un array de 2 dimensions amb el mesos i el nombre de dies corresponent. 
// Fes una funció que donat un mes que passem per get ens digui quants dies té. 

// Messos
$array_mesos = array(
    array("Gener", 31),
    array("Febrer", 28),
    array("Març", 31),
    array("Abril", 30),
    array("Maig", 31),
    array("Juny", 30),
    array("Juliol", 31),
    array("Agost", 31),
    array("Setembre", 30),
    array("Octubre", 31),
    array("Novembre", 30),
    array("Desembre", 31)
);

// Funció que calcula el dia
function dies_mes($nom_mes, $mesos) {
    foreach ($mesos as $mes) {
        if (strtolower($mes[0]) == strtolower($nom_mes)) {
            return "El mes de $nom_mes té $mes[1] dies.";;
        } else {
            return "ERROR: No s'ha trobat el mes $nom_mes.";
        }
    }
}

if (isset($_GET['mes'])) {
    echo dies_mes($_GET['mes'], $array_mesos);
} else {
    echo "ERROR: No s'ha introduït cap mes.";
}
