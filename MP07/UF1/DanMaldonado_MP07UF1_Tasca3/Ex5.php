<?php
#Crea el codi PHP que donin resposta a el següent plantejament:
#   Volem emmagatzemar en una matriu el nombre d'alumnes amb què compta una acadèmia, ordenats en funció de el nivell i de l'idioma que s'estudia. 
#   Hi haurà 3 files que representaran el Nivell bàsic, mitjà i de perfeccionament i 4 columnes en què figuraran els idiomes (0 = Anglès, 1 = Francès, 2 = Alemany i 3 = Rus). 
#   Es demana realitzar la declaració de la matriu i assignar-els valors indicats en la següent imatge a cada element:

# Fes les següents funcions : 
#  comptarTotalAlumnes, presenta el total d’alumnes de l’academia
#  comptarTotalAIdiomes, presenta el total d’alumnes per idioma ordenat de més a menys (amb un array associatiu)
#  buscarGrupMesNombros, presenta per pantalla el grup més nombrós
#  buscarGrupMenysNombros, presenta per pantalla el grup menys nombrós

include ("header.php");

# Definim la matriu amb el nombre d'alumnes per nivell i idioma
$alumnes = [
    [1, 14, 8, 3], 
    [6, 19, 7, 2],   
    [3, 13, 4, 1]  
];

# Contem el total d'alumnes
function comptarTotalAlumnes($alumnes) {
    $total = 0;
    # Sumem tots els alumnes
    foreach ($alumnes as $fila) {
        foreach ($fila as $valor) {
            $total += $valor;
        }
    }
    return $total;
}

# Comptem el total d'alumnes per idioma
function comptarTotalAIdiomes($alumnes) {
    $totalIdioma = [];
    foreach ($alumnes as $fila) {
        for ($idioma = 0; $idioma < 4; $idioma++) {
            $totalIdioma[$idioma] += $fila[$idioma]; 
        }
    }
    # Ordenem
    arsort($totalIdioma);
    return $totalIdioma;
    
}

# Busquem el grup més nombrós
function buscarGrupMesNombros($alumnes) {
    $max = 0;
    $idiomaIndex = 0; 
    $nivellIndex = 0; 

    # Per cada nivell i idioma comprovem si supera el màxim i actualitzem els valors
    foreach ($alumnes as $nivell => $idiomes) {
        foreach ($idiomes as $idioma => $valor) {
            if ($valor > $max) {
                # En cas que superem el màxim guardem el valor, l'idioma i el nivell
                $max = $valor;
                $idiomaIndex = $idioma; 
                $nivellIndex = $nivell; 
            }
        }
    }
    return [$max, $idiomaIndex, $nivellIndex];
}

# Busquem el grup menys nombrós
function buscarGrupMenysNombros($alumnes) {
    $min = PHP_INT_MAX;
    $idiomaIndex = 0; 
    $nivellIndex = 0; 

    # Per cada nivell i idioma comprovem si supera el màxim i actualitzem els valors
    foreach ($alumnes as $nivell => $idiomes) {
        foreach ($idiomes as $idioma => $valor) {
            if ($valor < $min && $valor > 0) {
                # En cas que superem el mínim guardem el valor, l'idioma i el nivell
                $min = $valor;
                $idiomaIndex = $idioma; 
                $nivellIndex = $nivell; 
            }
        }
    }
    return [$min, $idiomaIndex, $nivellIndex];
}

# Executem les funcions
$idiomes = ['Anglès', 'Francès', 'Alemany', 'Rus'];
$nivells = ['Bàsic', 'Mitjà', 'Perfeccionament'];

# Mostrem el total d'alumnes
$totalAlumnes = comptarTotalAlumnes($alumnes);
echo "Total d'alumnes a l'acadèmia: $totalAlumnes<br>";
echo "<br>";

# Mostrem el total d'alumnes per idioma
$totalIdiomes = comptarTotalAIdiomes($alumnes);
echo "Total d'alumnes per idioma (ordenat de més a menys):<br>";
foreach ($totalIdiomes as $idioma => $total) {
    echo "$idiomes[$idioma]: $total<br>"; 
}
echo "<br>";

# Mostrem el grup més nombrós
$grupMesNombros = buscarGrupMesNombros($alumnes);
echo "El grup més nombrós és de: " . $grupMesNombros[0] . " alumnes, en el nivell " . $nivells[$grupMesNombros[2]] . " i en el idioma " . $idiomes[$grupMesNombros[1]];
echo "<br>";

# Mostrem el grup menys nombró
$grupMenysNombros = buscarGrupMenysNombros($alumnes);
echo "El grup menys nombrós és de: " . $grupMenysNombros[0] . " alumnes, en el nivell " . $nivells[$grupMenysNombros[2]] . " i en el idioma " . $idiomes[$grupMenysNombros[1]];

include ("footer.php");
?>