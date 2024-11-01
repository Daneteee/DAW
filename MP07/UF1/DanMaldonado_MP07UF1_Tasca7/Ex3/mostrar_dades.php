<?php
$files_per_pagina = 20;

// Funció per llegir les dades d'un arxiu
function llegir_dades($arxiu) {
    $dades = [];

    // Obrim l'arxiu i comprovem que no doni error
    if (($fopen = fopen($arxiu, 'r')) !== FALSE) {
        
        // Ens saltemm la primera línia
        fgetcsv($fopen);

        // Anem afegim l'array de dades a $data, comprovant que no sigui FALSE, ja que significaría
        // que s'ha arribat al final de l'arxiu, i les afegim a l'array
        while (($data = fgetcsv($fopen)) !== FALSE) {
            $dades[] = $data; 
        }
        fclose($fopen); 
    }

    return $dades; 
}


// Funció per ordenar les dades
function ordenar_dades($dades, $criteri, $ordre = 'asc') {
    // Amb array column agafem la columna del csv
    $columna = array_column($dades, $criteri);

    // Canviem el ordre d'ordenació
    $sort_order = ($ordre === 'asc') ? SORT_ASC : SORT_DESC;

    // Ordenem multiples arrays amb el multisort, de forma ascendent, per columna
    array_multisort($columna, $sort_order, $dades);
    
    return $dades;
}


// Funció per filtrar les dades
function filtrar_dates($dades, $data_inici, $data_fi) {

    // Amb array filter i una funció fletxa, retornem només les dades que es trobin entre la data d'inici i la de fi
    // $d[2] és la columna de la data de naixement al csv
    return array_filter($dades, fn($d) => $d[2] >= $data_inici && $d[2] <= $data_fi);
}


// Agafem les dades
$dades = llegir_dades('dades.csv');

// Determinem l'ordre actual d'ordenació
$ordre = (isset($_GET['ordre']) && $_GET['ordre'] === 'desc') ? 'desc' : 'asc';

// Ordenem les dades en cas que hi hagi un paràmetre d'ordenació
if (isset($_GET['ordenar'])) {
    // Guardem el criteri com a un enter
    $criteri = $_GET['ordenar'] === 'nom' ? 0 : 1;
    
    // Si l'ordenació actual és 'asc', passem a 'desc' i viceversa
    $ordre = ($ordre === 'asc') ? 'desc' : 'asc';
    
    // Ordenem les dades
    $dades = ordenar_dades($dades, $criteri, $ordre);
}

// Filtrem les dades
if (isset($_GET['data_inici']) && isset($_GET['data_fi'])) {
    $data_inici = $_GET['data_inici'];
    $data_fi = $_GET['data_fi'];
    $dades = filtrar_dates($dades, $data_inici, $data_fi);
}

// Paginació
$dades_totals = count($dades);

// Aqui guardem la pàgina on ens trobem, si es la primera vegada que entrem, serà la primera
$pagina_actual = isset($_GET['pagina']) ? (int)$_GET['pagina'] : 1;

// Amb el ceil busquem arrodonir un nombre cap a dalt, per exemple, 40 línies de dades entre 20 files per pàgina dona 2.25
// Però amb el ceil serà 3, així agafem 3 pàgines senceres.
$pagines_totals = ceil($dades_totals / $files_per_pagina);

// Depenén d'on acabem la pagina, la següent començarà amb un index o un altre
$punter = ($pagina_actual - 1) * $files_per_pagina;

// Obtenim les dades de la página acutal
$dades_pagina = array_slice($dades, $punter, $files_per_pagina);

?>

<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>Mostrar Dades</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: purple;
            color: white;
        }
        .paginacio {
            display: flex;
            justify-content: space-between;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h2>Llistat d'Usuaris</h2>
    
    <a href="index.php">Inici</a>
    <form method="get">
        <label for="data_inici">Data Inici:</label>
        <input type="date" id="data_inici" name="data_inici">
        
        <label for="data_fi">Data Fi:</label>
        <input type="date" id="data_fi" name="data_fi">
        
        <button type="submit">Filtrar</button>
    </form>


    <!-- Creem variables i al click fiquem "location.href", el qual ens permet afegir a la url dades
     això ens serveix per ordenar les dades sense haver d'enviar un "type=submit" -->
    <?php
    $url_ordenar_nom = "?ordenar=nom&ordre=" . $ordre;
    $url_ordenar_cognom = "?ordenar=cognom&ordre=" . $ordre;
    ?>
    <button onclick="location.href='<?php echo $url_ordenar_nom; ?>'">Ordenar per Nom</button>
    <button onclick="location.href='<?php echo $url_ordenar_cognom; ?>'">Ordenar per Cognom</button>

    <!-- Mostrem las dades a la taula -->
    <table>
        <tr>
            <th>Nom</th>
            <th>Cognom</th>
            <th>Data de Naixement</th>
        </tr>
        <?php 
        foreach ($dades_pagina as $dada) {
            // Per cada dada comprovem que sigui segur el que s'introdueix
            echo "<tr>
                    <td>" . htmlspecialchars($dada[0]) . "</td>
                    <td>" . htmlspecialchars($dada[1]) . "</td>
                    <td>" . htmlspecialchars($dada[2]) . "</td>
                </tr>";
        }
        ?>
    </table>

    <div class="paginacio">
        <div>
            <?php
                // En cas que no estem a la primera pàgina, mostrem els links per anar a la primera pàgina i per anar enrere, restant 1 a la pàgina actual, en cas que no, no mostrem res, resta
                echo $pagina_actual > 1 ? '<a href="?pagina=1">&lt;&lt;</a> <a href="?pagina=' . ($pagina_actual - 1) . '">&lt;</a>' : '';
                
                // Mostrem el peu de pàgina
                echo 'Pàgina ' . $pagina_actual . ' de ' . $pagines_totals;

                // Aqui també, en cas que no estem a l'última pàgina, mostrem els links per anar avançar la pàgina i per anar a l¡última, afegint 1 a la pàgina actual per avançar, en cas que no, no mostrem res
                echo $pagina_actual < $pagines_totals ? ' <a href="?pagina=' . ($pagina_actual + 1) . '">&gt;</a> <a href="?pagina=' . $pagines_totals . '">&gt;&gt;</a>' : '';
            ?>
        </div>
    </div>
</body>
</html>
