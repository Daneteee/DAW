<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="utf-8" />
    <title>Pujar Arxius</title>
</head>

<body >
    <h1> Puja una imatge format jpg, peg o png </h1>
    <form method="post" action="" enctype="multipart/form-data">
        <input type="file" name="arxiu"/><br><br>
        <input type="submit" value="Puja Imatge" />
    </form>

    <?php
    // Comprovem si s'ha enviat el formulari i si hi ha un arxiu pujat sense errors
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES['arxiu']) && $_FILES['arxiu']['error'] === UPLOAD_ERR_OK) {

        $arxiu = $_FILES['arxiu'];
        $nom_arxiu = $arxiu['name'];
        $tipus = $arxiu['type'];

        // Comprovem si el tipus de l'arxiu és una imatge vàlida
        if ($tipus == "image/jpg" || $tipus == "image/jpeg" || $tipus == "image/png") {

            // Comprovem si la carpeta 'images' existeix, sino, la creem
            if (!is_dir('images')) {
                mkdir('images', 0777);
            } 
            
            // Definim la ruta de destí per a l'imatge
            $ruta_desti = 'images/' . $nom_arxiu;

            // Intentem moure l'arxiu pujat a la ruta de destí
            if (move_uploaded_file($arxiu['tmp_name'], $ruta_desti)) {

                // Si ha funcionat, mostrem un missatge de confirmació i mostrem la imatge a la pàgina
                echo "<h2> Imatge pujada correctament </h2>";
                echo "<img src='$ruta_desti' style='max-width: 100%;'>";
            } else {
                // Si hi ha un error al moure l'arxiu el mostrem
                echo "<h2>Error al pujar l'imatge</h2>";
            }
        } else {
            echo "<h2> Tipus d'imatge incorrecte </h2>";
        }
    }
    ?>

    
</body>
</html>

