<?php

// Validador de Contrasenyes. Fes un formulari on passes les dades per POST. Escriu una funció que validi contrasenyes basant-se en els següents criteris: (No podeu utilitzar expressions regulars)
//      Almenys 8 caràcters de longitud.
//      Conté almenys una lletra majúscula.
//      Conté almenys un número.
//      Conté almenys un caràcter especial (com ara @, #, $, etc.).


function validador($contrasenya) {
    $longitud_c = (strlen($contrasenya) >= 8);
    $mayuscula_c = false;
    $numero_c = false;
    $especial_c = false;

    
    for ($i = 0; $i < strlen($contrasenya); $i++) {
        $caracter = $contrasenya[$i];

        // Comprovem si és una lletra majúscula
        if (ctype_upper($caracter)) {
            $mayuscula_c = true;
        }

        // Comprovem si és un número
        if (ctype_digit($caracter)) {
            $numero_c = true;
        }

        // Comprovem si és un caràcter especial
        if (in_array($caracter, ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'])) {
            $especial_c = true;
        }
    }
    return $longitud_c && $mayuscula_c && $numero_c && $especial_c;
}

// Condicional per cridar a la funció
if (isset($_POST['contrasenya'])) {
    
    if (validador($_POST['contrasenya'])) {
        echo "Contrasenya vàlida.";
    } else {
        echo "Contrasenya invàlida.";
    }

} else {
    echo "ERROR: Valor incorrecte.";
}