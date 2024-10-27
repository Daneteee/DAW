<?php

function es_sencer_positiu($num) {
    return is_numeric($num) && $num > 0;
}

// 1.Fes una funció per calcular l’àrea d’un rectangle, Les dades provenen d’un formulari i tenint 
// en compte que la mida dels costats es passa per get. 

function calcular_area($numX, $numY) {
    // Obtenim els valors del formulari
        $numX = $_GET['length'];
        $numY = $_GET['width'];
    
        // Validem que els valors són numèrics i positius
        if (es_sencer_positiu($numX) && es_sencer_positiu($numY)) {
            // Calculem l'àrea
            $area = $numX * $numY;
            // Mostrem el resultat
            echo "L'àrea del rectangle és: " . htmlspecialchars($area);
        } else {
            echo "ERROR: Introdueix valors numèrics positius.";
        }
    }
    
calcular_area($numX, $numY);