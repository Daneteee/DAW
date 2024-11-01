<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diferència de Dates</title>
</head>
<body>
    <h1>Càlcul de Diferència entre Dates</h1>
    <form method="post" action="">
        <label for="data1">Data 1:</label>
        <input type="date" name="data1" required>
        <br>
        <label for="data2">Data 2:</label>
        <input type="date" name="data2" required>
        <br>
        <input type="submit" value="Calcular Diferència">
    </form>
    <br><br>
    
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        // Creem objectes DateTime
        $data1 = new DateTime($_POST["data1"]);
        $data2 = new DateTime($_POST["data2"]);

        // Comprovem que la primera data sigui major a la segona
        if ($data1 >= $data2) {
            echo "La primera data ha de ser més petita que la segona.";
        } else {
            $diferencia = $data1->diff($data2);
            
            // Primera línea con formato simple
            echo "* Hi ha una diferència de:<br>";
            echo "$diferencia->y anys, $diferencia->m mesos i $diferencia->d dies<br><br>";
            
            // Diferencias totales
            echo "Diferències totals:<br>";
            
            // Calculem les diferencies
            $total_dies = $diferencia->days;
            
            // Fem que cada 4 anys hi hagi un any de traspàs
            $total_anys = $total_dies / 365.25;

            // Fem una mitjana dels dies del més per tenir més exactitud
            $total_mesos = $total_dies / 30.436875; 
            $total_hores = $total_dies * 24;
            $total_minuts = $total_hores * 60;
            $total_segons = $total_minuts * 60;
            
            echo "$total_anys anys<br>";
            echo "$total_mesos  mesos<br>";
            echo "$total_dies dies<br>";
            echo "$total_hores hores<br>";
            echo "$total_minuts minuts<br>";
            echo "$total_segons segons";
        }
    }
    ?>

</body>
</html>
